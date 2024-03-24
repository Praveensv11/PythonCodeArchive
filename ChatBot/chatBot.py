import 







































import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(audio):
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour<18:
        speak("Good Afternood!")
    else:
        speak("Good Evening")

    speak("Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio, language='en-in')
        print(f"User said {query}\n")
    
    except Exception as e:
        print('Say that again please...')
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    Query = takeCommand().lower()
    while True:
        if "wikipedia" in Query:
            speak('Searching Wikipedia...')
            Query = Query.replace('wikipedia', '')
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in Query:
            webbrowser.open("google.com")

        elif 'open youtube' in Query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in Query:
            webbrowser.open('stackoverflow.com')