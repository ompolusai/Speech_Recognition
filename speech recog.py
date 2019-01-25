from translate import Translator
#install translate
import os
import speech_recognition as sr
#install speechRecognition
from gtts import gTTS
#install gTTs package
r = sr.Recognizer()
print('say something in english')
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
translator =  Translator(to_lang="te")
#install the translator package
translation = translator.translate(text)
#install the translation package
hindi_audio = gTTS(text = translation, lang='en')
hindi_audio.save('hindi_audio.mp3')
os.startfile('hindi_audio.mp3')
print(translation)
#download langdata master from github
#install google-api-python-client