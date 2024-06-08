from tkinter import filedialog
import tkinter as tk
import os

def openf(file_validation_label, perform_button, result_text):
    file_path = filedialog.askopenfilename()
    if file_path:

          name, extention = os.path.splitext(file_path)
          if extention == ".txt":

              file_validation_label.config(text="Valid file.", fg="#196F3D ")
              result_text.config(state = tk.NORMAL)
              perform_button.config(state = tk.NORMAL)
              return safe_to_open(file_path)
          else:
              file_validation_label.config(text="InValid file, please select a '.txt' file.", fg="#C0392B ")


    else:
        file_validation_label.config(text="No file was selected.", fg="#626567 ")

    return None


def safe_to_open(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content