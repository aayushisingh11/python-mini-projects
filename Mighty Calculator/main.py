from tkinter import *
import math

calculator = Tk() # This is to create a basic box
calculator.geometry("412x424")  # this is for the size of the box
calculator.resizable(0, 0)  # this is to prevent from resizing the calculator box
calculator.title("Mighty Calculator")



def button_click(item): #define button for click
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_clear(): #to clear input
    global expression 
    expression = "" 
    input_text.set("")
 

 
def button_equal(): #for output
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
input_text = StringVar()  # 'StringVar()' :It is used to get the instance of input field
 
#frame for the input field
 
input_frame = Frame(calculator, width=312, height=50, bd=0, highlightbackground="deep sky blue", highlightcolor="AntiqueWhite1", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#display box
 
input_field = Entry(input_frame, font=('arial', 15, 'bold'), textvariable=input_text, width=50, bg="AntiqueWhite1", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#frame
 
buttons_frame = Frame(calculator, width=312, height=272.5, bg="gray39")
 
buttons_frame.pack()
 
# first row
 
clear = Button(buttons_frame, text = "Clear", fg = "black", width = 32, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
root2 = Button(buttons_frame, text = "√2", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("1.412")).grid(row = 0, column = 4, padx = 1, pady = 1)

# second row
 
seven = Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(buttons_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

pie = Button(buttons_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("3.14")).grid(row = 1, column = 4, padx = 1, pady = 1)
 
# third row
 
four = Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
log3 = Button(buttons_frame, text = "log(3)", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("0.4771")).grid(row = 2, column = 4, padx = 1, pady = 1)

# fourth row
 
one = Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
log2 = Button(buttons_frame, text = "log(2)", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click("0.3010")).grid(row = 3, column = 4, padx = 1, pady = 1)

# fourth row
 
zero = Button(buttons_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: button_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

log7 = Button(buttons_frame, text = "log(7)", fg = "black", width = 10, height = 3, bd = 0, bg = "plum2", cursor = "hand2", command = lambda: button_equal("0.8450")).grid(row = 4, column = 4, padx = 1, pady = 1)
 
calculator.mainloop()       