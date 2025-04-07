import pyttsx3

def say(speach):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(speach)
    engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    say('Hello')