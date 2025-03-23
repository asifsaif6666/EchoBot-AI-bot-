'''
1A - Speech to Text using Google's SpeechRecognition API
'''
#from Speech_to_text import play_sound

import speech_recognition as sr
import pygame

pygame.mixer.init()
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)


def listen_with_google():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening ... ")
        play_sound(r"E:\Downloads\yolo\echobot\Resources\listen.mp3")
        audio = recognizer.listen(source)
        play_sound(r"E:\Downloads\yolo\echobot\Resources\convert.mp3")
        recognizer.adjust_for_ambient_noise(source)
        text = recognizer.recognize_google(audio)
        print("You said: "+ text)
        return text

##--------MAIN-----------

listen_with_google()