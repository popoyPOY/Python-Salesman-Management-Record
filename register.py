import sqlite3
from customtkinter import *
from tkinter import *
from PIL import ImageTk, Image



root = CTk()
root.geometry("500x300")
root.title("Coanime Co. | Sign Up")
root.resizable(0, 0)

USERNAME = StringVar()
PASSWORD = StringVar()

def register():
    connection = sqlite3.connect("SalesFile.db")
    
    conn = connection.cursor()

    connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", (USERNAME.get(), PASSWORD.get()))
    connection.commit()

welcome_label = CTkLabel(root, text="Sign Up", text_font=("Roboto 30 bold"))
welcome_label.place(x=180, y=30)

frame = CTkFrame(root, width=300, height=300, fg_color="#51557E")
frame.place(x=100, y=100)

username_label = CTkLabel(frame, text="Username: ", text_font=("Roboto 15 bold"))
username_label.grid(padx=10, pady=10, row=1, column=1)

username_entry = CTkEntry(frame, text_font=("Roboto 15"), width=150, textvariable=USERNAME)
username_entry.grid(padx=10, pady=10, row=1, column=2)

username_label = CTkLabel(frame, text="Password: ", text_font=("Roboto 15 bold"))
username_label.grid(padx=10, pady=10, row=2, column=1)

pasword_entry = CTkEntry(frame, text_font=("Roboto 15"), width=150, show="*", textvariable=PASSWORD)
pasword_entry.grid(padx=10, pady=10, row=2, column=2)

image_size = 20
signup_image = ImageTk.PhotoImage(Image.open(
            "assets/signup.png").resize((image_size, image_size)))

button = CTkButton(root, text="Sign Up", image=signup_image, compound=LEFT, width=100, height=50, hover_color=("#C7D36F"), fg_color="#9EB23B", text_color="black", command=register)
button.place(x=200, y=230)

root.mainloop()