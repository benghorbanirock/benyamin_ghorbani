from tkinter import *
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import colorchooser, filedialog,simpledialog
from PIL import Image, ImageTk,ImageDraw,ImageFont
from numpy import *
from tkinter.simpledialog import askstring
win = Tk()

def choose_photo():
    global photo_path
    photo_path = filedialog.askopenfilename(filetypes=[("Photo", '*.jpg')])

photo_button = Button(win, text='Choose_photo', bg='green', command=choose_photo)
photo_button.pack()

def show_photo():
    imag = Image.open(photo_path)
    img = ImageTk.PhotoImage(imag)
    cv_image = cv2.cvtColor(cv2.imread(photo_path), cv2.COLOR_BGR2RGB)
    cv2.imshow('show_image', cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

photo_button = Button(win, text='Show Photo', bg='green', command=show_photo)
photo_button.pack()


def font_photo():
    imag = Image.open(photo_path)
    img = ImageTk.PhotoImage(imag)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv_image = cv2.imread(photo_path)
    cv2.putText(cv_image, 'hello world', (10, 40), font, 1, (225, 335, 224), 2, cv2.LINE_AA)
    cv2.imshow('show_image', cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

font_photo_button = Button(win, text='Font Photo', bg='blue', command=font_photo)
font_photo_button.pack()

def prohibited_photo():
    cv_image = cv2.imread(photo_path)
    cv2.line(cv_image, (0, 0), (cv_image.shape[1], cv_image.shape[0]), (0, 0, 255), 2)
    cv2.line(cv_image, (cv_image.shape[1], 0), (0, cv_image.shape[0]), (0, 0, 255), 2)
    cv2.imshow('show_image', cv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

prohibited_button = Button(win, text='Prohibited Photo', bg='magenta', command=prohibited_photo)
prohibited_button.pack()

def show_image_and_text(sem, color=None):
    image = Image.open(photo_path)
    drew = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Define rgb_color before the check
    rgb_color = color if color else 'red'  # Provide a default color if color is None

    if sem is not None:
        drew.text((100, 100), sem, font=font, fill=rgb_color)
    cv2_image = cv2.cvtColor(array(image), cv2.COLOR_RGB2BGR)
    cv2.imshow("show_image", cv2_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_photo():
    show_image_and_text(None, photo_path, None)

def font_photo():
    photo_path = filedialog.askopenfilename(filetypes=[("Photo", '*.jpg')])
    show_image_and_text('hello world', photo_path, None)



def choose_color_and_image():

    color = colorchooser.askcolor(title="Choose a color")[1]
    sentence = askstring("Enter Sentence", "Please enter a sentence:")
    
        
    show_image_and_text(sentence,photo_path, color)

button = Button(win, text="Choose Color & Image", command=choose_color_and_image)
button.pack()

def JPEG():
    #image=Image.open(photo_path)
    new_file_path = photo_path.replace('.png', '.jpeg') 
    photo_path.save(new_file_path, 'jpeg')

button = Button(win, text="JPEG_format", command=JPEG)
button.pack()


def save_photo():
    global photo_path
    
    
    if photo_path :
        file_name = filedialog.asksaveasfilename(initialfile="edited_image.jpg", defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        
        if file_name:
            cv2.imwrite(file_name, photo_path)
            messagebox.showinfo("Photo Saved", "Photo saved successfully.")
        else:
            messagebox.showerror("Error", "Please provide a valid file name.")


button = Button(win, text="Save Photo", command=save_photo)
button.pack()



win.geometry('300x300')
win.mainloop()
