import pyttsx3
import speech_recognition as sr
import webbrowser
from googletrans import Translator
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
from pydictionary import Dictionary as Diction
import datetime
from playsound import playsound
import psutil
import requests
from bs4 import BeautifulSoup
import PyPDF2
from gtts import gTTS
from pywikihow import search_wikihow

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
Assistant.setProperty('rate', 150)

def Speak(audio):
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def takeCommand():
    command =sr.Recognizer()
    with sr.Microphone() as source:
        print("***Listing***")
        command.pause_threshold = 1
        audio=command.listen(source, 0, 4)

        try:
            print("-> Recongnizing....")
            query = command.recognize_google(audio, language= 'en-in')
            print(f"You Said :{query}")
        except:
            return "none"

        return query.lower()

def taskExecution():

    Speak("Hello Sir, I am Insane")
    Speak("How May I Help You?")

    def Music():
        Speak("Tell me the name of the song which you want to listen.")

        musicName= takeCommand()

        if 'chitthi' in musicName:
            os.startfile("D:\\Personal Data\\Music\\Chitthi_QK,UKRapiBoy_Hustle2.0.mp3")
        
        elif 'ye aaj ka din' in musicName:
            os.startfile("D:\\Personal Data\\Music\\Ye_Aaj_Ka_Din_Kings_Clan_Hustle 2.0.mp3")

        else:
            pywhatkit.playonyt(musicName)
        
        Speak("Your song has been played sir, Enjoy!!")

    def WhatsApp():
        Speak("Tell me the name of the person!")
        name= takeCommand()

        if'mayank' in name:
            Speak("Ok Sir, Tell me the message!")
            msg= takeCommand()
            Speak("Tell me the time sir!")
            Speak("Time in Hour!")
            hour= int(takeCommand())
            Speak("Time in minute!")
            min= int(takeCommand())
            pywhatkit.sendwhatmsg("+919729812392", msg, hour, min, 20)
            Speak("Ok Sir, Sending whatsapp message!")
        
        else:
            Speak("Tell me the phone number.")
            phone= int(takeCommand())
            ph= '+91' + phone
            Speak("Ok Sir, Tell me the message!")
            msg= takeCommand()
            Speak("Tell me the time sir!")
            Speak("Time in Hour!")
            hour= int(takeCommand())
            Speak("Time in minute!")
            min= int(takeCommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
            Speak("Ok Sir, Sending whatsapp message!")

    def OpenApps():
        Speak("Ok Sir, wait a second!")

        if 'code' in query:
            os.startfile("C:\\Users\\Smart Joules\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif 'brave' in query:
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
        
        elif 'slack' in query:
            os.startfile("C:\\Users\\Smart Joules\\AppData\\Local\\slack\\slack.exe")
        
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        
        elif 'telegram' in query:
            webbrowser.open("https://web.telegram.org/")
        
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps")

        elif 'translator' in query:
            webbrowser.open("https://translate.google.co.in/")

        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'google' in query:
            webbrowser.open("https://www.google.com/")

        Speak("Work has been done sir.")

    def CloseApps():
        Speak("Ok Sir, Wait a second.")

        if 'code' in query:
            os.system("TASKKILL /f /im Code.exe")
        
        elif 'brave' in query:
            os.system("TASKKILL /f /im brave.exe")
        
        elif 'slack' in query:
            os.system("TASKKILL /f /im slack.exe")
        
        elif 'chrome' in query:
            os.system("TASKKILL /f /im chrome.exe")
        
        Speak("Work has been done sir.")

    def YouTubeAuto():
        Speak("What's Your Command?")
        comm= takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')
        
        elif 'restart' in comm:
            keyboard.press('0')
        
        elif 'mute' in comm:
            keyboard.press('m')
        
        elif 'forward' in comm:
            keyboard.press('l')
        
        elif 'rewind' in comm:
            keyboard.press('j')
        
        elif 'back' in comm:
            keyboard.press('j')
        
        elif 'full screen' in comm:
            keyboard.press('f')
        
        elif 'previous video' in comm:
            keyboard.press('p')
        
        elif 'next video' in comm:
            keyboard.press('n')
        
        elif 'decrease playback rate' in comm:
            keyboard.press('<')
        
        elif 'increase playback rate' in comm:
            keyboard.press('>')
        
        elif 'theater mode' in comm:
            keyboard.press('t')
        
        elif 'mini player' in comm:
            keyboard.press('i')
        
        elif 'close mini player' in comm:
            keyboard.press('escape')
        
        elif 'caption' in comm:
            keyboard.press('c')
        
        Speak ("Done Sir.")

    def ChromeAuto():
        Speak("What's Your Command?")
        comm = takeCommand()

        if 'close this tab' in comm:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in comm:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in comm:
            keyboard.press_and_release('ctrl + h')

        elif 'history' in comm:
            keyboard.press_and_release('ctrl + h')

        elif 'download tab' in comm:
            keyboard.press_and_release('ctrl + j')  

        Speak ("Done Sir.")

    def Dict():
        Speak ("Activated Dictionary.")
        Speak("Tell me the word!")
        word = takeCommand()

        if 'meaning' in word:
            word = word.replace ("What is the meaning of", "")
            word= word. replace ("insane", "")
            result = Diction.meanings(word)
            Speak(f"The meaning of {word} is {result}.")
        
        elif 'synonym' in word:
            word = word.replace ("What is the synonym of", "")
            word= word. replace ("insane", "")
            result = Diction.synonyms(word)
            Speak(f"The synonym of {word} is {result}.")
        
        elif 'antonym' in word:
            word = word.replace ("What is the antonym of", "")
            word= word. replace ("insane", "")
            result = Diction.antonyms(word)
            Speak(f"The antonym of {word} is {result}.")
        
        Speak("Exited Dictionary.")

    def screenshot():
        Speak("Ok Boss, What should I Name that file.")
        path= takeCommand()
        path1name= path + ".png"
        path1= "D:\\Personal Data\\" + path1name
        ss= pyautogui.screenshot()
        ss.save(path1)
        os.startfile("D:\\Personal Data")
        Speak("Here is your screenshot.")

    def TakeHindi():
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
    
    def Tran():
        Speak("Tell me the line Sir!")
        line= TakeHindi()
        t= Translator()
        result= t.translate(line)
        Text= result.text
        Speak(Text)

    def temp():
        Speak("Sure Sir, Please tell me the location.")
        search= takeCommand()
        url= f"https://www.google.com/search?q=temperature of{search}"
        r= requests.get(url)
        data= BeautifulSoup(r.text, "html.parser")
        temp= data.find("div", class_ ="BNeawe").text
        Speak(f"The Temperature is {temp}.")

    def reader():
        Speak("Tell me the name of the Book.")
    
        name= takeCommand()

        if 'soft skills' in name:
            os.startfile("D:\\Personal Data\\B.Tech\\SSIC\\Soft Skills & Interpersonal Communication.pdf")
            book = open("D:\\Personal Data\\B.Tech\\SSIC\\Soft Skills & Interpersonal Communication.pdf", "rb")
            pdfreader = PyPDF2.PdfFileReader(book)
            pages= pdfreader.getNumPages()
            Speak(f"Number of pages in this books are {pages}")
            Speak("From which page I have to start reading?")
            numPage= int(input("Enter the page number: "))
            page= pdfreader.getPage(numPage)
            text= page.extractText()
            Speak("In which language, I have to read?")
            lang= takeCommand()

            if 'hindi' in lang:
                transl= Translator()
                textHin= transl.translate(text, 'hi')
                textm= textHin.text
                speech= gTTS(text= textm)
                
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                
                except:
                    playsound('book.mp3')


            else:
                Speak(text)

        else:
            Speak("You Book is not found sir. Please try again.")

    def speedTest():
        import speedtest
        Speak("Checking Speed.....")
        speed = speedtest.Speedtest()
        downloading= speed.download()
        correctDownload= int(downloading/800000)
        upload= speed.upload()
        correctUpload= int(upload/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUpload} mbp s.")
        
        elif 'downloading' in query:
            Speak(f"The downloading speed is {correctDownload} mbp s.")
        
        else:
            Speak(f"The downloading speed is {correctDownload} mbp s and the uploading speed is {correctUpload} mbp s.")

    while True:

        query = takeCommand()

        if 'hello' in query:
            Speak("Hello Sir, I am Insane 2 point o.")
            Speak("How May I Help You?")
        
        elif 'how are you' in query:
            Speak("I am Fine Sir!")
            Speak("What about You?")

        elif 'i am also fine' in query:
            Speak("Great to hear that sir.")
        
        elif 'thank you' in query:
            Speak("It's my Pleasure Sir.")
        
        elif 'thanks' in query:
            Speak("It's my Pleasure Sir.")
        
        elif 'you need a break' in query:
            Speak("Ok Sir, You Can Call me Anytime")
            Speak("Just Say Wake Up Insane.")
            break

        elif 'youtube search' in query:
            Speak("Ok Sir, This is What I Found for you!")
            query= query.replace("insane", "")
            query= query.replace("youtube search for", "")
            web= "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            Speak("Please let me know if its fine!")

        elif 'google search' in query:
            Speak("Ok Sir, This is What I Found for you!")
            query= query.replace("insane", "")
            query= query.replace("google search for", "")
            pywhatkit.search(query)
            Speak("Please let me know if its fine!")

        elif 'website' in query:
            Speak("Ok Sir, Launching.....")
            query= query.replace("insane", "")
            query= query.replace("website", "")
            query= query.replace(" ", "")
            web1= query.replace("open", "")
            web2 = "http://www." + web1 + ".com"
            webbrowser.open(web2)
            Speak("The site has been launched sir!")
        
        elif 'launch' in query:
            Speak("Tell me the name of the website.")
            name = takeCommand()
            web = "http://www." + name + ".com"
            webbrowser.open(web)
            Speak("Done Sir!")
        
        elif 'music' in query:
            Music()
        
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query= query.replace("wikipedia", "")
            query= query.replace("insane", "")
            wiki= wikipedia.summary(query, 100)
            Speak(f"According to Wikipedia: {wiki}")
            
        elif 'whatsapp message' in query:
            WhatsApp()
        
        elif 'snapshot' in query:
            screenshot()
        
        elif 'open code' in query:
            OpenApps()
        
        elif 'open brave' in query:
            OpenApps()
        
        elif 'open slack' in query:
            OpenApps()
        
        elif 'open chrome' in query:
            OpenApps()
        
        elif 'open facebook' in query:
            OpenApps()
        
        elif 'open telegram' in query:
            OpenApps()
        
        elif 'open whatsapp' in query:
            OpenApps()
        
        elif 'open instagram' in query:
            OpenApps()
        
        elif 'open map' in query:
            OpenApps()
        
        elif 'open translator' in query:
            OpenApps()
        
        elif 'open youtube' in query:
            OpenApps()
        
        elif 'open google' in query:
            OpenApps()
        
        elif 'close code' in query:
            CloseApps()
        
        elif 'close brave' in query:
            CloseApps()
        
        elif 'close slack' in query:
            CloseApps()
        
        elif 'close chrome' in query:
            CloseApps()

        elif 'pause' in query:
            keyboard.press('space bar')
            Speak ("Noted Sir!")
        
        elif 'restart' in query:
            keyboard.press('0')
            Speak ("Noted Sir!")
        
        elif 'mute' in query:
            keyboard.press('m')
            Speak ("Noted Sir!")
        
        elif 'forward' in query:
            keyboard.press('l')
            Speak ("Noted Sir!")
        
        elif 'rewind' in query:
            keyboard.press('j')
            Speak ("Noted Sir!")
        
        elif 'back' in query:
            keyboard.press('j')
            Speak ("Noted Sir!")
        
        elif 'full screen' in query:
            keyboard.press('f')
            Speak ("Noted Sir!")
        
        elif 'previous video' in query:
            keyboard.press('p')
            Speak ("Noted Sir!")
        
        elif 'next video' in query:
            keyboard.press('n')
            Speak ("Noted Sir!")
        
        elif 'decrease playback rate' in query:
            keyboard.press('<')
            Speak ("Noted Sir!")
        
        elif 'increase playback rate' in query:
            keyboard.press('>')
            Speak ("Noted Sir!")
        
        elif 'theater mode' in query:
            keyboard.press('t')
            Speak ("Noted Sir!")
        
        elif 'mini player' in query:
            keyboard.press('i')
            Speak ("Noted Sir!")
        
        elif 'close mini player' in query:
            keyboard.press('escape')
            Speak ("Noted Sir!")
        
        elif 'caption' in query:
            keyboard.press('c')
            Speak ("Noted Sir!")
        
        elif 'youtube tools' in query:
            YouTubeAuto()
        
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            Speak ("Noted Sir!")

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + n')
            Speak ("Noted Sir!")

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            Speak ("Noted Sir!")

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            Speak ("Noted Sir!")

        elif 'download tab' in query:
            keyboard.press_and_release('ctrl + j')
            Speak ("Noted Sir!")  
        
        elif 'chrome automation' in query:
            ChromeAuto()
        
        elif 'joke' in query:
            joke= pyjokes.get_joke()
            Speak(joke)

        elif 'repeat my words' in query:
            Speak("Noted Sir.")
            word = takeCommand()
            Speak(f"You Said: {word}")
        
        elif 'my location' in query:
            Speak("Ok Sir, Wait a second.")
            webbrowser.open("https://www.google.com/maps/@29.971515,76.320995,14z/")

        elif 'dictionary' in query:
            Dict()
        
        elif 'alarm' in query:
            Speak("Enter the time!")
            time= input("--> Enter the time: ")

            while True:
                Time= datetime.datetime.now()
                now= Time.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to Wakeup Sir!")
                    playsound('Insane Wake Up Iron Man Edition.mp3')
                    Speak("Alarm Closed!")
                
                elif now>time:
                    break
        
        elif 'translator' in query:
            Tran()
            
        elif 'remember that' in query:
            msg= query.replace("remember that", "")
            msg= query.replace("insane", "")
            Speak(f"You tell me to remind that: {msg}")
            remember= open('data.txt', 'w')
            remember.write(msg)
            remember.close
        
        elif 'what do you remember' in query:
            remember= open('data.txt', 'r')
            Speak(f"You tell me that {remember.read()}")

        elif 'search on google' in query:
            import wikipedia as googleScrap
            query = query.replace("insane", " ")
            query = query.replace("search", " ")
            query = query.replace("on", " ")
            query = query.replace("google", " ")
            query = query.replace("about", " ")
            Speak("This is what I found of Web for you sir.")
            pywhatkit.search(query)

            try:
                result= googleScrap.summary(query, 2)
                Speak(result)
            
            except:
                Speak("No Speakable Data Available!")
        
        elif 'temperature' in query:
            temp()

        elif 'book reader' in query:
            reader()

        elif 'downloading speed' in query:
            speedTest()
        
        elif 'uploading speed' in query:
            speedTest()
        
        elif 'internet speed' in query:
            speedTest()
        
        elif 'how to' in query:
            Speak("Ok Sir, getting the data from internet.")
            op = query.replace("insane", "")
            max_result= 1
            how_to_func= search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

taskExecution()
