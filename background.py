from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import webbrowser
import pyttsx3
import time
from GUI import GUI
from Vlad_up import UP
from commands import terminate

# Text To Speech

eng = pyttsx3.init('espeak')
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)

# High priorty commands

# WAKE_UP = ["on", "wake up"]
TERMINATE = ["shut down", "terminate", "quit"]

def background():

    print("Hi I'm Thursday")
    eng.say('Hi I am Thursday')
    eng.runAndWait()

    while True:

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout= None)

            try:

                order = r.recognize_google(audio).lower()


                print(order)
                
                if order.startswith("thursday"):
                    # print("Up")
                   
                    # eng.say('I am Up')
                    # eng.runAndWait()

                    UP(order.replace('thursday ', ''))
                    
                    eng.say("Going to Stand by mode")
                    eng.runAndWait()
                    print("Stand by mode...")


                elif order in TERMINATE:
                    terminate()

                
                elif ("terminal" in order) or ("criminal" in order) or ("permanent" in order) or ("birmingham" in order):
                    GUI()
                    print('Back to Thursday')
                    eng.say("Back to Thursday")
                    eng.runAndWait()

                elif ("your name" in order) and (order.startswith("what") or order.startswith("what's")):
                    eng.say("My Name is Thursday.")
                    eng.runAndWait()
                    print("My Name is Thursday.")
     
                elif ("your name" in order) and (order.startswith("why")):
                    eng.say("Because Tony Stark has already used 'Friday'. and The Weeknd's music rocks.")
                    eng.runAndWait()
                    print("Beacuse Tony Stark already has used 'Friday' and The Weeknd's music rocks.")
    


            except sr.UnknownValueError:
                print("Listening to the magic words: 'Wake up ' or 'Shut down'")

            except sr.RequestError:
                eng.say("I'm sorry, I couldn't reach google")
                eng.runAndWait()
                print("I'm sorry, I couldn't reach google")

