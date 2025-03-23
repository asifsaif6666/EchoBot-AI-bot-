'''
Step 1:
Speech to Text using VOSK offline API

Download VOSK model from: https://alphacephei.com/vosk/models
'''

import vosk
import pyaudio
import json
import pygame

pygame.mixer.init()
model = vosk.Model(r"E:\Downloads\yolo\echobot\Resources\vosk-model-small-en-us-0.15")
#model = vosk.Model(r"E:\Downloads\yolo\echobot\Resources\vosk-model-en-in-0.5")
recognizer = vosk.KaldiRecognizer(model, 16000)
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait for audio to finish playing
        pygame.time.Clock().tick(5)

def listen_with_vosk():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    print("Listening ...")
    play_sound(r"E:\Downloads\yolo\echobot\Resources\listen.mp3")

    while True:
        data = stream.read(8192)
        if len(data) == 0:
            continue

        if recognizer.AcceptWaveform(data):
            play_sound(r"E:\Downloads\yolo\echobot\Resources/convert.mp3")
            result =  recognizer.Result()
            text = json.loads(result)["text"]
            print("You said: " + text)
            return text

###-------------MAIN-------------

while True:
    listen_with_vosk()
