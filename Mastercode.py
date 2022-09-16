#import time
#exec(open("voiceassistant.py").read())
#time.sleep(100)
#exec(open("toyreyalgo.py").read())
#time.sleep(100)
#exec(open("speech.py").read())
from __future__ import print_function

#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import time
import os
import openai
import time
from gtts import gTTS
openai.api_key = "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"
from http.client import UNAUTHORIZED
file = open("text.txt","w")
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

WAKE = "ok"
print("Start")
y = 0
while y<1:
    print("Listening")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("On what topic would you like to hear a story about")
        
        toys = get_audio()
        #file.write("A story about " + str(toys))
        input_str = "A story about " + str(toys)
        y = y+1

#file = open("text.txt","r")
text = input_str
response = openai.Completion.create(
  model="text-davinci-002",
  prompt= text,
  temperature=0.5, # 1 toy -0.5, 2   toys - 
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
#output = open("output.txt","w")
#output.write(response["choices"][0].text)
output_str = response["choices"][0].text
#print(response["choices"][0].text)
def text_to_speech(text,lang):
        
        #mytext = 'There was a girl. She loved to play.There were many games but did not have great fun. Let us begin our story.'
# Language in which you want to convert
        language = lang  #Check the gtts documentation to get lang codes

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
        myobj = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
        myobj.save("msg.mp3")

# Playing the converted file
        #playsound("msg.mp3")
        
        os.system("start msg.mp3")
        return
#test
#file = open("output.txt","r")
mytext = output_str
text_to_speech(mytext,'en')
