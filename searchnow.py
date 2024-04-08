import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import pyautogui
from time import sleep
import os
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

query = takeCommand().lower()
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
searchnow={"searchGoogle=searchGoogle","youtube=youtube"}


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query=" +query    
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia..")
        query = query.replace("wikipedia","")  
        query = query.replace("search wikipedia","") 
        query = query.replace("jarvis","")  
        results = wikipedia.summary(query, sentences = 1)
        speak("According to wikipedia..")
        print(results)
        speak(results)
        
def closeappweb (query):
        speak("closing...")
        if "one tan" or "1 tab" in query:
            pyautogui.hotkey("ctrl","w")
            speak("tab is closed")
        elif "2 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)

        else :
            keys = list(searchnow.keys())
            for app in keys:
                for app in query:
                    os.system(f"taskkill /f im {searchnow[app]}.exe")