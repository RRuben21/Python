
# hello my name is Ruben Rosa.
# date: 12/01/2022
# class: 2022-Fall: ITSE-1402-V02-Computer Programming 
# The purpose of this program is to create a to do list or a checklist
    #that can also be used to add the total of items that you may need to buy

#Simple Checklist
import re #library used to clean user input data
import tkinter
from tkinter import END, ANCHOR

#Define window

rtotal = 0
root = tkinter.Tk()
root.title('Advanced Budgeting Checklist')
root.iconbitmap('download.ico')#changed to my own icon
root.geometry('400x475')
root.resizable(0,0)

#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = '#0000B9'
button_color = '#C0C0C0'
root.config(bg=root_color)

#Define functions
def add_item():
    """Add an individual item to the listbox"""
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

#my created_function
def add_price():
   # """add a price"""
    sInput = list_entry_price.get() # storing user input to var
    
    my_listbox1.insert(END, list_entry_price.get())  # adding user input to list box
    list_entry_price.delete(0, END)   # clearing input box
    
    global rtotal # declaring var as gobal 
    try:
        c = float(sInput.replace(',', '').replace('$', '')) # input Data validation and cleaning input data and converting string to float
        rtotal = rtotal + c # adding previous total and new item amount
        print (rtotal) # test printing amount
    
        outputTotal.config(text = "Total: $ " + str(rtotal)) # updating running total label
        
    except:
        outputTotal.config(text= "Please enter a Number")
        
    
def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)
    my_listbox1.delete(ANCHOR)


def clear_list():
    """Delete all items from the listbox"""
    my_listbox.delete(0, END)
    my_listbox1.delete(0, END)


def save_list():
    """Save the list to a simple txt file"""
    with open('checklist.txt', 'w') as f:
        #listbox.get() returns a tuple....
        list_tuple = my_listbox.get(0, END)
        
                
        for item in list_tuple:
            #Take proper precautions to include only one \n for formatting purposes
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + "\n")


def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                my_listbox.insert(END, line)
                list_entry_price.insert(END, line)
    except:
        return


#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()


#Input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
#adding entry for price
list_entry_price = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame, text="Add Item", borderwidth=2, font=my_font, bg=button_color, command=add_item)
#adding button to add prices to list
list_add_button_price = tkinter.Button(input_frame, text="Add Price", borderwidth=2, font=my_font, bg=button_color, command=add_price)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_entry_price.grid(row=1, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=3, padx=5, pady=5, ipadx=5)
list_add_button_price.grid(row=1, column=3, padx=5, pady=5, ipadx=5)

#Output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=15, width=20, borderwidth=3, font=my_font, yscrollcommand=my_scrollbar.set)
my_listbox1 = tkinter.Listbox(output_frame, height=15, width=20, borderwidth=3, font=my_font)
#adding another frame using a tkinter Label
outputTotal = tkinter.Label(output_frame,height=1, width=17, borderwidth=3, font=my_font, text=" ") # display running total 

#Link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
#arranging the listbox and running total
my_listbox1.grid(row=0, column=1)
outputTotal.grid(row=8, column=1)
my_scrollbar.grid(row=0, column=2, sticky="NS")

#Button Frame layout
list_remove_button = tkinter.Button(button_frame, text="Remove Item", borderwidth=2, font=my_font, bg=button_color, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text='Clear List', borderwidth=2, font=my_font, bg=button_color, command=clear_list)
save_button = tkinter.Button(button_frame, text='Save List', borderwidth=2, font=my_font, bg=button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

#Open the previous list if available
open_list()

#Run the root window's main loop
root.mainloop()
