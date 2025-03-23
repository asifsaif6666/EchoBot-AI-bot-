import speech_recognition as sr
import pygame
import google.generativeai as genai
import pyttsx3
import time

# ---------------------- CONFIGURE GEMINI API -----------------------
genai.configure(api_key="AIzaSyDcx39dpx5qe4OKSe6L7hi7W7s9bb_KVb0")  # Replace with your key
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# ---------------------- SOUND EFFECTS -----------------------
pygame.mixer.init()

def play_sound(file_path):
    """Play a sound effect from the given file path."""
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)

# ---------------------- SPEECH TO TEXT (OPTIMIZED) -----------------------
def listen_with_google():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening... Speak now!")
        
        # Play listening sound (optional)
        play_sound(r"E:\Downloads\yolo\echobot\Resources\listen.mp3")  # Replace with your path

        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=30)  # Supports long sentences
            play_sound(r"E:\Downloads\yolo\echobot\Resources\convert.mp3")  # Replace with your path
            
            print("\nProcessing speech...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None
        except Exception as e:
            print("Error:", e)
            return None

# ---------------------- AI MODEL (GEMINI API) -----------------------
def gemini_api(text):
    """Generate AI response using Gemini API."""
    try:
        response = model.generate_content(text)
        return response.text.strip()  # Get only the AI-generated response
    except Exception as e:
        print("Error with Gemini API:", e)
        return "Sorry, I couldn't process your request."

# ---------------------- TEXT TO SPEECH -----------------------
def text_to_speech(text, voice_index=0, rate=170, volume=1.0):
    """Convert text to speech and speak it."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)  # 0 for male, 1 for female
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    print("\nAI: " + text)  # Display the response
    engine.say(text)
    engine.runAndWait()

# ---------------------- MAIN PROGRAM LOOP -----------------------
def interactive_ai_robot():
    print("\nWelcome to Interactive AI Robot! (Say 'exit' to stop)")
    while True:
        user_input = listen_with_google()
        if user_input:
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("\nExiting AI Robot...")
                text_to_speech("Goodbye! Have a great day!", voice_index=1)
                break

            ai_response = gemini_api(user_input)
            text_to_speech(ai_response, voice_index=1)  # Female voice

            time.sleep(1)  # Small delay before next interaction

# ---------------------- RUN THE AI ROBOT -----------------------
interactive_ai_robot()
