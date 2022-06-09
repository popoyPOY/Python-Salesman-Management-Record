from audioop import add
import sqlite3
from tkinter import font, messagebox
from tkinter import *
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import customtkinter
from customtkinter import *
from pyparsing import col

from app import System

customtkinter.set_appearance_mode("system")


class mainGUI(Tk):
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
        
        #for image or logo of the salesman
        self.canvas = CTkCanvas(side_information_frame, height=150, width=200, bg='blue')
        self.canvas.place(x=50, y=10)

        self.salesman_number_label = CTkLabel(side_information_frame, text_font="Roboto 20", text="")
        self.salesman_number_label.place(x=90, y=170)

        self.salesman_name_label = CTkLabel(side_information_frame, text_font="Roboto 20", text="")
        self.salesman_name_label.place(x=90, y=200)

        self.salesman_gender_label = CTkLabel(side_information_frame, text_font="Roboto 20", text="")
        self.salesman_gender_label.place(x=90, y=230)

        self.salesman_age_label = CTkLabel(side_information_frame, text_font="Roboto 20", text="")
        self.salesman_age_label.place(x=90, y=260)

        self.salesman_address_label = CTkLabel(side_information_frame, text_font="Roboto 20", text="")
        self.salesman_address_label.place(x=90, y=300)

        #Frame for treeview_information
        treeview_information_frame = Frame(window, height=400, width=1100, bg='#354259')
        treeview_information_frame.place(x=300, y=100)

        self.treeview_column = ('1', '2', '3', '4', '5')

        self.treeview = Treeview(treeview_information_frame, columns=self.treeview_column, show='headings', height=21)

        self.treeview.heading('1', text="Salesman Number")
        self.treeview.column("#1", width=220)
        self.treeview.heading('2', text="Salesman Name")
        self.treeview.column("#2", width=220)
        self.treeview.heading('3', text="Salesman Gender")
        self.treeview.column("#3", width=220)
        self.treeview.heading('4', text="Salesman Age")
        self.treeview.column("#4", width=220)
        self.treeview.heading('5', text="Salesman Address")
        self.treeview.column("#5", width=220)

        self.treeview.grid()
        self.treeview.bind("<Double-Button-1>", self.showValue)
        
        #Frame for buttons
        button_information_frame = Frame(window, height=100, width=1100, bg='#363062')
        button_information_frame.place(x=300, y=500)


        #Photo image icons
        image_size = 20

        add_photo = ImageTk.PhotoImage(Image.open("assets/icon/add-user.png").resize((image_size, image_size)))
        edit_photo = ImageTk.PhotoImage(Image.open("assets/icon/settings.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open("assets/icon/bell.png").resize((image_size, image_size)))

        add_button = CTkButton(button_information_frame, width=200, height=60, text="Add", image=add_photo, compound="left", command=None, fg_color="#4B8673", hover_color="#5FD068")
        add_button.place(x=50, y=30)

        edit_button = CTkButton(button_information_frame, width=200, height=60, text="Edit", image=edit_photo, compound="left", command=None, fg_color="#47B5FF", hover_color="#1363DF")
        edit_button.place(x=300, y=30)

        delete_button = CTkButton(button_information_frame, width=200, height=60, text="Delete", image=delete_photo, compound="left", command=None, fg_color="#D82148", hover_color="#FF1818")
        delete_button.place(x=550, y=30)


        self.display_salesman_information(self.treeview)

        window.mainloop()
    
    

    #show data in the side_information_frame

    def showValue(self, event):
        global salesman_number

        treeview = self.treeview.focus()
        content = (self.treeview.item(treeview))
        selecteditem = content['values']

        self.salesman_number = selecteditem[0]
        print(self.salesman_number)

        row_id = self.treeview.selection()[0]
        self.setlist = self.treeview.set(row_id)

        self.salesman_number_label['text'] = self.setlist['1']
        self.salesman_name_label['text'] = self.setlist['2']
        self.salesman_gender_label['text'] = self.setlist['3']
        self.salesman_age_label['text'] = self.setlist['4']
        self.salesman_address_label['text'] = self.setlist['5']

    #display data
    def display_salesman_information(self, listbox):
        listbox.delete(*listbox.get_children())

        cursor = sqlite3.connect("SalesFile.db").cursor()

        cursor.execute("SELECT * FROM salesman ORDER BY salesman_no ASC")

        rows = cursor.fetchall()

        for row in rows:
            listbox.insert('', 'end', values=(row[1], row[2],row[3],row[4],row[5]))

app = mainGUI()
app.salesman_gui()