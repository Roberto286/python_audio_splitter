# Audio Splitter

This Python program allows you to split a long audio file into smaller segments of 10 seconds each. It uses the `pydub` library to handle audio operations and works with various supported audio formats such as MP3, WAV, OGG, FLAC, and AAC.

## Prerequisites

To run this program, you need to have the following installed on your system:

1. Python (3.6 or higher)
2. `pydub` library

You can install the `pydub` library using `pip`:

pip install pydub


## How to Use

1. Clone or download this repository to your local machine.
2. Place the audio file you want to split in the "audio_to_split" folder within the repository directory.
3. Open a terminal or command prompt in the repository directory.
4. Run the program using the following command:

python audio_splitter.py


## Important Notes

- The audio file must be at least 10 seconds long for the program to work correctly.
- The program can only process one audio file at a time. Make sure you have only one audio file in the "audio_to_split" folder.

## Customization

If you need to change the input folder or the output folder for the splitted audio segments, you can do so by modifying the following lines in the `audio_splitter.py` file:

```python
input_folder = "audio_to_split"
output_folder = "splitted_audios"

Replace "audio_to_split" with the path to the folder containing your input audio file, and "splitted_audios" with the desired output folder path.

License
This program is provided under the MIT License. Feel free to use and modify it according to your needs.

Disclaimer
The author of this program is not responsible for any misuse or damages caused by the use of this software. Always ensure you have the necessary rights to use and modify the audio files.
