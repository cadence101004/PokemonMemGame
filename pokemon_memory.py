import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Setup window
root = tk.Tk()
root.title("Pokémon Memory Match")
root.configure(bg="#fff0f5")  # light lavender-pink
root.geometry("500x550")

# Load & double the PNG filenames
image_dir = "images"
original_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]
card_files = original_files[:8] * 2  # 8 unique x 2 = 16 total
random.shuffle(card_files)

# Game state
flipped = []
matched = set()
buttons = []
images = []

# Load images
for file in card_files:
    path = os.path.join(image_dir, file)
    img = Image.open(path).resize((100, 100))
    images.append(ImageTk.PhotoImage(img))

# Back image (pink square)
back_img = ImageTk.PhotoImage(Image.new("RGB", (100, 100), "#fbb1bd")) 

def check_match():
    if len(flipped) == 2:
        i, j = flipped
        if card_files[i] == card_files[j]:
            buttons[i].config(state="disabled")
            buttons[j].config(state="disabled")
            matched.update([i, j])
            if len(matched) == 16:
                messagebox.showinfo("Victory!", "You matched all the Pokémon! 🎉")
        else:
            buttons[i].config(image=back_img)
            buttons[j].config(image=back_img)
        flipped.clear()

def flip_card(index):
    if index in flipped or index in matched or len(flipped) == 2:
        return
    buttons[index].config(image=images[index])
    flipped.append(index)
    root.after(700, check_match)

def reset_game():
    global card_files, images, flipped, matched
    flipped.clear()
    matched.clear()
    card_files = original_files[:8] * 2
    random.shuffle(card_files)
    images.clear()
    for i, file in enumerate(card_files):
        path = os.path.join(image_dir, file)
        img = Image.open(path).resize((100, 100))
        images.append(ImageTk.PhotoImage(img))
        buttons[i].config(image=back_img, state="normal")

# Create 4x4 grid of buttons
for i in range(16):
    btn = tk.Button(root, image=back_img, command=lambda i=i: flip_card(i), bd=0)
    btn.grid(row=i//4, column=i%4, padx=10, pady=10)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(
    root,
    text="Reset",
    command=reset_game,
    bg="#fbb1bd",
    activebackground="#ffc0cb",
    fg="#fbb1bd",
    font=("Comic Sans MS", 14, "bold"),
    relief="raised",
    bd=3
)

reset_btn.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
