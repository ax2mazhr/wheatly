import win32com.client as wincl
from playsound import playsound
import datetime
import threading


speak = wincl.Dispatch("SAPI.SpVoice")
playsound('hello.mp3')
speak.Speak("Hello World")
alarms = ["test"]
print("start " + datetime.datetime.now().strftime("%y/%m/%d %H:%M"))

def alarm():

	while True:
		if int(datetime.datetime.now().strftime("%f")) > 999000 :
			print(datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S"))
			print(alarms)
		if datetime.datetime.now().strftime("%y/%m/%d %H:%M") in alarms :
			threading.Thread(target = playsound, args=("wake.mp3",)).start()
			# threading.Thread(target = playsound, args=("wake2.mp3",)).start()
			# speak.Speak("wake up bitch")
			# speak.Speak("wake up bitch")
			# speak.Speak("wake up bitch")
			print("wake up bitch")
			alarms.remove(datetime.datetime.now().strftime("%y/%m/%d %H:%M"))


def inputt():
	global alarms
	alarms.append(input("go ahead"))
	for x in alarms:
			print(x)
	inputt()


threading.Thread(target = inputt).start()
alarm()
