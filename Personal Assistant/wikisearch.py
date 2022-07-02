import wikipedia
import speech_recognition as sr
import pyttsx3
import datetime

e=pyttsx3.init()

date = int(datetime.datetime.now().day)
Time=datetime.datetime.now().strftime("%I:%M:%S")

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
		elif "offline" in query:
			quit()