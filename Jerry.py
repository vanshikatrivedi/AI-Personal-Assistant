import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

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
