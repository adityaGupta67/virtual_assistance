import wolframalpha
import pyttsx3
import speech_recognition

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wolfRamAlpha(query):

    apikey = "7UEXPY-TE6GH7XPYQ"
    requester = wolfRamAlpha.Client(apikey)
    requested = requester.query(query)
    try:
        answer = next(requested.result).txt
        return answer
    except:
        speak("The valuse is not answerable")

def calculate(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divide","/")
    Term = Term.replace("plus","+")
    Term = Term.replace("subtract","-")

    final=str(Term)
    try:

        result= wolframalpha(final)
        print(f"{result}")
        speak(result)
    except:
        speak("value is not ansrable")