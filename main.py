import sqlite3
from tkinter import font, messagebox
from tkinter import *
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import customtkinter
from customtkinter import *
from matplotlib import image
from app import System

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

        information_dashboard_frame = CTkFrame(window, height=100, width=1400, fg_color=("#209ce8","#0c3d5c"))
        information_dashboard_frame.place(x=0.1, y=0.1)

        image_label = Image.open("assets/logo3.png").resize((100, 100), Image.ANTIALIAS)
        resize_image = ImageTk.PhotoImage(image_label)

        logo_label = CTkLabel(information_dashboard_frame, image=resize_image,relief=GROOVE, borderwidth=0, bg="#0c3d5c")
        logo_label.place(x=0.1, y=0.1)

        company_label = CTkLabel(information_dashboard_frame, text="Canime Co. | Sales Management Dashboard", text_font=("Gluten", 30), bg_color="#0c3d5c", text_color=('#000000', '#faf7f7'))
        company_label.place(x=200, y=25)

        #Frame for sidebar_information
        side_information_frame = Frame(window, height=500, width=300)
        side_information_frame.place(x=0.1, y=100)
        
        #for image or logo of the salesman
        self.canvas = CTkCanvas(window, height=150, width=200, bg='blue')
        self.canvas.place(x=40, y=100)


        self.salesman_number_Entry = CTkEntry(side_information_frame, fg="#fcfcfc", bg=self.color, width=200, text_font="Gluten 20", state="disabled")
        self.salesman_number_Entry.place(x=40, y=170)

        self.salesman_name_Entry = CTkEntry(side_information_frame, fg="#fcfcfc", bg=self.color, width=200, text_font="Gluten 20", state="disabled")
        self.salesman_name_Entry.place(x=40, y=220)
        
        self.salesman_gender_Entry = CTkEntry(side_information_frame, fg="#fcfcfc", bg=self.color, width=200, text_font="Gluten 20", state="disabled")
        self.salesman_gender_Entry.place(x=40, y=270)

        self.salesman_age_Entry = CTkEntry(side_information_frame, fg="#fcfcfc", bg=self.color, width=200, text_font="Gluten 20", state="disabled")
        self.salesman_age_Entry.place(x=40, y=320)

        self.salesman_address_Entry = CTkEntry(side_information_frame, fg="#fcfcfc", bg=self.color, width=200, text_font="Gluten 20", state="disabled")
        self.salesman_address_Entry.place(x=40, y=370)

        

        #Frame for treeview_information
        treeview_information_frame = Frame(window, height=400, width=1100)
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
        button_information_frame = Frame(window, height=100, width=1100)
        button_information_frame.place(x=300, y=500)


        #Photo image icons
        image_size = 20

        add_photo = ImageTk.PhotoImage(Image.open("assets/icon/add-user.png").resize((image_size, image_size)))
        edit_photo = ImageTk.PhotoImage(Image.open("assets/icon/settings.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open("assets/icon/bell.png").resize((image_size, image_size)))

        add_button = CTkButton(button_information_frame, width=200, height=60, text="Add", image=add_photo, compound="left", command=self.create_salesman, fg_color="#4B8673", hover_color="#5FD068")
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
        #print(self.salesman_number)

        row_id = self.treeview.selection()[0]
        self.setlist = self.treeview.set(row_id)

        self.salesman_number_Entry.config(state="normal")
        self.salesman_name_Entry.config(state="normal")
        self.salesman_gender_Entry.config(state="normal")
        self.salesman_age_Entry.config(state="normal")
        self.salesman_address_Entry.config(state="normal")


        self.salesman_number_Entry.delete(0, END)
        self.salesman_name_Entry.delete(0, END)
        self.salesman_gender_Entry.delete(0, END)
        self.salesman_age_Entry.delete(0, END)
        self.salesman_address_Entry.delete(0, END)

        self.salesman_number_Entry.insert(0, self.setlist['1'])
        self.salesman_name_Entry.insert(0, self.setlist['2'])
        self.salesman_gender_Entry.insert(0, self.setlist['3'])
        self.salesman_age_Entry.insert(0, self.setlist['4'])
        self.salesman_address_Entry.insert(0, self.setlist['5'])

        self.salesman_number_Entry.config(state="disabled")
        self.salesman_name_Entry.config(state="disabled")
        self.salesman_gender_Entry.config(state="disabled")
        self.salesman_age_Entry.config(state="disabled")
        self.salesman_address_Entry.config(state="disabled")


    #display data
    def display_salesman_information(self, listbox):
        listbox.delete(*listbox.get_children())

        cursor = sqlite3.connect("SalesFile.db").cursor()

        cursor.execute("SELECT * FROM salesman ORDER BY salesman_no ASC")

        rows = cursor.fetchall()

        for row in rows:
            listbox.insert('', 'end', values=(row[1], row[2],row[3],row[4],row[5]))


    def create_salesman(self):
        create_window = Toplevel()
        create_window.title("Canime Co. | Edit Salesman Information")
        create_window.geometry("400x600")

        #Frame for widgets
        self.sales_information_create_frame = CTkFrame(create_window, height=500, width=300, fg_color="#B7CADB")
        self.sales_information_create_frame.place(x=60)

        self.create_label = CTkLabel(self.sales_information_create_frame, text="Create Salesman", text_font="Gluten 20")
        self.create_label.grid(row=1, column=1, padx=10, pady=50)

        self.create_label_name = CTkLabel(self.sales_information_create_frame, text="Salesman Name: ", text_font="Gluten 20")
        self.create_label_name.grid(row=2, column=1)

        self.create_Entry_name = CTkEntry(self.sales_information_create_frame, text_font="Gluten 20")
        self.create_Entry_name.grid(row=2, column=2)



        create_window.mainloop()

    def edit_information(self):
        window = Toplevel()
        window.title("Canime Co. | Edit Salesman Information")
        window.geometry("400x600")

app = mainGUI()
app.create_salesman()