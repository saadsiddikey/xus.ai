import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I didn't understand"
    except sr.RequestError:
        return "Error connecting to Google Speech API"

def open_app(command):
    if "open youtube" in command:
        os.system("start https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        os.system("start https://www.google.com")
        speak("Opening Google")
    elif "play music" in command:
        os.system("start https://www.spotify.com")
        speak("Playing music")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    else:
        speak("Sorry, I can't do that yet.")

while True:
    command = listen()
    if "exit" in command:
        speak("Goodbye!")
        break
    else:
        open_app(command)
