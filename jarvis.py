import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak("Good Morning sir!")
    elif 12 <= hour <= 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good night sir!")
    speak("It's")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("It's" +" " + strTime)
    speak(strTime)
    speak("Hi I am mili. How can i help you sir")
    '''search="temperature is sylhet"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data= BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_="BNeawe").text
    print(f"The current {search} is {temp}")
    speak(f"The current {search} is {temp}")
    speak("I'm mele. How can i help you siam?")'''



def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.

        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say any thing...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     sender_email = open("", "r").read()
#     sender_pass = open("", "r").read()
#     server.login(sender_email, sender_pass )
#     server.sendmail(sender_email, to, content)
#     server.close()



if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")

        elif 'open classroom' in query:
            webbrowser.open("classroom.google.com")
            speak("Opening Google classroom")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("gmail.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow")

        elif 'what is your name' in query:
            speak("My name is mele")
        elif 'hey mili' in query:
            speak("Hi Sir. How can I help you?")

        elif 'who are you' in query:
            speak("I'm the personal assistant of my sir .")

        elif 'who gave your name' in query:
            speak("This name is given to my sir.")

        elif 'who is your boss' in query:
            speak("His name is sir. He is a university student. He study in Bsc in cse from Metropolitan University. He live in sylhet, Bangladesh.")

        elif 'who am i' in query:
            speak("Your nane is sir. You are a university student. You study in Bsc in cse from Metropolitan University. You live in sylhet, Bangladesh.")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\WALTON\\Music\\VideoProc'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Opening play music")

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")


        elif 'open vs code' in query:
            speak("Opening vs code")
            codePath = "C:\\Users\\WALTON\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            speak("Opening pycharm")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(codePath)


        # elif 'send email' in query:
        #     speak("Opening email.")
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "hasubul.syl@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Siam. I am not able to send this email")

        elif'play' in query:
            song = query.replace("play", "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'temperature' in query:
            search="temperature is sylhet"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data= BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            print(f"Current {search} is {temp}")

        elif 'stop mili' in query:
            speak("Good by sir! See you again and love you sir.")
            exit()



