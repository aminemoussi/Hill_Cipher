import tkinter as tk
from tkinter import ttk, filedialog
#import Encryption
import key_validation
from open_file import openf
import hill
import cipher_plain_mapping

x = "Please type in the (cipher text to plain text) mapping in this format (c1c2c3c4 : p1p2p3p4) :"

def activate_key():
    key_label.config(state=tk.NORMAL)
    key_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    key_validity.config(state=tk.NORMAL)


def browse_file(file_validation_label, perform_button, result_text):
    txt = openf(file_validation_label, perform_button, result_text)
    if txt:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, txt)
    else:
        result_text.config(state=tk.DISABLED)
        perform_button.config(state=tk.DISABLED)

def op_update(*args):
    operation = operation_var.get()
    print("operation_var: ",operation)
    if operation in ["Encrypt", "Decrypt"]:
        key_label.config(text="Select a valid key (4 letter word): ", state=tk.NORMAL)
        key_entry.config(state=tk.NORMAL)
        submit_button.config(text="submit", state=tk.NORMAL, command = lambda : key_validation.valid_key(get_key(), key_validity, file_label, browse_button, result_text, key_entry), font=('Arial', 7))
        key_validity.config(state=tk.NORMAL)
    else:
        key_label.config(text=x, fg="white", bg="#333")
        #key_entry.config(state=tk.DISABLED)
        submit_button.config(text="submit", command= lambda : cipher_plain_mapping.validate(get_key(), key_validity, file_label, browse_button, key_entry, result_text, perform_button, result_label, submit_button))
        key_validity.config(state=tk.DISABLED)
        file_label.config(state=tk.DISABLED)
        browse_button.config(state=tk.DISABLED)
        key_label.config(state=tk.NORMAL)
        key_entry.config(state=tk.NORMAL)
        submit_button.config(state=tk.NORMAL)
        key_validity.config(state=tk.NORMAL)

def get_key(*args):
    return key_var.get()

def get_op(*args):
    return operation_var.get()

def reset_all():
    operation_var.set("")

    key_label.config(text="Select a valid key (4 letter word): ", state=tk.DISABLED)
    key_var.set("")
    key_entry.config(state=tk.DISABLED)
    submit_button.config(text="submit", state=tk.DISABLED, command=lambda: key_validation.valid_key(get_key(), key_validity, file_label, browse_button,          result_text, key_entry), font=('Arial', 7))

    key_validity.config(text="")

    file_label.config(state=tk.DISABLED)
    browse_button.config(state=tk.DISABLED)

    file_validation_label.config(text="")

    result_label.config(text="Input")
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.1, tk.END)
    result_text.config(state=tk.DISABLED)


    perform_button.config(state=tk.DISABLED, text="Perform Operation", command= lambda : hill.hill(result_label, get_op(), get_key(), result_text, perform_button))


root = tk.Tk()
root.title("Hill Cipher Program")
root.configure(bg="#333")
root.geometry("970x520")

operation_var = tk.StringVar()
operation_var.trace('w', op_update)  #UpToDate value of operation
key_var = tk.StringVar()




# Title label
title_label = tk.Label(root, text="Hill Cipher", font=("Helvetica", 18), fg="white", bg="#333")
title_label.pack(pady=10)

# Operation selection
operation_label = tk.Label(root, text="Select Operation:", fg="white", bg="#333")
operation_label.pack()
operation_combobox = ttk.Combobox(root, textvariable=operation_var, values=["Encrypt", "Decrypt", "Crack"])
operation_combobox.pack()


#key
key_label = tk.Label(root, text="Select a valid key (4 letter word): ", fg="white", bg="#333", state=tk.DISABLED)
key_label.pack()
key_entry = tk.Entry(root, textvariable=key_var, state=tk.DISABLED)
key_entry.pack()





#lambda to execute the command once the button is clicked, not every time the gui is loaded
submit_button = tk.Button(root, text="submit key", command = lambda : key_validation.valid_key(get_key(), key_validity, file_label, browse_button, result_text, key_entry), font=('Arial', 7), state=tk.DISABLED)
submit_button.pack()
key_validity = tk.Label(root,  bg="#333", state=tk.DISABLED)
key_validity.pack()



filler = tk.Label(root,  bg="#333")
filler.pack()


# File selection
file_label = tk.Label(root, text="Select .txt File:", fg="white", bg="#333", state=tk.DISABLED)
file_label.pack()
browse_button = tk.Button(root, text="Browse system files", command = lambda : browse_file(file_validation_label, perform_button, result_text), font=('Arial', 7), state=tk.DISABLED)
browse_button.pack()

#file velidation
file_validation_label = tk.Label(root, bg="#333")
file_validation_label.pack()

# Result display
result_label = tk.Label(root, text="Input:", fg="white", bg="#333")
result_label.pack()
result_text = tk.Text(root, width=50, height=10, bg="#222", fg="white", state=tk.DISABLED)
result_text.pack()

# Perform Operation button
perform_button = ttk.Button(root, text="Perform Operation", command= lambda : hill.hill(result_label, get_op(), get_key(), result_text, perform_button), state=tk.DISABLED)
perform_button.pack(pady=10)


#reset button
clear_button = tk.Button(root, text="Clear_everything", command=reset_all, bg="#85929E")
clear_button.pack()


# Run the application
root.mainloop()