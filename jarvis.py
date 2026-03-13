
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import cv2
import numpy as np

# ---------------- VOICE ENGINE ----------------
engine = pyttsx3.init()
engine.setProperty('rate',170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- SPEECH RECOGNITION ----------------
recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# ---------------- JARVIS UI ----------------
def jarvis_ui(text="JARVIS ONLINE"):
    img = np.zeros((500,800,3), np.uint8)

    cv2.putText(img,text,(50,250),
    cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),3)

    cv2.imshow("JARVIS",img)
    cv2.waitKey(1)

# ---------------- AI REPLY ----------------
def ai_reply(command):

    if "hello" in command or "hi" in command:
        return "Hello sir, how can I help you"

    elif "how are you" in command:
        return "I am fine sir"

    elif "your name" in command:
        return "My name is Jarvis"

    elif "who created you" in command:
        return "You created me sir"

    elif "what can you do" in command:
        return "I can open websites, tell time and talk with you"

    else:
        return "Sorry sir, I didn't understand"

# ---------------- START JARVIS ----------------
speak("Jarvis Activated")
jarvis_ui("JARVIS ACTIVATED")

while True:

    command = take_command()

    if "time" in command:

        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
        jarvis_ui("TIME: " + time)

    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        jarvis_ui("OPENING YOUTUBE")

    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://google.com")
        jarvis_ui("OPENING GOOGLE")

    elif "play music" in command:

        speak("Playing music")
        webbrowser.open("https://spotify.com")
        jarvis_ui("PLAYING MUSIC")

    elif "bye" in command or "exit" in command:

        speak("Goodbye sir , have a nice day")
        jarvis_ui("SYSTEM SHUTDOWN")
        break

    elif command != "":

        reply = ai_reply(command)
        speak(reply)
        jarvis_ui(reply)

cv2.destroyAllWindows()
