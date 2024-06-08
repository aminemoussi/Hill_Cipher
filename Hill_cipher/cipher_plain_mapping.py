import json

import hill
import numpy as np
import math
import key_inverse
import tkinter as tk


alpha_to_num_mapping = {chr(i): i for i in range(256)}

def update_variable_value(new_value):
    # Convert the NumPy array to a nested list
    new_value_list = new_value.tolist()

    # Update the JSON file with the new value
    with open('cracked_keys.json', 'r+') as f:
        data = json.load(f)
        data['cracked_key'] = new_value_list
        f.seek(0)
        json.dump(data, f, indent=4)


def validate(txt, key_validity, file_label, browse_button, key_entry, result_text, perform_button, result_label, submit_button):
    txt = txt[:11]
    print(txt)


    if len(str(txt)) == 11:

        if txt[4] == ' ' and txt[5] == ':' and txt[6] == ' ':

            print("Valid cracking format.")

            cipher = txt[:4]
            plain = txt[7:]

            cipher = np.array([
                [alpha_to_num_mapping[cipher[0]], alpha_to_num_mapping[cipher[2]]],
                [alpha_to_num_mapping[cipher[1]], alpha_to_num_mapping[cipher[3]]]
            ])
            plain = np.array([
                [alpha_to_num_mapping[plain[0]], alpha_to_num_mapping[plain[2]]],
                    [alpha_to_num_mapping[plain[1]], alpha_to_num_mapping[plain[3]]]
            ])

            det = (plain[0, 0] * plain[1, 1]) - (plain[0, 1] * plain[1, 0])
            if (det != 0) and (math.gcd(det, 256) == 1):
                print(str(det), ", ", str(math.gcd(det, 256)), ".")
                print("Combination Accepted")
                browse_button.config(state=tk.NORMAL)
                file_label.config(state=tk.NORMAL)
                key_entry.config(state=tk.DISABLED)
                submit_button.config(state=tk.DISABLED)
                result_text.config(state=tk.NORMAL)
                plain = key_inverse.key_inverse(plain)
                cracked_key = np.dot(cipher, plain) % 256
                key_validity.config(text=("The key value is: " + str(cracked_key) + " ."), fg="green")

                update_variable_value(cracked_key)


            else:
                key_validity.config(
                    text="Could not extract the key out of the given combination, try a different combination.",
                    fg="#C0392B")
                key_entry.insert(tk.END, "")
                print(str(det), ", ", str(math.gcd(det, 256)), ".")



        else:
            key_validity.config(text = "Invalid mapping (c1c2c3c4 : p1p2p3p4)", fg = "#C0392B")
    else:
        key_validity.config(text=("Invalid mapping (c1c2c3c4 : p1p2p3p4)"+ str(len(txt))), fg = "#C0392B")







