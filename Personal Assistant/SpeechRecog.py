import speech_recognition as sr
import pyttsx3

e=pyttsx3.init()

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

takeCommand()