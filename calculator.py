from tkinter import *
from termcolor import *
window=Tk()
window.title('python')

text_input = StringVar()
txtDisplay = Entry(window, font=('arial', 20, 'bold'), textvariable=text_input, bd=30,
                   insertwidth=4, bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)

buttons = [
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '0', '+', '-','*','/'
]
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

def btnzarb():
    global operator
    operator = operator + '*'
    text_input.set(operator)

def btnDivision():
    global operator
    operator = operator + '/'
    text_input.set(operator)    

operator = ""
row = 1
col = 0

for button in buttons:
    if button :
        btn = Button(window, text=button, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                     command=lambda button=button: btnClick(button))
        btn.grid(row=row, column=col)
        btn.configure(bg='yellow')
        col += 1
    if col > 3:
        col = 0
        row += 1

        
btnEquals = Button(window, text='=', padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                   command=btnEqualsInput)
btnEquals.grid(row=4, column=2)
btnEquals.configure(text='=',bg='green')
btnClear = Button(window, text='C', padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                  command=btnClearDisplay)
btnClear.grid(row=4, column=1)
btnClear.configure(text='C',bg='red')
btn0 = Button(window, text='0', padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              command=lambda: btnClick(0))
btn0.grid(row=4, column=0)
btn0.configure(bg='blue')
btnzarb = Button(window, text='*', padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                   command=btnzarb)
btnzarb.grid(row=4, column=3)
btnzarb.configure(bg='magenta')
btnDivision = Button(window, text='/', padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                   command=btnDivision)
btnDivision.grid(row=5, column=0)
btnDivision.configure(bg='orange')
#window.geometry('400x400')
window.mainloop()