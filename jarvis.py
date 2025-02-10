import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import subprocess
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service, How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('21104016.kaushik.prabhunerurkar@gmail.com', 'password')
    server.sendmail('21104016.kaushik.prabhunerurkar@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\kaushik\Downloads\Music\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery= psutil.sensors_battery()
    speak("Battery is at " )
    speak( battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were multiple results for that query, please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("I could not find any results for your query.")
            except Exception as e:
                speak("Sorry, I encountered an error while searching Wikipedia.")
                print(e)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'kaushik020603@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = f"https://{search}.com"
            try:
                chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                subprocess.Popen([chromepath, url])
            except Exception as e:
                print(f"Failed to open Chrome: {e}")
                speak("Unable to open Chrome, opening with default browser.")
                wb.open_new_tab(url)
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown -/s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t /1")
        elif 'play songs' in query:
            song_dir = r"C:\Users\kaushik\Downloads\Music"
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
        elif 'remember that' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("You said me to remember this data" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you remember' in query:
            remember = open('data.txt','r')
            speak("You said me to remember this data" + remember.read())
        elif "screenshot" in query:
            speak("Taking screenshot")
            screenshot()
            speak("Screenshot Saved")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()

        elif 'offline' in query:
            speak("Going offline. Goodbye!")
            break
