import pyttsx3 as pt
def speak(text):
    engine=pt.init()
    engine.say(text)
    engine.runAndWait
#print("hello")
speak("nice")