from textblob import TextBlob
import emoji

y = input("Enter your sentence: ")
edu = TextBlob(y)

x = edu.sentiment.polarity
if x<0:
	print("Negative sentence ", emoji.emojize(":disappointed_face: "))
elif x==0:
	print("Neutral sentence ", emoji.emojize(":zipper-mouth_face: "))
elif x>0 and x<=1:
	print("Positive sentence ", emoji.emojize(":grinning_face_with_big_eyes: "))