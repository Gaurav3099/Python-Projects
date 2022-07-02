
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

e=pyttsx3.init()

date = int(datetime.datetime.now().day)
Time=datetime.datetime.now().strftime("%I:%M:%S")


def sendemail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.echo()
	server.starttls()
	server.login('gaurav.sarkar830@gmail.com', 'Password')
	server.sendmail('gaurav.sarkar830@gmail.com', to, content)
	server.close()

def speak(audio):
	e.say(audio)
	e.runAndWait()

def time():
	Time=datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)


def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	speak(date)
	speak(month)
	speak(year)

def wishme():
	speak("Welcome")
	
	hour = datetime.datetime.now().hour
	if hour >= 6 and hour <12:
		speak("Good morning")
	elif hour>=12 and hour <18:
		speak("Good afternoon")
	elif hour>=18 and hour <24:
		speak("good evening")
	else:
		speak("good night")
	speak("Jarvis at your service, how can i help you")

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listning...")
		r.pause_threshold = 1
		audio = r.listen(source)

		try:
			print("Recognizing...")
			query = r.recognize_google(audio, language='en-in')
			print(query)
		except Exception as e:
			print(e)
			return "None"
			speak("Say that again please")

		return query 

def screenshot():
	img = pyautogui.screenshot()
	img.save("D:/Exp/Projects/AI")

def cpu():
	usage = str(psutil.cpu_percent())
	speak("CPU is at"+usage)
	battery = psutil.sensors_battery()
	speak("Battery is at")
	speak(battery.percent)

def jokes():
	speak(pyjokes.get_joke())

if __name__=="__main__":
	wishme()
	while True:
		query = takeCommand().lower()

		if "time" in query:
			time()
		elif "date" in query:
			date()
		elif "wikipedia" in query:
			speak("searching...")
			query = query.replace("wikipedia","")
			result = wikipedia.summary(query, sentences=2)
			print(result)
			speak(result)

		elif "send email" in query:
			try:
				speak("What shoud I say?")
				#print("What shoud I say?")
				content = takeCommand()
				content = input()
				to = "gaurav.sarkar830@gmail.com"
				sendemail(to, content)
				speak("Email has been sent")
				
			except Exception as e:
				print(e)
				speak("Unable to send the email")

		elif 'search in chrome' in query:
			speak("What should i search?")
			chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
			search = takeCommand().lower()
			wb.get(chromepath).open_new_tab(search+'.com')

		#Logout shutdown restart
		elif 'logout' in query:
			os.system("shutdown -l")
		elif 'shutdown' in query:
			os.system("shutdown /s /t 1")
		elif 'restart' in query:
			os.system("shutdown /r /t 1")

		#Play songs
		elif 'play songs' in query:
			songs_dir = 'D:/Pics/Songs'
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[8]))

		#Remember Function
		elif 'remember that' in query:
			speak("what should I remember?")
			data = takeCommand()
			speak("you said me to remember "+data)
			remember = open("data.txt", "w")
			remember.write(data)
			remember.close()

		#Screenshot
		elif 'screenshot' in query:
			screenshot()
			speak("Done")

		#Battery & CPU
		elif 'cpu' in query:
			cpu()

		#Jokes Function
		elif 'jokes' in query:
			jokes()


		elif "offline" in query:
			quit()

#weather
#news