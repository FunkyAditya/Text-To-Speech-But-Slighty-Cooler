# This audio book prototype is made by Aditya Prakash

# This is a prototype of project and none of the following module is made by me

import pyttsx3
import pytesseract as tess
from PIL import Image
from cgitb import text
import speech_recognition as sr

r = sr.Recognizer() 

with sr.Microphone() as source:
    print("Say : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text + ".png"
    except: 
        print("say it again")

img = Image.open(text)
text = tess.image_to_string(img)

engine = pyttsx3.init()

rate = engine.getProperty("rate")
engine.setProperty("rate", 120)

engine.say(text)
engine.runAndWait()
