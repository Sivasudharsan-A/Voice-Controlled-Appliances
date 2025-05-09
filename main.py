# main.py

import pyttsx3
import speech_recognition as sr
from controller import control_appliance

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return None

def main():
    speak("Say a command to control the appliance.")
    
    while True:
        command = listen_for_command()
        if command:
            if "turn on light" in command:
                control_appliance("light", "turn on")
                speak("Turning on the light.")
            elif "turn off light" in command:
                control_appliance("light", "turn off")
                speak("Turning off the light.")
            elif "turn on fan" in command:
                control_appliance("fan", "turn on")
                speak("Turning on the fan.")
            elif "turn off fan" in command:
                control_appliance("fan", "turn off")
                speak("Turning off the fan.")
            elif "exit" in command or "quit" in command:
                speak("Exiting program.")
                break
            else:
                speak("Command not recognized. Try again.")

if __name__ == "__main__":
    main()
