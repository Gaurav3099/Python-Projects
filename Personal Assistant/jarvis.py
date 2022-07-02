from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import smtplib
import wikipedia
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

display="welcome"

root =Tk()
root.title("JARVIS AI ")
root.geometry("300x300+300+300")
e=pyttsx3.init()


#def write(display):
scrollbar = Scrollbar(root) 
scrollbar.pack( side = RIGHT, fill = Y ) 
mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
mylist.insert(END, 'Hello') 
mylist.pack( side = LEFT, fill = BOTH) 
scrollbar.config( command = mylist.yview )



def speak(audio):
	e.say(audio)
	e.runAndWait()

def time():
	Time=datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)
	mylist.insert(END, Time )
def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	mylist.insert(END, str(date) +"-"+ str(month) +"-"+str(year))
	speak(date)
	speak(month)
	speak(year)

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		#print("Listning...")
		mylist.insert(END, "Listning...")
		r.pause_threshold = 1
		audio = r.listen(source)

		try:
			#print("Recognizing...")
			mylist.insert(END, "Recognizing...")
			query = r.recognize_google(audio, language='en-in')
			#print(query)
			mylist.insert(END, query)
		except Exception as e:
			print(e)
			return "None"
			speak("Say that again please")
			mylist.insert(END, "Say that again please")

		return query 

def wishme():
	
	speak("Welcome")
	mylist.insert(END, "Welcome" )
	speak("Current time is")
	time()

	speak("Todays date is")
	date()
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour <12:
		speak("Good morning")
		mylist.insert(END, "good morning" )
	elif hour>=12 and hour <18:
		speak("Good afternoon")
		mylist.insert(END, "good afternoon" )
	elif hour>=18 and hour <24:
		speak("good evening")
		
		mylist.insert(END, "good evening" )
	else:
		speak("good night")
		mylist.insert(END, "good night" )
	speak("Jarvis at your service, how can i help you")
	mylist.insert(END, "Jarvis at your service, how can i help you")
	takeCommand()

btnSubmit=Button(root,text="Submit",command=wishme)
btnSubmit.pack()
root.mainloop()


