import ast
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import numpy as np
def help_info():
    h = messagebox.showinfo("Help", "This program is used to calculate singular value decomposition.\n"
                                    "\nEnter a matrix or array into the top input field and have it printed to the 'Results' output or, save it to a file.")

def printOut():
    url = inputTextbox.get(1.0, "end-1c")
    A = np.array(ast.literal_eval(url))
    x,y,z = np.linalg.svd(A)
    outputTextbox.insert(1.0, x)
    outputTextbox.insert(1.0, y)
    outputTextbox.insert(1.0, z)
    return(url)

# save output to a file -- works
def save_as():
    save_output = filedialog.asksaveasfile()


# quit the program -- works
def quit_program():
    are_you_sure = messagebox.askquestion("Quit", "Are you sure?")
    if are_you_sure == 'yes':
        mainWindow.destroy()
    else:
        mainWindow.mainloop()


# Create mainWindow, not resizeable
mainWindow = tk.Tk()
mainWindow.title("计算奇异值分解")
mainWindow.geometry("585x355-730-400")
mainWindow.resizable(False, False)

# label for user input
input_label = tk.Label(mainWindow, text="Enter a matrix or array", font="Arial 9")
input_label.place(x=7, y=5)

# input textbox
inputTextbox = tk.Text(mainWindow, width=70, height=8)
inputTextbox.place(x=10, y=25)

# label for output
output_label = tk.Label(mainWindow, text="Results", font="Arial 9")
output_label.place(x=7, y=165)

# results textbox
outputTextbox = tk.Text(mainWindow, width=70, height=8)
outputTextbox.place(x=10, y=185)

# help button
help_button = tk.Button(mainWindow, text="Help", padx=20, pady=0, command=help_info)
help_button.place(x=100, y=325)

# print button
print_button = tk.Button(mainWindow, text="Print", padx=20, pady=0, command=printOut)
print_button.place(x=200, y=325)

# save button
save_button = tk.Button(mainWindow, text="Save", padx=20, pady=0, command=save_as)
save_button.place(x=300, y=325)

# exit button
exit_button = tk.Button(mainWindow, text="Exit", padx=20, pady=0, command=quit_program)
exit_button.place(x=400, y=325)

# run the program
mainWindow.mainloop()