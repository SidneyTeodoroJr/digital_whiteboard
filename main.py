# Importing dependencies
import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import filedialog
import os

# Create a main window
root = tk.Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = "black"

# Function to track mouse location
def locate_xy(event):
    global current_x, current_y

    current_x = event.x
    current_y = event.y

# Function to add a line drawn by the user
def addline(event):
    global current_x, current_y

    # Create a line on the canvas
    canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(),
                       fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = event.x, event.y

# Function to update pen color
def show_color(new_color):
    global color

    color = new_color

# Function to create a new whiteboard
def new_canvas():
    canvas.delete('all')
    display_palette()

# Function to insert an image on the canvas
def insertimage():
    global filename
    global f_img

    # Open a dialog box to select an image
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetype=(("PNG file", "*.png"), ("All files", "*.txt")))
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(180, 50, image=f_img)
    root.bind("<B3-Motion>", my_callback)

# Callback function to move the image
def my_callback(event):
    global f_img

    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x, event.y, image=f_img)

# Icon
Image_icon = PhotoImage(file="./icon/logo.png")
root.iconphoto(False, Image_icon)

# Side bar
color_box = PhotoImage(file="./icon/color_section.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

eraser = PhotoImage(file="./icon/eraser.png")
Button(root, image=eraser, bg="#f2f3f5", command=new_canvas).place(x=30, y=400)

importmage = PhotoImage(file="./icon/addimage.png")
Button(root, image=importmage, bg="#fff", command=insertimage).place(x=30, y=450)

# Colors
colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

# Function to display the color palette
def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill="white")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

    id = colors.create_rectangle((10, 40, 30, 60), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 70, 30, 90), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10, 100, 30, 120), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10, 130, 30, 150), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 160, 30, 180), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 190, 30, 210), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

display_palette()

# Main screen
canvas = Canvas(root, width=930, height=500, background="#fff", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)

# Slider
current_value = tk.DoubleVar()

# Function to get the current value of the slider
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()