from tkinter import messagebox
from app import *
from tkinter import *


class mainGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Canime Co. Management System | Login")
        self.geometry("900x500")
        self.config(bg="#BDF2D5")
        self.fgcolor = "#4B5D67"
        self.bgcolor = "#BDF2D5"
        self.color = "#3C2C3E"

        #Frame1-------------
        self.frame1=Frame(self, width=400, height=500, bg="Cyan")
        self.frame1.place(x=10, y=10)

        self.login_form = Frame(self, bg=self.bgcolor)
        self.login_form.place(x=500, y=180)

        self.welcome_label = Label(self, text="Canime Co.", font=("Gluten", 50), fg=self.fgcolor, bg=self.bgcolor)
        self.welcome_label.place(x=450, y=30)
        
        self.label_image = PhotoImage(file="img0.png")
        
        self.username_label = Label(self.login_form, text="Username", font=("Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=1)

        self.username_entry = Entry(self.login_form, font=("Gluten", 14), fg="#FF06B7", bg=self.color)
        self.username_entry.grid(row=1, padx=10, pady=10, column=2)

        self.username_label = Label(self.login_form, text="Password", font=("Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=2)

        self.password_entry = Entry(self.login_form, font=("Gluten", 14), bg=self.color, fg="#FF06B7", show="*")
        self.password_entry.grid(row=2, padx=10, pady=10, column=2)

        self.login_button = Button(self, text="Login", font=("Gluten", 20), width=13 ,command=self.Login, fg=self.fgcolor)
        self.login_button.place(x=570, y=300)
    
    def Login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            messagebox.showinfo(title="Canime Co. | Message", message="Canime Co. | Login Successful")
            self.salesman_gui()
        
        elif self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror(title="Canime Co. | Message", message="Canime Co. | No credentials provided!")
        else:
            messagebox.showerror(title="Canime Co. | Message", message="Canime Co. | Login Failed, invalid username or password")
    

    def salesman_gui(self):
        window = Tk()

        window.geometry("1500x600")

        

        window.mainloop()
app = mainGUI()
app.salesman_gui()