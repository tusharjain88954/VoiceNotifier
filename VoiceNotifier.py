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



def notification_():
    root.destroy() # destroy all loops and widgets
    while(True):
        Title_ = Title.get()
        msg_ = msg.get() 
        path_to_icon = "D:\\coding_files\\remainder.ico"
        notification.notify(
            title = Title_ ,
            message = msg_,
            app_icon = path_to_icon,
            timeout = 1 
        )
        subprocess.call('espeak '+'"'+msg_+'"', shell=True)
        time.sleep(7200) # remainder repeating time

Label(root , text="Enter title",bg="#1E1B1B",fg="#A22314").grid(row=1,column=1)

Entry(root , textvariable=Title,bg="#1E1B1B",fg="#279DDE").grid(row=1,column=2)

Label(root , text="Enter a short message",bg="#1E1B1B",fg="#A22314").grid(row=2,column=1)

Entry(root , textvariable=msg,bg="#1E1B1B",fg="#279DDE").grid(row=2,column=2)

Button(root , text="Set Remainder" ,bg="#1E1B1B",fg="#A22314",command=notification_).grid(row=3,column=2) # on clicking button , it will call notification_ function

root.mainloop()   
