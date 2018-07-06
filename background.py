from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import webbrowser
import pyttsx3
import time
from GUI import GUI
from Vlad_up import UP

# Text To Speech

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)

# High priorty commands

WAKE_UP = ["on", "wake up"]
TERMINATE = ["shut down", "terminate", "quit"]
CANCEL = ["cancel", "back", "stand"]

def background():

    # root = Tk()
    # root.title('Vlad')
    # root.iconbitmap('mic.ico')

    # style = ttk.Style()
    # style.theme_use('winnative')

    # label_txt = StringVar()
    # label_txt.set('Vlad')
    # label1 = ttk.Label(root, textvariable = label_txt)
    # label1.grid(row=0, column=0)

    print("Hi I'm Vlad")
    # label_txt.set("Hi I'm Vlad")
    eng.say('Hi I am Vlad')
    eng.runAndWait()

    while True:

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout= None)

            try:

                order = r.recognize_google(audio).lower()


                print(order)
                # label_txt.set(r.recognize_google(audio))
                if order in WAKE_UP:
                    print("Up")
                    # label_txt.set("Up")
                    eng.say('I am Up')
                    eng.runAndWait()

                    UP()
                    
                    eng.say("Going to Stand by mode")
                    eng.runAndWait()
                    print("Stand by mode...")
                    # label_txt.set("Stand by mode...")


                elif order.startswith("search google for"):
                    query = order[17:]
                    webbrowser.open('http://google.com/search?q=' + query)
                    print("Searching Google for"+ query)
                    # label_txt.set("Up")
                    eng.say("Searching Google for"+ query)
                    eng.runAndWait()

                elif order in TERMINATE:
                    eng.say("Shutting down")
                    eng.runAndWait()
                    print("Shutting down...")
                    # label_txt.set("Shutting down...")
                    exit(0)

                elif order in CANCEL:
                    eng.say("Stand by mode")
                    eng.runAndWait()
                    print("Stand by mode...")
                    # label_txt.set("Stand by mode...")
                    pass

                elif ("terminal" in order) or ("criminal" in order) or ("permanent" in order) or ("birmingham" in order):
                    GUI()
                    print('Back to Vlad')
                    # label_txt.set('Back to Vlad')
                    eng.say("Back to Vlad")
                    eng.runAndWait()

            except sr.UnknownValueError:
                print("Listening to the magic words: 'Wake up ' or 'Shut down'")
                # label_txt.set("Listening to the magic words: 'Wake up ' or 'Shut down'")

            except sr.RequestError:
                eng.say("I'm sorry, I couldn't reach google")
                eng.runAndWait()
                print("I'm sorry, I couldn't reach google")
                # label_txt.set("I'm sorry, I couldn't reach google")
    # root.mainloop()
