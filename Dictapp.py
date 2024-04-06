import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
Dictapp={"commandprompt":"cmd", "paint":"paint","chrome":"chrome","vscode":"code","notepad":"notepad"}

def openappweb(query):
    speak("launching...")
    if ".com" in query or ".co.in" or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace("", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(Dictapp.keys())
        for app in query:
            os.system(f"start {Dictapp[app]}")

def closeappweb (query):
        speak("closing...")
        if "one tan" or "1 tab" in query:
            pyautogui.hotkey("ctrl","w")
            speak("tab is closed")
        elif "2 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("closing...")
        elif "3 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5) 
            pyautogui.hotkey("ctrl","w")
            sleep(0.5) 
            pyautogui.hotkey("ctrl","w")
            speak("closing...")
        elif "4 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("closing...")

        else :
            keys = list(Dictapp.keys())
            for app in keys:
                for app in query:
                    os.system(f"taskkill /f im {Dictapp[app]}.exe")
        
        
        
        
        