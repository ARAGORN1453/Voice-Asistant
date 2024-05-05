import pyttsx3
import speech_recognition as sr 
import datetime
import os 
import cv2 
from requests import get
import wikipedia
import webbrowser
from gtts import gTTS
from playsound import playsound
import random

# text to speech
def speak(audio):
    xtts=gTTS(text=audio,lang="tr")
    file="file"+str(random.randint(1,10000))+".mp3"
    xtts.save(file)
    playsound(file)
    os.remove(file)

# To convert voice into text
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum..")
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        print("Sesi tanımlıyorum...")
        query=r.recognize_google(audio,language="tr-TR")
        print(f"Şunu söylediniz : {query}")
    except Exception as e  :
        print(e)
        speak("Lütfen tekrar edin.")
        return None
    return query 

# to wish 
def wishes():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Günaydın efendim.")
    elif hour>12 and hour<=17:
        speak("İyi günler efendim.")
    elif hour>17 and hour<=21:
        speak("İyi akşamlar efendim .")
    else:
        speak("İyi geceler efendim.")
    speak("Ben Lucy,size nasıl yardımcı olabilirim?")

if __name__ =="__main__":
    wishes()
    cap=cv2.VideoCapture(0)
    while True:

        query=take_command().lower()

        # logic building for tasks
        if "not defterini aç" in query:
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "komut istemini aç" in query:
            os.system("start cmd")


        elif "kamerayı aç" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,frame=cap.read()
                cv2.imshow("Camera",frame)
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break 
            cap.release()
            cv2.destroyAllWindows()

        elif "youtube aç" in query:
            speak("Ne izlemek istersiniz efendim ?")
            cm=take_command().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")

        elif " netflix aç " in query:
            speak("Hangi film ya da diziyi izlemek istersiniz efendim ?")
            cm=take_command().lower()
            webbrowser.open(f"https://www.netflix.com/search?q={cm}")

        elif "google aç" in query :
            speak("Google da ne aramak istersiniz efendim")
            cm=take_command().lower()
            webbrowser.open(f"https://www.google.com/search?client=opera-gx&q={cm}&sourceid=opera&ie=UTF-8&oe=UTF-8")





        elif "çıkış" in query:
            break







        

