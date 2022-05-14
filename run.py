import copy
import json
import multiprocessing as mp
import numpy as np
import soundcard as sc
import sounddevice as sd
import vosk

def capture_audio_output(audio_queue: mp.Queue,
                         capture_sec: float,
                         sample_rate: int) -> None:
    
    num_frame: int = int(sample_rate * capture_sec)
    
    while True:
        audio = sc.get_microphone(include_loopback=True, id=str(sc.default_speaker().name)) \
            .record(numframes=num_frame, samplerate=sample_rate, blocksize=sample_rate)
        audio_queue.put(copy.copy(audio[:, 0]))


def speech_to_text(audio_queue: mp.Queue,
                   sample_rate: int) -> None:
    NO_LOG: int = -1
    MODEL_PATH = "model"
    
    vosk.SetLogLevel(NO_LOG)
    
    model: vosk.Model = vosk.Model(MODEL_PATH)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)
    
    print("Recognizer is ready")
    print("Output sound from a speaker or a headphone")
    print("#" * 40)
    
    while True:
        audio = audio_queue.get()
        audio = map(lambda x: (x+1)/2, audio)
        audio = np.fromiter(audio, np.float16)
        audio = audio.tobytes()
        
        if recognizer.AcceptWaveform(audio):
            result: json = json.loads(recognizer.Result())
            text = result["text"].replace(" ", "")
            
            if text != "":
                print(text)

def main():
    CAPTURE_SEC: int = 0.4
    
    audio_queue: mp.Queue = mp.Queue()
    sample_rate: int = int(sd.query_devices(kind="output")["default_samplerate"])
    stt_proc: mp.Process = mp.Process(target=speech_to_text,
                                      args=(audio_queue, sample_rate))
    
    print("Type Ctrl+C to stop")
    
    stt_proc.start()
    
    try:
        capture_audio_output(audio_queue=audio_queue, capture_sec=CAPTURE_SEC, sample_rate=sample_rate)
        stt_proc.join()
    except KeyboardInterrupt:
        stt_proc.terminate()
        
        print("\nDone")


if __name__ == "__main__":
    main()
