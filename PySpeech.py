import json
import pyaudio
import vosk




def initialize_model(model_path):
    return vosk.Model(model_path)


def initialize_pyaudio():
    return pyaudio.PyAudio()


def open_microphone_stream(audio_device, rate, channels, frames_per_buffer):
    stream = audio_device.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    stream.start_stream()
    return stream


def recognize_speech(stream, recognizer: vosk.KaldiRecognizer):
    print("Listening...")
    last_partial_text = ""
    try:
        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                res_dict = json.loads(result)
                text = res_dict.get('text', '')
                print("Dict: " + result)
                print("You said: " + text)
                last_partial_text = ""
                if text == "stop":
                    raise KeyboardInterrupt
            else:
                partial_result = recognizer.PartialResult()
                partial_text = json.loads(partial_result).get('partial', '')
                if partial_text != last_partial_text:
                    print("Partial: " + partial_text)
                    last_partial_text = partial_text
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()


def main():
    # Initialize the model
    model_path = "vosk-model-en-us-0.22"
    model = initialize_model(model_path)

    # Initialize the audio device
    audio_device = initialize_pyaudio()
    rate = 16000
    channels = 1
    frames_per_buffer = 8192
    stream = open_microphone_stream(audio_device, rate, channels, frames_per_buffer)

    # Initialize the recognizer
    recognizer = vosk.KaldiRecognizer(model, 16000)
    recognize_speech(stream, recognizer)

    # If recognize_speech() is interrupted, close the stream and terminate the audio device
    audio_device.terminate()


if __name__ == "__main__":
    main()