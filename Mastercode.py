
from __future__ import print_function
from playsound import playsound
from translate import *
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


def speak(text,language):
		
		
# Language in which you want to convert
		 #Check the gtts documentation to get lang codes

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
	myobj = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
	myobj.save("msg.mp3")

# Playing the converted file
	playsound("msg.mp3")
		
		#os.system("start msg.mp3")
	return
def get_audio(lang):
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio,language = lang )
			print(said)
		except Exception as e:
			pass
		if(lang[:2] == 'en'):
			return said.lower()
		else:
			return said

WAKE = "ok"
print("Start")
y = 0
while y<1:
	
	print("Listening")
	text = get_audio('en-US')
	
	if text.count(WAKE) > 0:
		speak("Please choose your language ",'en')
		speak('''कृपया भाषा चुनें''','hi')
				
		given_lang = str(get_audio('en-US'))
	
		if (given_lang).lower() == 'english':
			speak("On what topic would you like to hear a story about",'en')
			toys = str(get_audio('en-US'))
			speak('Would you like to hear their history or a story about them?','en')
			preference = str(get_audio('en-US'))
			if 'story' in preference.lower():
				input_str = "A story about Indian toys - " + str(toys)
				temperature =0.5	
				y+=1
			#else preference.lower():
			#	input_str = 'The history of Indian toys ' +str(toys)
			#	temperature = 0
			#	y+=1
			text = input_str
			response = openai.Completion.create(
			model="text-davinci-002",
			prompt= text,
			temperature=temperature, # 1 toy -0.5, 2   toys - 
			max_tokens=500,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0
			)

			output_str = response["choices"][0].text

			mytext = output_str
			speak(mytext,'en')
		elif given_lang.lower() == 'hindi':
			speak('''आप किन खिलौनों के बारे में सुनना चाहेंगे''',
'hi')
			toys = str(get_audio('hi-IN'))
			toys = hindi_to_english(toys)
			#speak('क्या आप इन खिलौनों के बारे में कहानी सुनना चाहेंगे या उनका इतिहास?','hi')
			#preference = str(get_audio('hi'))
			print()
			#if ' कहानी ' in preference:
			input_str = "A story of Indian - " + (str(toys))
			temperature =0.5	
			y+=1
			#else:
			#	input_str = 'The history of Indian toys ' +str(toys)
			#	temperature = 0
			#	y+=1
			text = input_str
			response = openai.Completion.create(
			model="text-davinci-002",
			prompt= input_str,
			temperature=temperature, # 1 toy -0.5, 2   toys - 
			max_tokens=500,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0
			)

			output_str = response["choices"][0].text

			mytext = english_to_hindi(output_str)
			speak(mytext,'hi')
		
		
	
 
