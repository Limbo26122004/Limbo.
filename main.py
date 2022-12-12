import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import wolframalpha
from ecapture import ecapture as ec
from googletrans import Translator
import time 
import ctypes
import winshell 
import os

openai.api_key=api_data

completion=openai.Completion()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello How Are You? ")

def  takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}")

    except Exception as e:
        speak(" ")
        return "none"
    return query

if __name__ == '__main__':
    while True:
        query=takeCommand().lower()

        if 'battery' in query or 'how much power left' in query or 'how much power we have' in query:
            
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        

        elif 'net speed' in query or 'internet speed' in query or 'speed of internet' in query or 'speed of net' in query or 'data speed' in query:
            import speedtest
            speedtester = speedtest.Speedtest()
            dl = speedtester.download()
            up = speedtester.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif 'search' in query: 
            query = query.replace("search", "")	
            webbrowser.open(query)

        if 'launch' in query or 'open' in query:
            query = query.replace('open','')
            query = query.replace('launch','')
            query = query.replace('  ','')
            webbrowser.open(query)

        elif "play a song" in query or "play song" in query:
            import random
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Kaushal\\Music"
            songs = os.listdir(music_dir)
            s = random.randint(0,391)
            os.startfile(os.path.join(music_dir, songs[s])) 

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "C:\\Users\\Kaushal\\Pictures\\Wallpaper",
                                                    0)
            speak("Background changed successfully")

        elif 'joke' in query:
            import pyjokes
            speak(pyjokes.get_joke())
       
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        if "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query or "log out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "IP address" in query:
            from requests import get
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")


        if 'bye' in query:
            break

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'lock' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown /s')

        elif "change your name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand().lower()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "LIMBO" in query:
            speak("LIMBO in your service Mister")
            speak(assname)

        elif 'play music' in query:
            webbrowser.open("music.google.com")         

        elif 'mail' in query:
            webbrowser.open("mail.google.com")

        elif 'earth' in query:
            webbrowser.open("earth.google.com")
            
        elif 'sky' in query:
            webbrowser.open("sky.google.com")


        else:
            def Reply(question):
                prompt=f'Kaushal: {question}\n Limbo: '
                response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Kaushal'], max_tokens=200)
                answer=response.choices[0].text.strip()
                return answer

            ans=Reply(query)
            print(ans)
            speak(ans)



