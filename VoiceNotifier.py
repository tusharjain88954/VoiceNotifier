from plyer import notification
import os
import time
import subprocess
from tkinter import *


root = Tk() # Creating root for Voice-Notifier Window
root.geometry("500x500") 
root.title("VoiceNotifier")
# root.configure(bg="#1E1B1B")
Title = StringVar() # StringVar is used for modifying widget text
msg = StringVar()


def notification_():
    root.destroy() # destroy all loops and widgets
    while(True):
        Title_ = Title.get()
        msg_ = msg.get() 
        pwd=os.getcwdb()# get the current working directory(byte string format).
        path_to_icon = pwd + b'\\remainder.ico'

        notification.notify(
            title = Title_ ,
            message = msg_,
            app_icon = path_to_icon,
            timeout = 1 
        )
        subprocess.call('espeak '+'"'+msg_+'"', shell=True)
        time.sleep(10) # remainder repeating time

label1 = Label(root , text="Enter title") 
label1.pack()

e1 = Entry(root , textvariable=Title)
e1.pack()

label2 = Label(root , text="Enter a short message")
label2.pack()

e2 = Entry(root , textvariable=msg)
e2.pack()

button1 = Button(root , text="Set Remainder" ,command=notification_) # on clicking button , it will call notification_ function
button1.pack()

root.mainloop()   
