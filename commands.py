# #Thursday open Facebook					online
# #Thursday go to Projects					offline
# #Thursday start media player 				offline
# #Thursday Search Google for whatever		online
# #Thursday play The weeknd on anghami		online

import webbrowser
import pyttsx3

import os, subprocess

def search_google(query):
    webbrowser.open('http://google.com/search?q=' + query)
    print("Searching Google for" + query)
    eng.say("Searching Google for" + query)
    eng.runAndWait()

def open_on_browser(website):
	if ('mail'in website) or ('e-mail'in website) or ('gmail'in website):
		webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
	elif 'google keep' in website:
		webbrowser.open('https://keep.google.com/keep')
	elif 'google drive' in website:
		webbrowser.open('https://drive.google.com/drive')
	elif 'massenger' in website:
		webbrowser.open('https://www.facebook.com/messages')
	else:
		webbrowser.open('https://www.%s.com/' % website)

def start_app(app):
	if 'media player' in app:
		os.system("start wmplayer")
	elif 'command'in app:
		os.system("start cmd")
	else:
		os.system("start "+ app)

def goto_dir(directory):
	if 'projects' in directory:
		os.chdir("D:/Projects")
		os.system("start cmd")
		os.system("start .")

	elif 'Google' in directory:
		os.chdir("D:/way to google")
		os.system("start cmd")
		os.system("start .")
	elif 'series' in directory:
		os.chdir("E:/Series")
		os.system("start cmd")
		os.system("start .")
	elif 'music' in directory:
		os.chdir("E:/Music")
		os.system("start cmd")
		os.system("start .")

	elif 'movies' in directory:
		os.chdir("E:/Movies")
		os.system("start cmd")
		os.system("start .")
    

def play_music(music):
	webbrowser.open('https://play.anghami.com/search/'+ music)

def terminate(eng):
	eng.say("Shutting down")
	eng.runAndWait()
	print("Shutting down...")
	exit(0)



# string = 'Thursday play The weeknd on anghami'
# string = string.replace('Thursday ', '').replace('on anghami', '')
# print(string)
