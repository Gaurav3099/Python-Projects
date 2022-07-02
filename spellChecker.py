from textblob import TextBlob 

#a = "Coding is gret"
a = input("Enter your text: ")
print("original text: " +str(a))

b = TextBlob(a)
print("Corrected text: "+str(b.correct()))