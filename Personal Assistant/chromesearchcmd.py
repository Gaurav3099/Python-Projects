import webbrowser as wb
import pyttsx3
import datetime
import os
import pyautogui 
import psutil
import pyjokes

e=pyttsx3.init()

date = int(datetime.datetime.now().day)
Time=datetime.datetime.now().strftime("%I:%M:%S")

def speak(audio):
	e.say(audio)
	e.runAndWait()

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
	print("how can i help you")

def screenshot():
	Timess=datetime.datetime.now().strftime("%I_%M_%S")
	name = str(Timess)+".png"
	img = pyautogui.screenshot()
	path= "D:/Exp/Projects/AI/Screenshots/"+name
	img.save(path)

def cpu():
	usage = str(psutil.cpu_percent())
	speak("CPU is at"+usage)
	print(usage)
	battery = psutil.sensors_battery()
	speak("Battery is at")
	speak(battery.percent)
	print(battery.percent)

def jokes():
	speak(pyjokes.get_joke())

if __name__=="__main__":
	wishme()
	#speak("welcome")
	while True:
		query = input()
		if 'search in chrome' in query:
			speak("what should I search?")

			print("What should i search?")

			chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
			#search = takeCommand().lower()
			search = input()

			wb.get(chromepath).open_new_tab(search)

		#Play songs
		elif 'play songs' in query:
			songs_dir = 'D:/Pics/Songs'
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[8]))

		#Remember Function
		elif 'remember that' in query:
			speak("what should I remember?")
			data = input()
			speak("you said me to remember "+data)
			remember = open("data.txt", "w")
			remember.write(data)
			remember.close()

		elif 'do you know anything' in query:
			remember = open('data.txt', 'r')
			speak("you said me to remember that"+remember.read())

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