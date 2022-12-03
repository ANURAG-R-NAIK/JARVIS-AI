import pyttsx3 #for the voice of denji
import wikipedia #for info through wikipedia
import webbrowser # for redirecting on the web
import speech_recognition as sr  #to recognise the speech through google
import datetime  #for the date and time access
import os
import smtplib

engine = pyttsx3.init('sapi5')  #by microsoft used to take the voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#takes the voices and sets the one we want from them


def speak(audio):
    '''THIS FUNCTION MAKES THE AI SPEAK THE COMMANDS GIVEN'''
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    ''' GREETS THE USER AND THEN INTRODUCES HIMSELF'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour <= 18:
        speak("Goood Afternoon Sir")    
    else:
        speak("Good Evening Sir")  
    
    speak("I am Denji")   
    speak("Please tell me how may i help you")

def takecommand():
    #It takes microphone input from the user and gives output as a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail,com" , 'your-password')  ####THIS TWO LINES HERE YOU HAVE TO GIVE UR RMAIL###
    server.sendemail('youreemail@gmail.com', to , content) ########ALSO WRITE THE COMMENTS FOR THE LAST FEW PARTS#######
    server.close()    
if __name__ == "__main__":
    wishMe()
    
    #now based on query by user we do the tasks
    while True:
        query = takecommand().lower() #the query gets converted inlower case so it matches easily without any errors
        
        if 'wikipedia' in query: #make sure u tell wikipedia in the sentence
            speak('Searching Wikipedia....') #this told in the atart of the converstaion
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) #summary is made out of wikipedia in 2 lines
            speak("According to wikipedia") #the sentence before giving the results
            print(results)
            speak(results) #speak out the ruslts
            
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'google' in query:
            webbrowser.open("google.com")
        
        elif 'github' in query:
            webbrowser.open("github.com")    
            
        elif 'play music' in query:
            musicdir = 'D:\\JARVIS-AI\\music'
            songs= os.listdir(musicdir)
            print(songs)
            os.start(os.path.join(musicdir, songs[0]))#####TO BE WORKED UPON PUT SOME SONGS 
            #ALSO USE RANDON MODULE AND PLAY RANDOM SONGS##########
            
        elif 'the time' in query:
            strtime = datetime.datetime.strftime("%H:%M:%S")
            speak(f"Sir , The time is {strtime} ")
            
        elif 'open code ' in query:
            cpath =  "C:\\Users\\anura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(cpath) ########TO BE WORKED UPON NOT WORKING######
            
        elif 'email' in query: 
            try: 
                speak("What should i say?")
                content = takecommand()
                to = "anuragnaik02@gmail.com"
                sendemail(to, content)
                speak ("Email has been sent!")
                
            except Exception as e:
                speak ("sorry this email is not sent presently ! ")  
                speak("Try again  later")
            
            