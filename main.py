import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import time 
import ctypes
import winshell 
import os
import pyautogui
import openai
import datetime
from apikey import api_data

#from playsound import playsound

#playsound("C:\\Users\\Kaushal\\Desktop\\powerfull_jarvis_python-main\\powerfull_jarvis_python-main\\Sounds\\JARVIS STARTUP SOUND.mp3")

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
    prompt=f'Kaushal: {question}\n Jarvis: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Jarvis'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")

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
    
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    
    while True:
        query=takeCommand().lower()

        if 'battery' in query or 'how much power left' in query or 'how much power we have' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        elif 'search' in query: 
            query = query.replace("search", "")	
            webbrowser.open(query)

        elif 'launch' in query :
            #query = query.replace('open','')
            query = query.replace('launch','')
            query = query.replace('  ','')
            webbrowser.open(query)

        elif "play a song" in query or 'gana' in query or 'gane' in query or 'bajao' in query or 'baja' in query or 'play songs' in query or 'song' in query or 'songs' in query:
            import random
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\Kaushal\\Music"
            songs = os.listdir(music_dir)
            s = random.randint(0,391)
            os.startfile(os.path.join(music_dir, songs[s])) 

        elif 'joke' in query:
            import pyjokes
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif "close" in query :
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")
       
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "hibernate" in query or "sleep" in query:
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

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'lock' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown /s')

        elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    #query = query.replace("Limbo","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

        elif "type" in query:
            query = query.replace("type","")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'play music' in query or 'play some music' in query or 'music' in query:
            webbrowser.open("music.youtube.com")         

        elif 'mail' in query:
            webbrowser.open("mail.google.com")

        elif 'earth' in query:
            webbrowser.open("earth.google.com")
            
        elif 'sky' in query:
            webbrowser.open("sky.google.com")

        elif 'bye' in query or 'stop listening' in query or 'dont listen' in query or 'tata' in query or 'soja' in query or 'Chal nikal' in query or 'chala ja' in query or 'ja' in query:
            break

        ans=Reply(query)
        speak(ans)