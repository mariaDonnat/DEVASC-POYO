import tkinter as tk
from tkinter import *
from requests import get


def yesorno(root):
    yesorno = Label(
        root, text = "Enter your ip address: ",
        font="Raleway",
        fg='#20bebe'
        )
    yesorno.grid(columnspan=2,column=0,row=13)
    root.disp_tf = Entry(
        ws, 
        width=38,
        font="Raleway",
        fg='#2f303f'
    )
    root.disp_tf.grid(columnspan=2,column=0,row=14)
    spacee= Label(root, text="")
    spacee.grid(columnspan=2,column=0,row=15)
    
    submitbtn = Button(
        ws,
        font= "Raleway",
        bg="#20bebe",
        fg="white",
        height=2,
        width=15,
        text="Submit",
        command=lambda root = ws: youripadd(root)
    )
    submitbtn.grid(columnspan=2,column=0,row=16)


def youripadd(root):
    ipcountry = root.disp_tf.get()
    youripaddis = Label(
        root, 
        text = "Your country is  " + (get('https://ipapi.co/'+ipcountry+'/country/').text),
        font="Raleway",
        fg='#2f303f'
        )
    space_ip = Label(root, text="")
    space_ip.grid(columnspan=2,column=0,row=17)
    youripaddis.grid(columnspan=2,column=0,row=18)

def frame_sentence():
    yorno = yorno_tf.get()

def thankyou(root):
    thankyousm = Label(
        root, 
        text = "Thank you!",
        font=("Raleway bold",15),
        fg='#20bebe'
        )
    thankyousm.grid(columnspan=2,column=0,row=19)
    prepared = Label(
        root, 
        text = "Prepared By: fuck",
        font=("Raleway bold",15),
        fg='#20bebe'
        )
    prepared.grid(columnspan=2,column=0,row=20)
    vincent = Label(
        root, 
        text = "Ferrer, Vincent",
        font="Raleway",
        fg='#2f303f'
        )
    vincent.grid(columnspan=2,column=0,row=21)
    jeric = Label(
        root, 
        text = " Mataga, Carl",
        font="Raleway",
        fg='#2f303f')
    jeric.grid(columnspan=2,column=0,row=22)
    donna = Label(
        root, 
        text = " Olidana, Donna",
        font="Raleway",
        fg='#2f303f')
    donna.grid(columnspan=2,column=0,row=23)
 
  

ws = tk.Tk()
ws.title('DEVASC PROJECT 4 : Ferrer, Mataga, Olidana')

canvas = tk.Canvas(ws, width=600, height= 300)
canvas.grid(columnspan=2, rowspan=24)

yorno_tf = Entry(ws)

yorno_lbl = Label(
    ws,
    text='Do you want to search the details of an IP Address?',
    font=("Raleway bold",15),
    fg='#20bebe'
)
title2 = Label(
    ws,
    text="This will display your local computer's information\n such as your public IP Address and more",
    font=("Raleway bold",20),
    fg='#20bebe'
)
space0 = Label(
    ws,
    text="",
)
space = Label(
    ws,
    text="",
)
space2 = Label(
    ws,
    text="",
)
space3 = Label(
    ws,
    text="",
)

ipadd = Label(
    ws,
    text='Your IP Address is ' + (get('https://ipapi.co/ip/').text),
    font="Raleway",
    fg='#2f303f'
)

city = Label(
    ws,
    text='The city is ' +(get('https://ipapi.co/city/').text),
    font="Raleway",
    fg='#2f303f'
)

country = Label(
    ws,
    text='The country is ' +(get('https://ipapi.co/country/').text),
    font="Raleway",
    fg='#2f303f'
)

currency = Label(
    ws,
    text='The currency of that country is ' +(get('https://ipapi.co/currency/').text),
    font="Raleway",
    fg='#2f303f'
)

languages = Label(
    ws,
    text='The languages that is being used are ' +(get('https://ipapi.co/languages/').text),
    font="Raleway",
    fg='#2f303f'
)

asn = Label(
    ws,
    text='The ASN is ' +(get('https://ipapi.co/asn/').text),
    font="Raleway",
    fg='#2f303f'
)

space0.grid(columnspan=2,column=0,row=0)
title2.grid(columnspan=2,column=0,row=1)
space.grid(columnspan=2,column=0,row=2)
ipadd.grid(columnspan=2,column=0,row=3)
city.grid(columnspan=2,column=0,row=4)
country.grid(columnspan=2,column=0,row=5)
#languages.grid(columnspan=2,column=0,row=6)
currency.grid(columnspan=2,column=0,row=7)
asn.grid(columnspan=2,column=0,row=8)
space2.grid(columnspan=2,column=0,row=9)
yorno_lbl.grid(columnspan=2,column=0,row=10)



btn = Button(
    ws,
    font= "Raleway",
    bg="#20bebe",
    fg="white",
    height=2,
    width=15,
    text='YES',
    command= lambda root = ws: yesorno(root)
)

btn2 = Button(
    ws,
    font= "Raleway",
    bg="#73bebe",
    fg="white",
    height=2,
    width=15,
    text='NO',
    command= lambda root = ws: thankyou(root)
)
btn2.grid(column=0,row=11)
btn.grid(column=1, row=11)
space3.grid(columnspan=2,column=0,row=12)

canvas = tk.Canvas(ws, width=600, height= 50)
canvas.grid(columnspan=3)

ws.mainloop()