# from distutils.core import setup
# import py2exe

# setup(console=['cVlad.py'])

from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\win8\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\win8\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

include_files = ['microphone.png',
			'mic.ico',
			'chime1.mp3',
			'chime2.mp3',
 			os.path.join("C:\\Users\\win8\\AppData\\Local\\Programs\\Python\\Python36-32", 'DLLs', 'tk86t.dll'),
            os.path.join("C:\\Users\\win8\\AppData\\Local\\Programs\\Python\\Python36-32", 'DLLs', 'tcl86t.dll'),
            ]


excludes = ['']
packages = ["pygame", "speech_recognition", "webbrowser","tkinter", "pyttsx3"]

setup(name = 'Vlad',
	version = '1.1',
	description = 'VA',
	options = {
	"build_exe": {
	    'packages': packages,
	    'include_files': include_files,
	    'excludes': excludes,
	    'optimize' : 2,
	    'include_msvcr': True,
		}
	},
	executables = [Executable(script="main.py",
							  targetName='Vlad.exe',
							  icon='mic.ico'),

				   ]

	)