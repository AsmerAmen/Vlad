import speech_recognition as sr
import webbrowser
import pyttsx3
import time

from commands import *

import os, subprocess

# Text To Speech

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[5].id)


CANCEL = ["cancel", "back", "stand by"]
TERMINATE = ["shut down", "terminate", "quit"]

r2 = sr.Recognizer()

def UP(cmd):
    # while True:
        
        # with sr.Microphone() as source2:
        #     r2.adjust_for_ambient_noise(source2)
        #     audio2 = r2.listen(source2, timeout= None)

        # try:
        #     cmd = r2.recognize_google(audio2)

    print("I Think you said " + cmd)
    eng.say("I Think you said " + cmd)
    eng.runAndWait()

    # cmd = cmd.lower()

    if cmd in CANCEL:
        return

    elif cmd in TERMINATE:
        terminate(eng)
        
    elif cmd.startswith("search google for"):
        query = cmd[17:]
        search_google(query)

    elif cmd.startswith("play"):
        query = cmd.replace('play ', '').replace(' on anghami', '')
        play_music(query)

    elif cmd.startswith("open"):
        website = cmd.replace('open ', '')
        open_on_browser(website)
        
    elif cmd.startswith("start"):
        app = cmd.replace('start ', '')
        start_app(app)

    elif cmd.startswith("go to"):
        directory = cmd.replace('go to ', '')
        goto_dir(directory)

    elif ("greatest singer" in cmd) or ("best singer" in cmd):
        eng.say("Abel The Weenknd Teesfye, fo sure.")
        eng.runAndWait()
        print("Abel The Weenknd Teesfye, fo sure.")
    
   
    else:
        pass

        # except sr.UnknownValueError:
        #     eng.say("I'm sorry, I couldn't understand you")
        #     eng.runAndWait()
        #     print("I'm sorry, I couldn't understand you")

        # except sr.RequestError:
        #     eng.say("I'm sorry, I couldn't reach google")
        #     eng.runAndWait()
        #     print("I'm sorry, I couldn't reach google")