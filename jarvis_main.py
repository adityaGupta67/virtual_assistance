import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui
import os

for i in range(3):
       a= input("Enter passwd to open :-")
       pw_file= open("password.txt","r")
       pw = pw_file.read()
       pw_file.close() 
       if (a==pw):
              print("WELCOME ! SAY [wake up] TO LOAD ME UP")
              break
       elif(i==2 and a!=pw):
              exit()
       elif(a!=pw):
              print("Try Again")



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
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        if "wake up" in query:
            from GreetMe import wishMe
            wishMe()
        while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                        speak("ok sir,you can call anytime")
                        break

                elif "hello" in query:
                            speak("Hello sir ,How are you")
                elif "i am fine" in query:
                            speak("Thats great")
                elif "how r u" in query:
                            speak("Perfect sir")
                elif "thanks" in query:
                            speak("Your welcome , sir")
                elif "pause" in query:
                       pyautogui.press("k")
                       speak("Video is paused")
                elif "play" in query:
                       pyautogui.press("k")
                       speak("Video is played")
                elif "mute" in query:
                       pyautogui.press("m")
                       speak("Video is Muted")
                elif "volume up" in query:
                       from keyboard import volumeup
                       volumeup()
                       speak("volume is turned up")
                elif "volume down" in query:
                       from keyboard import volumedown
                       speak("volume is turned down")
                       volumedown()
                elif "calculate" in query:
                       from calculateNum import wolfRamAlpha 
                       from calculateNum import calculate
                       query = query.replace("calculate","")
                       query = query.replace("jarvis","")
                       calculate(query)
                elif "whatsapp" in query:
                       from whatsapp import sendMessage
                       sendMessage()      
                
                elif "open" in query:
                       query = query.replace("open","")
                       query = query.replace("jarvis","")
                       pyautogui.press("super")
                       pyautogui.typewrite(query) 
                       pyautogui.press("enter")      

                       
                elif "open" in query:
                       from Dictapp import openappweb
                       openappweb(query)
                elif "close" in query:
                       from Dictapp import closeappweb
                       closeappweb(query)
                                
                elif "google" in query:
                       from searchnow  import searchGoogle
                       searchGoogle(query)
                elif "youtube" in query:
                       from searchnow import searchYoutube
                       searchYoutube(query) 
                       
                elif "wikipedia" in query:
                       from searchnow import searchWikipedia
                       searchWikipedia(query)             
            
                elif "time" in query:
                       strTime =datetime.datetime.now().strftime("%H:%S")
                       speak(f"time is {strTime}")

                elif "finally sleep" in query:
                       speak(f"going to sleep")
                       exit()

                elif "sreenshot" in query:
                       import pyautogui
                       im = pyautogui.screenshot()
                       im.save("ss.jpg")
                       
                elif "click my photo" in query:
                       pyautogui.press("super")
                       pyautogui.typewrite("Camera")
                       pyautogui.press("Enter")
                       pyautogui.sleep(2)
                       speak("smile")
                       pyautogui.press("Enter")

                elif "shutdown system" in query:
                       speak("Are you really want to shutdown your system")
                       shutdown = input("Are you really want to shut down (y/n)") 
                       if shutdown == "yes":
                              os.system("shutdown /s /t 1")
                       elif shutdown == "no":
                              break
                elif "open" in query:
                       query = query.replace("open","")
                       query = query.replace("jarvis","")
                       pyautogui.press("super")
                       pyautogui.typewrite(query) 
                       pyautogui.press("enter")      