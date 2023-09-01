from flask import Flask, request, render_template, jsonify
import numpy as np
import soundfile as sf
import librosa
import keras

app = Flask(__name__)
model = keras.models.load_model('model.h5')
model_classes = ["German", "English", "Spanish", "Persian"]

def adjust_length(file_path):
    y, sr = librosa.load(file_path, sr=None)
    target_duration = 10
    current_duration = librosa.get_duration(y=y, sr=sr)

    if current_duration >= target_duration:
        y = y[:int(target_duration * sr)]

    elif current_duration < target_duration:
        silence_duration = target_duration - current_duration
        silence_samples = int(silence_duration * sr)
        silence = np.zeros(silence_samples)
        y = np.concatenate((y, silence), axis=0)

    sf.write(file_path, y, sr)

def spectrogram_mat(file_path):
    clip, sample_rate = librosa.load(file_path, sr=22050)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    SP = librosa.power_to_db(S, ref=np.max)
    #np.save(save_prefix+file, SP)
    return SP

def process_audio(file_path):
    adjust_length(file_path)
    return spectrogram_mat(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    import timeit
    first= timeit.timeit()
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        audio_path = 'temp_audio.wav'
        uploaded_file.save(audio_path)
        processed_data = process_audio(audio_path)
        prediction = model.predict(np.array([processed_data]))
        predicted_label = prediction.argmax(axis=1)[0]
        #print(f'it says {predicted_label}')
        return jsonify({'language': model_classes[predicted_label]})
    end= timeit.timeit()
    print(end-first)

if __name__ == '__main__':
    app.run(debug=True)
