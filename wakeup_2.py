import speech_recognition as sr
import webbrowser
import pyttsx3
import time

import os, subprocess

# Text To Speech

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[2].id)


CANCEL = ["cancel", "back", "stand"]
TERMINATE = ["shut down", "terminate", "quit"]

r2 = sr.Recognizer()

def UP():
    while True:
        
        with sr.Microphone() as source2:
            r2.adjust_for_ambient_noise(source2)
            audio2 = r2.listen(source2, timeout= None)

        try:
            cmd = r2.recognize_google(audio2)

            print(cmd)
            eng.say(cmd)
            eng.runAndWait()

            cmd = cmd.lower()

            if cmd in CANCEL:
                    break

            elif cmd in TERMINATE:
                eng.say("Shutting down")
                eng.runAndWait()
                print("Shutting down...")
                exit(0)        

            elif cmd is "play music":
                webbrowser.open('https://play.anghami.com/mymusic/')

            elif cmd.startswith("play") and cmd.endswith("anghami"):
                webbrowser.open('https://play.anghami.com/search/'+ cmd[5:-10])

            elif cmd.startswith("open"):
                
                # if cmd.endswith("online"):
                if ('mail'in cmd) or ('e-mail'in cmd) or ('gmail'in cmd):
                    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
                elif 'google keep' in cmd:
                    webbrowser.open('https://keep.google.com/keep')
                elif 'google drive' in cmd:
                    webbrowser.open('https://drive.google.com/drive')
                else:
                    webbrowser.open('https://www.%s.com/' % cmd[5:])

            elif cmd.startswith("start"):
                if 'media player' in cmd:
                    os.system("start wmplayer")
                elif 'chrome' in cmd:
                     os.system("start chrome")
                elif 'firefox' in cmd:
                     os.system("start firefox")
                elif 'command'in cmd:
                    os.system("start cmd")

            elif cmd.startswith("go to"):
                if 'projects' in cmd:
                    os.chdir("D:/Projects")
                    os.system("start cmd")
                    os.system("start .")

                elif 'Google' in cmd:
                    os.chdir("D:/way to google")
                    os.system("start cmd")
                    os.system("start .")

                elif 'series' in cmd:
                    os.chdir("E:/Series")
                    os.system("start cmd")
                    os.system("start .")

                elif 'music' in cmd:
                    os.chdir("E:/Music")
                    os.system("start cmd")
                    os.system("start .")

                elif 'movies' in cmd:
                    os.chdir("E:/Movies")
                    os.system("start cmd")
                    os.system("start .")

            else:
                pass

        except sr.UnknownValueError:
            eng.say("I'm sorry, I couldn't understand you")
            eng.runAndWait()
            print("I'm sorry, I couldn't understand you")

        except sr.RequestError:
            eng.say("I'm sorry, I couldn't reach google")
            eng.runAndWait()
            print("I'm sorry, I couldn't reach google")

    

