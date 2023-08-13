import subprocess #used to get various sub process details such as shutdown,sleep 
import wolframalpha #used in expert level answering using wolframs algorithm ,knowledge base and AI technology
import pyttsx3 #used to convert text to speech 
import tkinter #used in building GUI 
import json #usd to transfer data in form of text that can sent over network
import random 
import operator #expoers set of efficient functions corresponding to intresic operators in python 
import speech_recognition as sr #recognizes the speech from user 
import datetime 
import wikipedia #collects data from wikipedia
import webbrowser #to perfrom websearch 
import os 
import winshell #module offers spetial folders ,file operations,shortcuts,structured storage 
import pyjokes
import feedparser
import smtplib #used to sent email 
import ctypes # provide C-compatible data types and allow the calling functions in shared libraries or dynamic link libraries.
import time
import requests #allows to send HTTP requests using python 
import shutil #allows file operaations like copy,create and remote operations
from twilio.rest import Client #used to amke calls and messages 
#from Clint.textui import progress 
from ecapture import ecapture as ec # used to capture images from camera 
from bs4 import BeautifulSoup #used to scrape information from webpages
import win32com.client as wincl
from urllib.request import urlopen #used in fetching URL,offers simple interface,capable of fetching url from different protocols
import numpy as np
import cv2
import pyautogui
from tkinter.filedialog import *
import socket 
import pywhatkit 
from geopy.geocoders import Nominatim



app=wolframalpha

try:
    app=wolframalpha.Client("8QPPX9-8723AWLA7Y")
except Exception as e:
    print(e)
    print("unable to recognize")   


#using pyttsx3 for text to speech 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #voices[1] for female voice 

#definig function to speak 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#definig function to wish 
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0  and hour <12: 
        print("good morinig sir")
        speak("good moring sir....")

    elif hour>12 and hour<16:
        print("good afternoon sir ")
        speak("good afternoon sir ")

    else:
        print('good evening sir ')
        speak("good evening sir")
    assname=('jarvis 2 point O')
    print(f"i am your assistant \n{assname}")
    speak(f"i am your assistant \n{assname}")

def username():
    speak("what would i call you sir ")
    uname=takecommand()
    speak("welcome mister")
    
    columns=shutil.get_terminal_size().columns

    print("###############".center(columns))
    print("welcome mr.",uname.center(columns))
    print("##############".center(columns))

    speak(f"how may i help you mr.{uname}")

def takecommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("listenig.........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing..........")
        query=r.recognize_google(audio,language="en-in")
        print(f"your query was :\n{query}")

    except Exception as e:
        print(e)
        speak("sarriga cheppu raa ")
        print("unable to recognize ypur command ")
        return None
    return query

def sendemail(to,content):
    pass


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any command before execution of this python file
    clear()
    wishme()
    #username()
     
    while True: 

        query = takecommand().lower()

        
        if "wikipedia" in query:
            speak("searching on wikipedia ......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak(results)
            print(results)

        elif "on youtube" in query:
            speak("playing it shortly sir .......")  
            query=query.replace("on youtube","")
            

            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("sir what should i search for you on google .........")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
            webbrowser.open("google.com")

        elif "stack overflow" in query:
            speak("opening stack overflow shortly....")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query :
            speak("playing music shortly.......")
            music_dir="C:\\Users\\vinay\\Downloads\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            random=os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time " in query:
            strtime=datetime.datetime.now().strftime("%H %M %S")
            speak(f"the time is {strtime}")

        elif "email to vinay" in query :
            speak("what should i say?")
            content=takecommand()
            to="reciever email address"
            sendemail(to,content)
            speak("email has been sent")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif "exit" in query:
            print("thanks for giving your time ") 
            speak("thanks for giving your time ")
            exit()

        elif "joke" in query:
            speak(pyjokes.get_joke()) 

        

        elif "screenshot" in query:# take screenshot using pyautogui  
            root=tkinter.Tk()
            window=tkinter.Canvas(root,width=200,height=200)
            window.pack()

            def take_ss(): 
                screenshot=pyautogui.screenshot()
                savepath=asksaveasfilename()
                screenshot.save(savepath+"_screenshot.png")
            ss_button=tkinter.Button(text="take screenshot",command=take_ss,font=20)
            window.create_window(100,100,window=ss_button)
            root.mainloop() 


        elif "alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir="C:\\Users\\vinay\\Downloads\\songs"
                song=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[0])) 


        elif "ip address" in query:
            hostname=socket.gethostname()
            ipaddr=socket.gethostbyname(hostname)
            speak("your computer name is "+hostname)
            print("your computer name is "+hostname)
            speak("your ip address is "+ipaddr)
            print("your ip address is "+ipaddr) 



        elif "send message" in query: 
            pywhatkit.sendwhatmsg("+919515919840","this is testing message",10,59)

        elif "play song" in query:
            query=query.replace("play song","") 
            speak(query)
            pywhatkit.playonyt(query) 

        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(5)
            pyautogui.keyUp("alt")


        else:
            try:
                responce=app.query(query)
                print(next(responce.results).text)# PIL(pillow) and in RGB we need to #convert it to numpy array and BGR 

                speak(next(responce.results).text)

            except :
                print("internet problem")


'''elif "camera" in query:
            cap=cv2.VideoCapture(0) 
            while True:
                ret,image=cap.read()
                cv2.imshow("webcam",image)
                k=cv2.waitKey(50)
                #if k==27:
                 #   break
            cap.release()
            cv2.destroyAllWindows()'''
"""        elif "where" in query:
            send_url = "http://api.ipstack.com/check?access_key=YOUR_ACCESS_KEY"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']"""
      




            
        
        

  


   






