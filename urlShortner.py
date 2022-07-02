#url shortner package : pip install pyshorteners
import pyshorteners

url = input("Enter url : ")

print("URL after shortning : ", pyshorteners.Shortener().tinyurl.short(url))