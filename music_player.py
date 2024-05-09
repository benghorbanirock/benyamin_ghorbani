import pygame
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from mutagen.mp3 import MP3
pygame.init()
clock=pygame.time.Clock()
root=Tk()
root.title('Music player')

courretttt=0

selected_song_label = Label(root, text="Selected Songs:", bg="yellow")
selected_song_label.pack()


def MUSIC_PLAYER():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
    pygame.mixer.init()
    if file_path:
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play(start=courretttt)
            except Exception as e:
                messagebox.showerror("Error", str(e))
    else:
        root.destroy()
    file_name = file_path.split("/")[-1]
    song_label = Label(root, bg='red', text=file_name)
    song_label.pack()
def Pause():
    pygame.mixer.music.pause()
    courretttt=pygame.mixer.music.get_pos()
def unPause():
    pygame.mixer.music.unpause()
    courretttt=pygame.mixer.music.get_pos()
def rewind():
    pygame.mixer.music.rewind()
def exit():
    root.destroy()

paluinbuttun=pygame.K_SPACE
stopbouttun=pygame.K_s

def total_color(button):
    curret_color=button['highlightbackground']
    if curret_color=='red':
        button.config(highlightbackground=None)
    else:
        button.config(highlightbackground="red")



    


buttun1=Button(root,text='play',command=MUSIC_PLAYER)
buttun1.pack()
fa1=Frame(root,bg='green')
fa1.pack(fill='both')
buttun2=Button(root,text='pause',command=Pause)
buttun2.pack()
fa1=Frame(root,bg='green')
fa1.pack(fill='both')
buttun3=Button(root,text='unpause',command=unPause)
buttun3.pack()
fa1=Frame(root,bg='green')
fa1.pack(fill='both')
buttun4=Button(root,text='rewind',command=rewind)
buttun4.pack()
fa1=Frame(root,bg='green')
fa1.pack(fill='both')
buttun5=Button(root,text='exit',command=exit)
buttun5.pack()
fa1=Frame(root,bg='green')
fa1.pack(fill='both')

frame1 = Frame(root, width=200, height=100, bg="magenta")
frame1.pack(side=LEFT)
frame2 = Frame(root, width=200, height=100, bg="green")
frame2.pack(side=RIGHT)

label = Label(root, text="date_music")
label.pack(fill='both',expand=True)
label = Label(root, text="another_music")
label.pack(fill='both',expand=True)



def sayhello():
    messagebox.showinfo(title='Karakit message', message='Hello world!') 
def showabout():
    messagebox.showinfo(title='Karakit Menu', message='This program is made by karakit to show you how to add menus to your GUI.')
def showabout2(self):
    messagebox.showinfo(title='Karakit Menu', message='This program is made by karakit to show you how to add menus to your GUI.')
menubar = Menu(root)
root.config(menu=menubar)
mainmenu=Menu(menubar)
menubar.add_cascade(label="Main", menu=mainmenu)
mainmenu.add_command(label="Hello", command=sayhello)
mainmenu.add_separator()

helpmenu=Menu(menubar)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=showabout,accelerator="Ctrl+H")
n_b=ttk.Notebook(root)
tab1=ttk.Frame(n_b)
label1=ttk.Label(tab1,text='this is text1')
label1.pack()


root.geometry('500x500')
root.mainloop()
    