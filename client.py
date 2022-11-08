import socket
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8050
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title('Music Sharer')
    window.resizable(width=False,height=False)
    window.configure(width=540,height=490,bg='#202121')

    selectlabel = Label(window, text= "Select Song",bg="#202121" ,fg="white",font = ("Calibri 24 bold"))
    selectlabel.place (x=6, y=4)

    listbox = Listbox(window , height = 20,width = 73, activestyle = "dotbox" , bg='#495057', bd=0 ,highlightthickness=3,font = ("calibri" , 10))
    listbox.place (x=10,y=45)
    listbox.config(cursor='arrow',highlightbackground = "#2ec4b6", highlightcolor= "#2ec4b6")

    scrollbarl = Scrollbar(listbox)
    scrollbarl.place(relheight= 1,relx= 0.965)
    scrollbarl.config(command= listbox.yview)

    PlayButton = Button(window,text='\u23F5', bd=0, bg="#202121",fg='#2ec4b6' , font= ("calibri 32 bold"))
    PlayButton.place (x=200, y=375)
    
    Stop = Button(window, text="⏹", bd=0 , bg="#202121",fg='#2ec4b6', font = ("calibri 48 bold",))
    Stop.place (x=270, y=405)

    Upload = Button(window, text="Upload", width=5,bg="#202121",fg='#2ec4b6',bd=0, font= ("calibri 14 bold"))
    Upload.place (x=130,y=400)

    Download = Button(window , text="Download",width=8,bg="#202121",fg='#2ec4b6',bd=0, font= ("calibri 14 bold"))
    Download.place(x=320, y=400)

    infoLabel = Label(window, text= "",bg="#202121",fg= "#2ec4b6", font = ("Calibri 14 italic") )
    infoLabel.place (x=6, y=460)

    window.mainloop ()

def setup():
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    print('\t\t\t\tCONNECTED')

    musicWindow()

setup()