import speech_recognition as sr
import webbrowser
import pyttsx3
import time


# Text To Speech

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[2].id)

# High priorty commands

WAKE_UP = ["on", "wake up"]
TERMINATE = ['shut down', 'terminate', 'quit']
CANCEL = ['cancel', 'back']


while True:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout= None)

        try:
            if r.recognize_google(audio) in WAKE_UP:
                print("Up")
                eng.say('Up')
                eng.runAndWait()

                r2 = sr.Recognizer()

                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2)
                    audio2 = r2.listen(source2)

                try:
                    cmd = r2.recognize_google(audio2)

                    print(cmd)
                    eng.say(cmd)
                    eng.runAndWait()

                    if cmd is 'play music':
                        webbrowser.open('https://play.anghami.com/mymusic/')

                    elif cmd.endswith('anghami'):
                        webbrowser.open('https://play.anghami.com/search/'+ cmd[5:-10])

                    elif cmd.startswith('open'):
                        webbrowser.open('https://www.%s.com/' % cmd[5:])

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


            elif r.recognize_google(audio) in TERMINATE:
                eng.say("Shutting down")
                eng.runAndWait()
                print("Shutting down...")
                break

            elif r.recognize_google(audio) in CANCEL:
                eng.say("Stand by mode")
                eng.runAndWait()
                print("Stand by mode...")
                pass

        except sr.UnknownValueError:
            print("Listening to the magic words: 'Wake up ' or 'Shut down'")

        except sr.RequestError:
            eng.say("I'm sorry, I couldn't reach google")
            eng.runAndWait()
            print("I'm sorry, I couldn't reach google")