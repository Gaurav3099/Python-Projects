import pyttsx3
engine=pyttsx3.init()
#engine.say("Hello I am Jarvis")
#engine.runAndWait()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

speak("This is Jarvis")