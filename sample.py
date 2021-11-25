from tkinter import *
from requests import get


def yesorno(root):
    yesorno = Label(root, text = "Enter your ip address: ")
    yesorno.pack()
    root.disp_tf = Entry(
    ws, 
    width=38,
    font=('Arial', 14)
    )
    root.disp_tf.pack()
    submitbtn = Button(
    ws,
    text='Submit',
    relief=SOLID,
    command=lambda root = ws: youripadd(root)
)
    submitbtn.pack()





def youripadd(root):
    ipcountry = root.disp_tf.get()
    youripaddis = Label(root, text = "Your country is  " + (get('https://ipapi.co/'+ipcountry+'/country/').text))
    youripaddis.pack()

def frame_sentence():
    yorno = yorno_tf.get()

def thankyou(root):
    thankyousm = Label(root, text = "Thank you!  ")
    thankyousm.pack()
    prepared = Label(root, text = "Prepared By:  ")
    prepared.pack()
    vincent = Label(root, text = "Ferrer, Vincent ")
    vincent.pack()
    jeric = Label(root, text = " Mataga, Carl ")
    jeric.pack()
    donna = Label(root, text = " Olidana, Donna  ")
    donna.pack()
 
  

ws = Tk()
ws.title('"DEVASC PROJECT')
ws.geometry('700x500')
ws.config(bg='#0f4b6e')

yorno_tf = Entry(ws)

yorno_lbl = Label(
    ws,
    text='Do you want to search the details of an IP Address? (wink wink) (Y/N)',
    bg='#0f4b6e',
    fg='white'
)
title2 = Label(
    ws,
    text="This will display your local computer's information such as your public IP Address",
    bg='#0f4b6e',
    fg='white'
)

space = Label(
    ws,
    text="",
    bg='#0f4b6e',
    fg='white'
)
space2 = Label(
    ws,
    text="",
    bg='#0f4b6e',
    fg='white'
)


ipadd = Label(
    ws,
    text='Your IP Address is ' + (get('https://ipapi.co/ip/').text),
    bg='#0f4b6e',
    fg='white'
)

city = Label(
    ws,
    text='The city is ' +(get('https://ipapi.co/city/').text),
    bg='#0f4b6e',
    fg='white'
)

country = Label(
    ws,
    text='The country is ' +(get('https://ipapi.co/country/').text),
    bg='#0f4b6e',
    fg='white'
)

currency = Label(
    ws,
    text='The currency of that country is ' +(get('https://ipapi.co/currency/').text),
    bg='#0f4b6e',
    fg='white'
)

languages = Label(
    ws,
    text='The languages that is being used are ' +(get('https://ipapi.co/languages/').text),
    bg='#0f4b6e',
    fg='white'
)

asn = Label(
    ws,
    text='The ASN is ' +(get('https://ipapi.co/asn/').text),
    bg='#0f4b6e',
    fg='white'
)



title2.pack()
space.pack()
ipadd.pack()
city.pack()
country.pack()
languages.pack()
currency.pack()
asn.pack
space2.pack()
yorno_lbl.pack()


btn = Button(
    ws,
    text='Yes',
    relief=SOLID,
    command= lambda root = ws: yesorno(root)
)


btn.pack(pady=10)

btn2 = Button(
    ws,
    text='No',
    relief=SOLID,
    command= lambda root = ws: thankyou(root)
)
btn2.pack(pady=10)


ws.mainloop()