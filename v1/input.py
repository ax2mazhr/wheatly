import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source, duration=2)
    print('Speak')
    audio = r.listen(source)
    print('Analysing...')

try:
    print('Google thinks you said: \n' + r.recognize_google(audio))
# text =r.recognize_google(audio)                                    comment the above line and uncomment the followinf lines
#   print(text)

except Exception as e:
    print(e)
