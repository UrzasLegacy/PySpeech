# PySpeech 🎤

PySpeech is a Python script that uses the Vosk speech recognition toolkit to transcribe real-time audio from your microphone.

<p align="center"><img src="https://github.com/user-attachments/assets/736c09c7-8ded-4a6c-8fd4-230536f823f3" alt="cover"></p>

## Description 📝

This script initializes a Vosk model and a PyAudio stream to capture audio from your microphone. It then uses the Vosk recognizer to transcribe the audio offline, and in real-time, printing both partial and final transcriptions to the console.


## Key Notes 📌

- The script uses the Vosk speech recognition toolkit.
- It captures audio using PyAudio.
- Real-time transcription is printed to the console.
- Only tested on Windows, but it should work on Linux/Mac


## Installation 🛠️

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Nenotriple/PySpeech.git
    cd PySpeech
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```


## Usage 🚀

1. **Run the script:**
    ```sh
    python PySpeech.py
    ```

2. **Speak into your microphone:**
    - The script will print `Listening...` and start transcribing your speech.
    - Partial transcriptions will be printed as `Partial: ...`.
    - Final transcriptions will be printed as `You said: ...`.

3. **Stop the script:**
    - Press `Ctrl+C` to stop the script. The script will handle the interrupt and close the audio stream gracefully. *(Or close the terminal)*


## Additional Notes 🗒️

- Ensure your microphone is properly configured and accessible by PyAudio.
  - It should be the default input device.
- The script is configured to use a sample rate of 16000 Hz and a single audio channel.
- Additional Vosk models can be found here: https://alphacephei.com/vosk/models
