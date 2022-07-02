import webbrowser as wb 

def webauto():
	chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
	urls = (
		
		"https://www.udemy.com/",
		"https://github.com/Gaurav3099/Python-Projects"
		)
	for url in urls:
		print("opening :"+ url)
		wb.get(chrome_path).open(url)

webauto()