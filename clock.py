from tkinter import *
import time
import datetime
import pytz
window=Tk()
window.title('clock digital')
window.geometry('600x600')
clock_var = StringVar()
def Time():
    h_m_s_a_o_p=time.strftime('%I : %M : %S %p')
    clock=h_m_s_a_o_p
    label.config(text=clock)
    label.after(1000,Time)

    day=time.strftime("%A")
    year=time.strftime("%Y")
    month=time.strftime("%M")
    D_M_Y=year+'|'+month+'|'+day
    label1.config(text=D_M_Y)
    zone=time.strftime("%Z")
    zome = pytz.timezone('Iran/Tehran')
    datetime_London = datetime.now(zone)

    C_C_M=zone+zome+datetime_London
    label2.config(text=C_C_M)

label=Label(window,text="",font=('Arial',72),fg='white',bg='magenta')
label.pack()
label1=Label(window,text="",font=('Arial',72),fg='white',bg='green')
label1.pack()
label2=Label(window,text="",font=('Arial',72),fg='white',bg='blue')
label2.pack()
Time()
window.mainloop()