import subprocess
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel
from vosk.transcriber.transcriber import Transcriber
from types import SimpleNamespace

SAMPLE_RATE = 16000

SetLogLevel(0)

def secondary():
    model = Model(lang="en-us")
    rec = KaldiRecognizer(model, SAMPLE_RATE)

    with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                                "test.wav",#sys.argv[1],
                                "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                                stdout=subprocess.PIPE) as process:

        while True:
            data = process.stdout.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())
            else:
                print(rec.PartialResult())
        f_res = rec.FinalResult()
        print("f: ", f_res)
        pass

def main():
    #model = Model(lang="en-us")
    model_name = None #"vosk-model-en-us-0.22"#"vosk-model-en-us-0.22"
    model_path = "vosk-model-en-us-0.22"#vosk-model-small-en-us-0.15"
    # Original code
    args = {
        "model": model_path,
        "model_name": model_name,
        "lang": None,
        "server": None,
        "output_type": "json"
    }

    # Convert to an object with attribute access
    args = SimpleNamespace(**args)
    t = Transcriber(args)
    t.process_task_list([("test.mp3","test.json")])

main()