import random
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)

"""VOICE"""
# engine.setProperty('voices', voices[1].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=10)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")

    except Exception as e:
        speak("Please repeat ")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12 :
        speak("Hey! Good Morning!")
    elif hour>=12 and hour<=17:
        speak("Hey! Good Afternoon!")
    else:
        speak("Hey! Good Evening!")
    speak("I am Jerry, Vanshika's AI personal assistant")
    speak("Please tell me how can I help you?")


if __name__ == "__main__":
    wish()
    # while True:
    if 1:

        query = takecommand().lower()

        #logic_building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath="C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "G:\\Fashionshow"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("According to Wikipedia,")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("What should I search on Google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send a message" in query:
            kit.sendwhatmsg("+918797471121", "this is testing protocol",00,9)

        elif "play a song on youtube" in query:
            kit.playonyt("perfect")

        elif "email"
