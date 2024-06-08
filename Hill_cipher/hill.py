import tkinter as tk
import numpy as np
from key_inverse import key_inverse
import json


alpha_to_num_mapping = {chr(i): i for i in range(256)}



num_to_alpha_mapping = {i: chr(i) for i in range(256)}

print(alpha_to_num_mapping)
print(num_to_alpha_mapping)






def encrypt( key_matrix, txt_blocks):
    cipher_blocks = []
    cipher_txt = ""
    for i in range(txt_blocks.shape[0]):
        print("txt pair value: ", txt_blocks[i])
        x = np.dot(key_matrix, txt_blocks[i]) % 256
        print("Cipher pair: ", x)
        cipher_blocks.append(x)
    cipher_blocks = np.array(cipher_blocks)
    print(cipher_blocks)

    for row in cipher_blocks:

        for val in row:

            cipher_txt = cipher_txt + num_to_alpha_mapping[val]

    return cipher_txt


def decrypt(key_matrix, txt_blocks):
    inverse_key = key_inverse(key_matrix)
    print("rrrrr", inverse_key)
    plain_txt_blocks = []
    print(plain_txt_blocks)
    plain_txt_txt = ""
    for i in range(txt_blocks.shape[0]):
        print(txt_blocks[i])
        x = np.dot(inverse_key, txt_blocks[i]) % 256
        plain_txt_blocks.append(x)
        print(x)

    plain_txt_blocks = np.array(plain_txt_blocks)
    print("plain txt blocs: ", plain_txt_blocks)
    for row in plain_txt_blocks:
        for val in row:
            if num_to_alpha_mapping[val] != "ç":
                x = num_to_alpha_mapping[val]
                plain_txt_txt += x

    print(plain_txt_txt)

    return plain_txt_txt


def get_variable_value():
    with open('cracked_keys.json') as f:
        data = json.load(f)
        # Convert the nested list back to a NumPy array
        return np.array(data['cracked_key'])





def hill(result_label, operation, key, result_text, perform_button):
    result_label.config(text="Result:")
    print(operation)

    txt = result_text.get(1.0, tk.END).rstrip('\n')


    # handling if the length of the text was odd, padding 'ç', MAKE SURE TO IGNORE ç LATER
    if ((len(txt) % 2) != 0):
        txt = txt + 'ç'
    print(len(txt))
    print(txt)


    txt_matrix = []

    #for letter in txt:
     #       print(letter, ": ", mapping.index(letter))
     #       txt_matrix.append(mapping.index(letter))


    txt_matrix = [alpha_to_num_mapping[letter] for letter in txt]
    print(txt_matrix)

    print("Alphabet numerical mapping: ", alpha_to_num_mapping)
    #print("Modified text: ", txt)
    if operation == "Crack":
        key = get_variable_value()
        print("fetched key:", key)



    if isinstance(key, np.ndarray):
        key_matrix = key
        operation = "Decrypt"
    else:
        key_matrix = np.array([
            [ord(key[0]) - 97, ord(key[1]) - 97],
            [ord(key[2]) - 97, ord(key[3]) - 97]
        ])

    txt_matrix = np.array(txt_matrix)
    print("Text turned into a matrix: ", txt_matrix, ". Length =", len(txt_matrix))

    txt_blocks = txt_matrix.reshape(-1, 2)
    print("Reshaped matrix: ", txt_blocks)


    print(operation)

    if operation == "Encrypt":
        cipher_txt = encrypt(key_matrix, txt_blocks)
        result_label.config(text = "Encrypted Cipher text:")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, cipher_txt)
        result_text.config(state = tk.DISABLED)
        perform_button.config(state = tk.DISABLED)
    elif operation == "Decrypt":
        plain_txt = decrypt(key_matrix, txt_blocks)
        result_label.config(text="Decrypted Plain text:")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, plain_txt)
        result_text.config(state=tk.DISABLED)
        perform_button.config(state=tk.DISABLED)


