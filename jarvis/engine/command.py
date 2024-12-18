import pyttsx3
import speech_recognition as sr
import eel
import time
import webbrowser
import os  # Required to open system applications

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        print(f"Error during recognition: {e}")
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if "hello" in query:
            speak("Hello! How can I assist you today?")
        
        # Opening YouTube
        elif "on youtube" in query or "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        # Opening WhatsApp Web
        elif "open whatsapp" in query:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")
        
        # Opening Facebook
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        
        # Opening Notepad
        elif "open notepad" in query:
            speak("Opening Notepad")
            os.system("notepad")
        
        # Opening Calculator
        elif "open calculator" in query:
            speak("Opening Calculator")
            os.system("calc")
        
        # Opening Calendar
        elif "open calendar" in query:
            speak("Opening Calendar")
            webbrowser.open("https://calendar.google.com")
        
        # Opening Visual Studio Code
        elif "open vs code" in query or "open visual studio code" in query:
            speak("Opening Visual Studio Code")
            os.system("code")  # Ensure VS Code is added to the system PATH
        
        # Opening Chrome
        elif "open chrome" in query:
            speak("Opening Google Chrome")
            os.system("start chrome")
        
        # Opening Gmail
        elif "open gmail" in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")
        
        # Opening File Explorer
        elif "open file explorer" in query:
            speak("Opening File Explorer")
            os.system("explorer")
        
        else:
            speak("Sorry, I didn't understand that.")
            print("Command not recognized.")
    except Exception as e:
        print(f"Error: {e}")
    
    eel.ShowHood()
