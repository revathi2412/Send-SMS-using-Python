import tkinter as tk

from tkinter import*

from tkinter import messagebox

import requests

root = tk.Tk()

root.geometry('200x200')

root.maxsize(300,300)

root.minsize(300,300)

root.title('Send SMS')



def send_sms():
        
    number = phone_no.get()
 
    messages = message.get("1.0","end-1c")

 
    url = "https://www.fast2sms.com/dev/bulk"

    api = "Enter your api here" #fast2sms api
 
    querystring = {"authorization":api,"sender_id":"FSTSMS","message":messages,"language":"english","route":"p","numbers":number}

 
    headers = {
                 'cache-control': "no-cache"
                 }
       
    requests.request("GET", url, headers=headers, params=querystring)
       
    messagebox.showinfo("Send SMS",'SMS has been send successfully')



label = Label(root,text="Send SMS Using Python",font=('verdana',10,'bold'))

label.place(x=60,y=20)


phone_no = Entry(root,width=20,borderwidth=0,font=('verdana',10,'bold'))

phone_no.place(x=60,y=100)
phone_no.insert('end','phone number')


message = Text(root,height=5,width=25,borderwidth=0,font=('verdana',10,'bold'))

message.place(x=40,y=140)

message.insert('end','Message')


send = Button(root,text="Send Message",font=('verdana',10,'bold'),bg='blue',cursor='hand2',borderwidth=0,command=send_sms)

send.place(x=90,y=235)

root.mainloop()