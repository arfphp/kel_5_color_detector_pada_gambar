import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# Fungsi untuk mendeteksi warna dalam gambar
def detect_colors(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    colors, counts = np.unique(image.reshape(-1, 3), axis=0, return_counts=True)
    sorted_colors = colors[np.argsort(-counts)]

    return sorted_colors

# Fungsi saat tombol "Deteksi" ditekan
def detect_button_pressed():
    file_path = filedialog.askopenfilename()
    if file_path:
        colors = detect_colors(file_path)
        color_listbox.delete(0, tk.END)
        
        for color in colors:
            color_hex = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            color_listbox.insert(tk.END, color_hex)
    
        display_image(file_path)

# Fungsi untuk menampilkan gambar pada GUI
def display_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Main program GUI
app = tk.Tk()
app.title("Pendeteksi Warna dalam Gambar")

detect_button = tk.Button(app, text="Pilih Gambar", command=detect_button_pressed)
detect_button.pack(pady=10)

color_listbox = tk.Listbox(app)
color_listbox.pack()

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
