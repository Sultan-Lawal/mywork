from tkinter import *
from tkinter.messagebox import *


def click(value):
    display.insert(END, value)
    
def clear():
    display.delete(0, END)    
def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(END, current[:-1])

def calc_result():
    try:
        expression = display.get()
        result = eval(expression)

        clear()
        click(str(result))

    except ZeroDivisionError:
        clear()
        click('Cannot divide by zero')    
    
    except Exception:
        clear()
        click('Error')
        # showerror(title = "Alert",
        #         message = "Error")

root = Tk()
root.title("Calculator")
root.geometry('400x500')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)


display = Entry(root, font=('Arial', 20), justify='right')


bttn1 = Button(root, text='1', font=('Verdana', 18), width=5, command=lambda: click('1'))
bttn2 = Button(root, text='2', font=('Verdana', 18), width=5, command=lambda: click('2'))
bttn3 = Button(root, text='3', font=('Verdana', 18), width=5, command=lambda: click('3'))
bttn4 = Button(root, text='4', font=('Verdana', 18), width=5, command=lambda: click('4'))
bttn5 = Button(root, text='5', font=('Verdana', 18), width=5, command=lambda: click('5'))
bttn6 = Button(root, text='6', font=('Verdana', 18), width=5, command=lambda: click('6'))
bttn7 = Button(root, text='7', font=('Verdana', 18), width=5, command=lambda: click('7'))
bttn8 = Button(root, text='8', font=('Verdana', 18), width=5, command=lambda: click('8'))
bttn9 = Button(root, text='9', font=('Verdana', 18), width=5, command=lambda: click('9'))
bttn10 = Button(root, text='0', font=('Verdana', 18), width=5, command=lambda: click('0'))
bttn11 = Button(root, text='+', font=('Verdana', 18), width=5, command=lambda: click('+'))
bttn12 = Button(root, text='-', font=('Verdana', 18), width=5, command=lambda: click('-'))
bttn13 = Button(root, text='*', font=('Verdana', 18), width=5, command=lambda: click('*'))
bttn14 = Button(root, text='/', font=('Verdana', 18), width=5, command=lambda: click('/'))
bttn15 = Button(root, text='.', font=('Verdana', 18), width=5, command=lambda: click('.'))
calc_button = Button(root, text='=', font=('Verdana', 18), width=5,
command=calc_result)
clr_button = Button(text='C', font=('Verdana', 18), width=5, command=clear)
del_button = Button(text='⌫', font=('Verdana', 18), width=5, command=backspace)




display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')
bttn7.grid(row=1, column=0, padx=5, pady=5)
bttn8.grid(row=1, column=1, padx=5, pady=5)
bttn9.grid(row=1, column=2, padx=5, pady=5)
bttn14.grid(row=1, column=3, padx=5, pady=5)
bttn4.grid(row=2, column=0, padx=5, pady=5)
bttn5.grid(row=2, column=1, padx=5, pady=5)
bttn6.grid(row=2, column=2, padx=5, pady=5)
bttn13.grid(row=2, column=3, padx=5, pady=5)
bttn1.grid(row=3, column=0, padx=5, pady=5)
bttn2.grid(row=3, column=1, padx=5, pady=5)
bttn3.grid(row=3, column=2, padx=5, pady=5)
bttn12.grid(row=3, column=3, padx=5, pady=5)
bttn10.grid(row=4, column=0, padx=5, pady=5)
bttn15.grid(row=4, column=1, padx=5, pady=5)
calc_button.grid(row=4, column=2, padx=5, pady=5)
bttn11.grid(row=4, column=3, padx=5, pady=5)
clr_button.grid(row=5, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
del_button.grid(row=5, column=2, columnspan=2, sticky='ew', padx=5, pady=5)





mainloop()