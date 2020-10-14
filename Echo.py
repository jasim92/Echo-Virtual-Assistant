import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #selecting the output voice between male and female
# print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    '''
    this function greets you while it starts
    :return:
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Echo! Your Virtual Assistant. What can I do for you Sir")

def takecommand():
    '''
    this function take input from user and convert it to string output
    :return:
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception as e:
        print("Say that again...")
        return "none"
    return query

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    speak("logging")
    server.login('jasim9292@gmail.com','cxpdojhvdwcjjpsf')
    speak("what is subject of mail")
    subject = takecommand()
    speak("what is the body of mail")
    body = takecommand()
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('jasim9292@gmail.com', 'jassu92@yahoo.com', msg)
    speak("email has been sent\n")
    server.quit()

if __name__ == '__main__':
    greet()
    while True:
        query = takecommand().lower()
        #logic for task to execute query
        if "wikipedia" in query:
            print("searching...")
            query = query.replace('wikipedia', ' ')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia: ")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is: {strtime}")
        elif "open firefox" in query:
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox_path)
        elif "open pycharm" in query:
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharm_path)
        elif "who are you" in query:
            speak("I am Echo, Your Virtual Assistant. I am developed by Jassem. My boss Jassem created me with Python Module and its Library")
        elif "how old are you" in query:
            speak("I am less than one year old ")
        elif "open outlook" in query:
            outlook_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(outlook_path)
        elif "open twitter" in query:
            webbrowser.open("twitter.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open foss" in query:
            webbrowser.open("itsfoss.com")
        elif "omg ubuntu" in query:
            webbrowser.open("omgubuntu.co.uk")
        elif "what is date" in query:
            day = datetime.datetime.now()
            speak(f"Today is : {day}")
        elif "email" in query:
            try:
                sendEmail()
            except Exception as e:
                speak("sorry i am not able to send this mail")
        elif "quit" in query:
            exit()







