import tkinter as tk

kyrgyz_alphabet = "абвгдеёжзийклмнопрстуүфхцчшъыьэюя"

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = (kyrgyz_alphabet.find(char.lower()) + shift) % len(kyrgyz_alphabet)
                result += kyrgyz_alphabet[index].upper()
            else:
                index = (kyrgyz_alphabet.find(char) + shift) % len(kyrgyz_alphabet)
                result += kyrgyz_alphabet[index]
        else:
            result += char
    return result

def encrypt():
    text = text_entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", encrypted_text)

def decrypt():
    text = text_entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, -shift)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", decrypted_text)

# Create the Tkinter window
window = tk.Tk()
window.title("Caesar Cipher for Kyrgyz Alphabet")

# Create labels and entries
text_label = tk.Label(window, text="Enter the text:")
text_label.pack()
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

shift_label = tk.Label(window, text="Enter the shift value:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

# Create buttons
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

# Create result text area
result_label = tk.Label(window, text="Result:")
result_label.pack()
result_text = tk.Text(window, height=10, width=50)
result_text.pack()

# Start the Tkinter event loop
window.mainloop()