def text_to_speech(text,lang):
        from playsound import playsound
        from gtts import gTTS



        import os


        #mytext = 'There was a girl. She loved to play.There were many games but did not have great fun. Let us begin our story.'

# Language in which you want to convert
        language = lang  #Check the gtts documentation to get lang codes

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
        myobj.save("msg.mp3")

# Playing the converted file
        playsound("msg.mp3")
        return
#os.system("mpg321 msg.mp3")
#test

mytext = 'There was a girl. She loved to play.There were many games but did not have great fun. Let us begin our story.'
text_to_speech(mytext,'en')
~                                  
