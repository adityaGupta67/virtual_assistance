import pywhatkit
import speech_recognition as sr
import datetime
import pyttsx3
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
import pyautogui


engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source,0,4)
    try:
        print("understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query} \n")
    except Exception as e:
        print("say that again")
        return "None"
    return query
strTime=int(datetime.now().strftime("%H"))

update= int((datetime.now()+timedelta(minutes=2)).strftime("%M"))
def sendMessage():
    speak("Who you want to send message")
    a= int(input('''Adarsh Deshmuk Ltce'''))
    if a == 1:
        speak("Whats the message")
        message = str(input("Enteer the message- "))
        pywhatkit.sendwhatmsg("+91 97306 92185",message,time_hour=strTime,time_min=update)
        pyautogui.press("enter")
    elif a==2:
        pass


