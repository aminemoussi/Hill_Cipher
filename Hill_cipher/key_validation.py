import tkinter as tk
import numpy as np
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def valid_key(key, inputs_label, file_label, browse_button, result_text, key_entry):
    if key:
        if len(key) == 4:
            print("key value: ",key)
            if validated(key, inputs_label):
                inputs_label.config(text = "Valid key", fg = "#196F3D ")
                file_label.config(state=tk.NORMAL)
                browse_button.config(state=tk.NORMAL)
                result_text.config(state=tk.NORMAL)
                key_entry.config(state=tk.DISABLED)

            else:
                #inputs_label.config(text="InValid key.", fg="#C0392B ")
                key_entry.delete(0, tk.END)
        else:
            inputs_label.config(text="InValid key, 4 letters.", fg="#C0392B ")
            key_entry.delete(0, tk.END)

    else:
        inputs_label.config(text="InValid key.", fg="#C0392B ")

def validated(key, inputs_label):
    valid = True
    key_matrix = np.array([
        [ord(key[0]) - 97, ord(key[1]) - 97],
        [ord(key[2]) - 97, ord(key[3]) - 97]
    ])
    det = (key_matrix[0, 0] * key_matrix[1, 1]) - (key_matrix[0, 1] * key_matrix[1, 0])
    if (det == 0) or (math.gcd(256, det) != 1):
        print("Invalid key: det = "+str(det)+", gcd(256,det) = "+ str(math.gcd(256, det)))
        x = "Invalid key: det = "+str(det)+", gcd(256,det) = "+ str(math.gcd(256, det))
        inputs_label.config(text=x, fg="#C0392B ")
        valid = False

    print("Key matrix:", key_matrix)
    return valid