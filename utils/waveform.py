import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load the audio file
audio_path = 'audio.wav'
y, sr = librosa.load(audio_path)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.savefig('waveform.png')
plt.show()
