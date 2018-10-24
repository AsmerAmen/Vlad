from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer
from Vlad_up import UP


def GUI():
    # GUI

    root = Tk()
    root.title('Thursday')
    img= PhotoImage(file='microphone.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    # root.iconbitmap('/mnt/Asmer/Projects/Python/Vlad/mic.ico')

    style = ttk.Style()
    style.theme_use('classic')

    photo = PhotoImage(file="microphone.png").subsample(15, 15)

    label1 = ttk.Label(root, text='Query:')
    label1.grid(row=0, column=0)
    entry1 = ttk.Entry(root, width=40)
    entry1.grid(row=0, column=1, columnspan=4)

    # btn2 = StringVar()



    def Mic():

        r = sr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 400

        with sr.Microphone(device_index=1) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5)
            try:
                message = str(r.recognize_google(audio,
                                                 # key=google_api_key
                                                 )
                              )

                
                
                mixer.music.load('chime2.mp3')
                mixer.music.play()

                if message in ["off", "terminal off",  "terminal of"]:
                    root.destroy()
                    return
                entry1.focus()
                entry1.delete(0, END)
                entry1.insert(0, message)
                
                UP(message)

            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')

            except sr.RequestError as e:
                print('Could not request results from Google Speech Recognition Service')

            else:
                pass




    def callback():

        UP(entry1.get())


    def get(event):

        UP(entry1.get())


    def buttonClick():

        mixer.init()
        mixer.music.load('chime1.mp3')
        mixer.music.play()

        if Mic() == 'off':
            print('off')
            return




    entry1.bind('<Return>', get)

    MyButton1 = ttk.Button(root, text='Process', width=10, command=callback)
    MyButton1.grid(row=0, column=6)

    # MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
    # MyButton2.grid(row=1, column=1, sticky=W)

    # MyButton5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)
    # MyButton5.grid(row=1, column=2, )

    # MyButton6 = ttk.Radiobutton(root, text='anghami', value='anghami', variable=btn2)
    # MyButton6.grid(row=1, column=3, sticky=E)

    MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove',
                       relief='sunken')
    MyButton6.grid(row=0, column=5)

    entry1.focus()
    root.wm_attributes('-topmost', 1)
    # btn2.set('google')
    root.mainloop()