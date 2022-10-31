import os
import speech_recognition as sr

def takeCommand():
    command =sr.Recognizer()
    with sr.Microphone() as source:
        print("***Listing***")
        command.pause_threshold = 1
        audio=command.listen(source)

        try:
            print("-> Recongnizing....")
            query = command.recognize_google(audio, language= 'en-in')
            print(f"You Said :{query}")
        except:
            return "none"

        return query.lower()

while True:
    wake_up= takeCommand()

    if 'wake up jarvis' in wake_up:
        os.startfile("D:\\Personal Data\\Jarvis\\jarvis.py")

    else:
        print("Nothing.....")