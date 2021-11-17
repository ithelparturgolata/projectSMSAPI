# pip install pep8
# pip install pycodestyle
# pep8 --first dkmodraczekApp.py
# pycodestyle --first dk_modraczek.py
# coding: utf-8
from tkinter import *
from smsapi.client import SmsApiPlClient
from smsapi.client import SmsApiComClient
import os


def sendSMS():
    entryKontakt.info = entryKontakt.get()
    entryTresc.info = entryTresc.get()
    token = "wpisz swoj Token"
    client = SmsApiPlClient(access_token=token)
    send_results = client.sms.send(to=entryKontakt.info,
                                   message=entryTresc.info,
                                   from_="SMBUDOWLANI")
    for result in send_results:
        print(result.id, result.points, result.error)

    entryTresc.delete(0, END)
    entryKontakt.delete(0, END)

root = Tk()
root.title("Bramka SMS")
root.geometry("700x450")

appFrame1 = Frame(root, pady=20)
appFrame2 = Frame(root, pady=20)
appFrame3 = Frame(root, pady=20)

appFrame1.grid(row=0, column=0, sticky=W)
appFrame2.grid(row=1, column=0, sticky=E)
appFrame3.grid(row=2, column=0, sticky=E)

entryKontakt = IntVar()
entryTresc = StringVar()

# widget appFrame1
labelKontakt = Label(appFrame1, text="Podaj numer: ", font=("bold", 12))
entryKontakt = Entry(appFrame1, width=30,
                     textvariable=entryKontakt,
                     font=("bold", 12))

labelKontakt.grid(row=0, column=0)
entryKontakt.grid(row=0, column=1)

# widget appFrame2
labelTresc = Label(appFrame2, text="Treść: ", font=("bold", 12))
entryTresc = Entry(appFrame2, width=30,
                   textvariable=entryTresc,
                   font=("bold", 12))

labelTresc.grid(row=1, column=0)
entryTresc.grid(row=1, column=1)

# widget appFrame3
buttonSend = Button(appFrame3, text="Wyślij",
                    activebackground="yellow",
                    relief=GROOVE,
                    command=sendSMS,
                    font=("bold", 12))
buttonSend.grid(row=3, column=0)
root.mainloop()
