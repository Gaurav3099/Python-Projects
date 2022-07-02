import datetime
import pyttsx3

e=pyttsx3.init()

def speak(audio):
	e.say(audio)
	e.runAndWait()

def time():
	Time=datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)

time()

def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	speak(date)
	speak(month)
	speak(year)

date()