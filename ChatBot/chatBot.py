import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
# import contypes.client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

