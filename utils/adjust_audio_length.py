def adjust_length(file_path, final_duration):
    y, sr = librosa.load(file_path, sr=None)
    current_duration = librosa.get_duration(y=y, sr=sr)

    if current_duration >= final_duration:
        y = y[:int(final_duration * sr)]

    elif current_duration < final_duration:
        silence_duration = final_duration - current_duration
        silence_samples = int(silence_duration * sr)
        silence = np.zeros(silence_samples)
        y = np.concatenate((y, silence), axis=0)

    sf.write(file_path, y, sr)