from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("system")


class mainGUI(CTk):
    def __init__(self):
        super().__init__()
        self.title("Canime Co. Management System | Login")
        self.geometry("900x520")
        self.fgcolor = "#DFF6FF"
        self.bgcolor = "#06283D"
        self.color = "#3C2C3E"
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_height()
        
        self.resizable(False, False)

        #Frame1-------------
        self.background_image = Image.open("assets/background.jpg")
        self.resized_image = self.background_image.resize((400, 520), Image.ANTIALIAS)
        self.frame1=Frame(self, width=400, height=520, bg="Cyan")
        self.frame1.place(x=0.1, y=0.1)

        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.background_label = Label(self.frame1, image=self.new_image, relief=GROOVE, borderwidth=0)
        self.background_label.pack()

        self.login_form = CTkFrame(self, bg=self.bgcolor)
        self.login_form.place(x=500, y=180)

        self.welcome_label = CTkLabel(self, text="Canime Co.", text_font=("Gluten", 50), fg="#47B5FF", bg=self.bgcolor)
        self.welcome_label.place(x=450, y=30)
        
        #self.label_image = PhotoImage(file="img0.png")
        
        self.username_label = CTkLabel(self.login_form, text="Username", text_font=("Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=1)

        self.username_entry = CTkEntry(self.login_form, fg="#FF06B7", bg=self.color, width=150, text_font="Gluten")
        self.username_entry.grid(row=1, padx=10, pady=10, column=2)

        self.username_label = CTkLabel(self.login_form, text="Password", text_font=("Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=2)

        self.password_entry = CTkEntry(self.login_form, bg=self.color, fg="#FF06B7", show="*", width=150, text_font="Gluten")
        self.password_entry.grid(row=2, padx=10, pady=10, column=2)

        self.login_button = CTkButton(self, text="Login", text_font=("Gluten", 20), width=20 ,command=self.Login)
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
        window = Toplevel()
        
        window.resizable(0,0)
        window.geometry("1400x600")
        window.title("Canime Co. | Sales Management Dashboard")
        window.config()

        information_dashboard_frame = CTkFrame(window, height=100, width=1400, fg_color="#0c3d5c")
        information_dashboard_frame.place(x=0.1, y=0.1)

        image_label = Image.open("assets/logo3.png").resize((100, 100), Image.ANTIALIAS)
        resize_image = ImageTk.PhotoImage(image_label)

        logo_label = Label(information_dashboard_frame, image=resize_image,relief=GROOVE, borderwidth=0, bg="#0c3d5c")
        logo_label.place(x=0.1, y=0.1)

        company_label = Label(information_dashboard_frame, text="Canime Co. | Sales Management Dashboard", font=("Gluten", 30), bg="#0c3d5c")
        company_label.place(x=200, y=25)

        #Frame for sidebar_information
        side_information_frame = Frame(window, height=500, width=300, bg='#293462')
        side_information_frame.place(x=0.1, y=100)


        #Frame for treeview_information
        trevieww_information_frame = Frame(window, height=400, width=1100, bg='#354259')
        trevieww_information_frame.place(x=300, y=100)

        #Frame for buttons
        button_information_frame = Frame(window, height=100, width=1100, bg='#363062')
        button_information_frame.place(x=300, y=500)

        window.mainloop()
app = mainGUI()
app.salesman_gui()