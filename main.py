import os
from pydub import AudioSegment


def is_audio_file(file_path):
    audio_extensions = [".mp3", ".wav", ".ogg", ".flac", ".aac"]
    return os.path.splitext(file_path)[1].lower() in audio_extensions


def split_audio(input_file, output_folder):
    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"Error: {e}")
        return

    if not is_audio_file(input_file):
        print("The specified file is not a supported audio file.")
        return

    if len(audio) < 10000:
        print("The audio file must be at least 10 seconds long.")
        return

    segment_duration = 10 * 1000
    num_segments = len(audio) // segment_duration + \
        (1 if len(audio) % segment_duration else 0)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        for file_name in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    output_file_format = os.path.splitext(input_file)[1]
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        segment = audio[start_time:end_time]
        segment.export(os.path.join(
            output_folder, f"segment_{i}{output_file_format}"), format=output_file_format[1:])


if __name__ == "__main__":
    input_folder = "audio_to_split"
    output_folder = "splitted_audios"

    if not os.path.exists(input_folder):
        print(
            f"The folder {input_folder} does not exist. Make sure to place the audio file in the correct folder.")
    else:
        audio_files = [file for file in os.listdir(
            input_folder) if os.path.isfile(os.path.join(input_folder, file))]
        if len(audio_files) != 1:
            print("The program can only work with one file at a time. Make sure you have only one audio file in the 'audio_to_split' folder.")
        else:
            input_file_path = os.path.join(input_folder, audio_files[0])
            split_audio(input_file_path, output_folder)
            print("Splitting has been completed successfully.")
