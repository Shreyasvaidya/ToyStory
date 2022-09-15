#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install GTTS


# In[11]:


from gtts import gTTS 
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'There was a girl. She loved to play.There were many games but did not have great fun. Let us begin our story.'
  
# Language in which you want to convert
language = 'en'  #Check the gtts documentation to get lang codes
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("msg.mp3")
  
# Playing the converted file
os.system("start msg.mp3")
#os.system("mpg321 msg.mp3")

