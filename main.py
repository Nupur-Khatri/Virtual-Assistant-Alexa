import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            engine.say('Hello! I am Alexa.Let me know how can i help you')
            engine.runAndWait()
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        talk('Thank you for coming! do recall me when in need. Good byyyeee')
        sys.exit()
    return command


def take_command2():
    try:
        with sr.Microphone() as source:
            engine.say('')
            engine.runAndWait()
            print('listening...')
            voice = listener.listen(source)
            command2 = listener.recognize_google(voice)
            command2 = command2.lower()
            if 'alexa' in command2:
                command2 = command2.replace('alexa', '')
                print(command2)
    except:
        pass
    return command2

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Do you want me to do anything else for you?')
        command2 = take_command2()
        if 'yes' in command2:
            run_alexa()
        else:
            talk('Thank you! do recall me when in need. Good byyye')
        sys.exit()

while True:
    run_alexa()
