
from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

root = Tk()
root.geometry('1080x800')

root.title("Language Translator -- DANUSHRAJ M")
root.config(bg = 'light yellow')

#heading
Label(root, text = "LANGUAGE TRANSLATOR", font = "Magneto 20", bg='light yellow').place(x=350,y=20)



#INPUT AND OUTPUT TEXT WIDGET
Label(root,text ="ENTER THE TEXT", font = 'chiller 15 bold',bg='light pink').place(x=150,y=140)
Input_text = Text(root,font = 'arial 10', height = 20, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y =200)




Label(root,text ="TRANSLATED WORDS", font = 'chiller 15 bold',bg='magenta').place(x=780,y=140)
Output_text = Text(root,font = 'arial 10', height = 20, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 200)
 

#START ASSISTANT

def welcomemsg():
    engine = pyttsx3.init() # object creation
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 120)     # setting up new voice rate

    #"""VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1)    # setting up volume level  between 0 and 1

    #"""VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female 0 for male.

    engine.say("Hi , Welcome to The Translator !")
    engine.runAndWait()
    engine.stop()


#DROP DOWN LIST BOX

language = list(LANGUAGES.values())
welcomemsg()
src_lang = ttk.Combobox(root, values= language,height=15, width =30)
src_lang.place(x=20,y=80)
src_lang.set('From language')
dest_lang = ttk.Combobox(root, values= language,height=15, width =30)
dest_lang.place(x=800,y=80)
dest_lang.set('To language')




#END ASSISTANT

def endmsg(s1):
    engine = pyttsx3.init() # object creation
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 120)     # setting up new voice rate

    #"""VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1)    # setting up volume level  between 0 and 1

    #"""VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female 0 for male.

    engine.say("Here is your Translated Sentence ")
    engine.say(str(s1))
    engine.runAndWait()
    engine.stop()

    


#######  Translate function #######

def Translate():
    flag=0;flag1,flag2=0,0;f3=0
    # warnings #
    if src_lang.get() not in language and dest_lang.get() not in language:
        messagebox.showwarning("Language Translator -- DANUSHRAJ M","Kindly select the input and output language!!");
    if src_lang.get() not in language and dest_lang.get() in language:
        messagebox.showwarning("Language Translator -- DANUSHRAJ M","Kindly select the input language!!");
    if dest_lang.get() not in language and src_lang.get() in language:
        messagebox.showwarning("Language Translator -- DANUSHRAJ M","Kindly select the language to be translated!!")
    if src_lang.get() == dest_lang.get():
        messagebox.showwarning("Language Translator -- DANUSHRAJ M","Input and Output Language Must be Unique!!");f3=1
    if dest_lang.get() in language and src_lang.get() in language:flag1,flag2=1,1

    #TRANSLATE BUTTON PRESS#
   
    translator = Translator()
    if Input_text.get(1.0,END).strip():
            translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get());Output_text.delete(1.0, END);Output_text.insert(END, translated.text)
            endmsg(translated.text)
    elif not Input_text.get(1.0,END).strip() and flag1 and flag2 and not f3:messagebox.showwarning("Language Translator -- DANUSHRAJ M","Kindly enter the words to be translated!!")




##########  Translate Button ########
trans_btn = Button(root, text = 'Translate\n ==>',font = 'Forte 12 bold',pady = 5,command = Translate ,state="active",bg = 'light blue',relief="ridge", activeforeground = 'purple',activebackground = 'sky blue')
trans_btn.place(x = 487, y = 260)

root.mainloop()

