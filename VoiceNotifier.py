from plyer import notification
import os
import time
import subprocess
from tkinter import *

root = Tk() # Creating root for Voice-Notifier Window
# root.iconbitmap("remainder.ico")
root.title("VoiceNotifier")
root.configure(bg="#1E1B1B")
root.geometry("300x200") 
Title = StringVar() # StringVar is used for modifying widget text
msg = StringVar()
t = IntVar()


def notification_():
    root.destroy() # destroy all loops and widgets
    while(True):
        Title_ = Title.get()
        msg_ = msg.get() 
        t_ = t.get()
        path_to_icon = "D:\\coding_files\\remainder.ico" # Current directory address
        notification.notify(
            title = Title_ ,
            message = msg_,
            app_icon = path_to_icon,
            timeout = 2 # notification stay time
        )
        subprocess.call('espeak '+'"'+msg_+'"', shell=True)
        time.sleep(t_) # remainder repeating time

Label(root , text="Title",bg="#1E1B1B",fg="#A22314").grid(row=1,column=1)

Entry(root , textvariable=Title,bg="#1E1B1B",fg="#279DDE").grid(row=1,column=2)

Label(root , text="Message",bg="#1E1B1B",fg="#A22314").grid(row=2,column=1)

Entry(root , textvariable=msg,bg="#1E1B1B",fg="#279DDE").grid(row=2,column=2)

Label(root , text="Time in seconds",bg="#1E1B1B",fg="#A22314").grid(row=3,column=1)

Entry(root , textvariable=t,bg="#1E1B1B",fg="#279DDE").grid(row=3,column=2)

Button(root , text="Set Remainder" ,bg="#1E1B1B",fg="#A22314",command=notification_).grid(row=4,column=2) # on clicking button , it will call notification_ function

root.mainloop()   
