import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image, ImageTk

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

window = tk.Tk()
window.title("Handwritten Text Recognition")


def recognize_text():
    file_path = file_path_var.get()
    if file_path:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang='eng')
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        print(text)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_var.set(file_path)
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label_image.configure(image=photo)
        label_image.image = photo

file_path_var = tk.StringVar()
label_file_path = tk.Label(window, text="Enter file path:")
label_file_path.pack()
entry_file_path = tk.Entry(window, textvariable=file_path_var)
entry_file_path.pack()

button_open = tk.Button(window, text="Open Image", command=open_file)
button_open.pack()

button_recognize = tk.Button(
    window, text="Recognize Text", command=recognize_text)
button_recognize.pack()

label_image = tk.Label(window)
label_image.pack()

text_box = tk.Text(window, height=10, width=50)
text_box.pack()

window.mainloop()

