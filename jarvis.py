import datetime
import webbrowser

import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

""" Wish you according to the time """

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=1 and hour<12):
        speak("Good Morning Sir!")

    elif(hour>=12 and hour<18):
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I'm your jarvis . How may I help you !")

"""Take the command from the user and return it as string """

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing .... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}/n")

    except Exception as e:
        print("Please say that again ... ")
        return "None"
    return query
def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail","yourmail password")
    server.sendmail("your mail",to,content)
    server.close()

if __name__ == '__main__':
    wishme()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentence=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackflow' in query:
            webbrowser.open("stackflow.com")

        elif 'play song' in query:
            music_dir='G:\\2022 Songs'
            songs=os.listdir(music_dir)
            print(songs)
            randomno=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[randomno]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,the time is {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\sahil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send mail' in query:
            try:
                speak("What should I send ?")
                content=takeCommand()
                to="sahilbeny24@gmail.com"
                sendEmail(to,content)
                speak("Email sent scuccessfully.")
            except Exception as e:
                speak("Sorry my friend I was unable to send mail.")

        else:
            print("Sorry I can't Help with that.")

        if "quit" in query or "stop" in query or "exit" in query:
            speak("Thanks for using Jarvis . See you again")
            print("MADE BY --- SAHIL BENIWAL ")
            print(".....Thanks a lot .....")
            exit()
