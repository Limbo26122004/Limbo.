import os
import speech_recognition as sr
#from playsound import playsound

#playsound("C:\\Users\\Kaushal\\Desktop\\powerfull_jarvis_python-main\\powerfull_jarvis_python-main\\Sounds\\JARVIS.mp3")

def  takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}")

    except Exception as e:
        return "none"
    return query

while True:

    wake_Up = takeCommand().lower()

    if "wake up" in wake_Up or "uth jaa" in wake_Up or "uth ja" in wake_Up or "uth jao" in wake_Up or "Jarvis" in wake_Up or "make up" in wake_Up:
        os.startfile("C:\\Users\\Kaushal\\Desktop\\powerfull_jarvis_python-main\\powerfull_jarvis_python-main\\main.py")

    else:
        print("Nothing........")