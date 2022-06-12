from calendar import c
from email import message
import sqlite3
from tkinter import font, messagebox
from tkinter import *
from tkinter.ttk import Treeview
import tkinter.ttk as ttk
from tokenize import String
from turtle import bgcolor
from PIL import ImageTk, Image
import customtkinter
from customtkinter import *
from app import Sales_system, System


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
        photo = PhotoImage(file="assets/logo3.png")
        self.iconphoto(False, photo)
        self.resizable(False, False)
        #self.system = System()

        # Frame1-------------
        self.background_image = Image.open("assets/background.jpg")
        self.resized_image = self.background_image.resize(
            (400, 520), Image.ANTIALIAS)
        self.frame1 = Frame(self, width=400, height=520, bg="Cyan")
        self.frame1.place(x=0.1, y=0.1)

        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.background_label = Label(
            self.frame1, image=self.new_image, relief=GROOVE, borderwidth=0)
        self.background_label.pack()

        self.login_form = CTkFrame(self, bg=self.bgcolor)
        self.login_form.place(x=500, y=180)

        self.welcome_label = CTkLabel(self, text="Canime Co.", text_font=(
            "Gluten", 50), fg="#47B5FF", bg=self.bgcolor)
        self.welcome_label.place(x=450, y=30)

        #self.label_image = PhotoImage(file="img0.png")

        self.username_label = CTkLabel(self.login_form, text="Username", text_font=(
            "Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=1)

        self.username_entry = CTkEntry(
            self.login_form, fg="#FF06B7", bg=self.color, width=150, text_font="Gluten")
        self.username_entry.grid(row=1, padx=10, pady=10, column=2)

        self.username_label = CTkLabel(self.login_form, text="Password", text_font=(
            "Gluten", 13), bg=self.bgcolor, fg=self.fgcolor)
        self.username_label.grid(row=2)

        self.password_entry = CTkEntry(
            self.login_form, bg=self.color, fg="#FF06B7", show="*", width=150, text_font="Gluten")
        self.password_entry.grid(row=2, padx=10, pady=10, column=2)

        self.login_button = CTkButton(self, text="Login", text_font=(
            "Gluten", 20), width=20, command=self.Login)
        self.login_button.place(x=570, y=300)

    def Login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            messagebox.showinfo(title="Canime Co. | Message",
                                message="Canime Co. | Login Successful")
            self.withdraw()
            self.salesman_gui()

        elif self.username_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror(title="Canime Co. | Message",
                                 message="Canime Co. | No credentials provided!")
        else:
            messagebox.showerror(title="Canime Co. | Message",
                                 message="Canime Co. | Login Failed, invalid username or password")

    def salesman_gui(self):
        window = CTkToplevel()

        window.resizable(0, 0)
        window.geometry("1400x600")
        window.title("Canime Co. | Sales Management Dashboard")
        window.config()
        photo = PhotoImage(file="assets/logo3.png") 
        window.iconphoto(False, photo)

        #self.system = None
        self.SEARCH = StringVar()
        #filter search data

        # VARIABLES
        self.SALESMAN_NUMBER = IntVar()
        self.SALESMAN_NAME = StringVar()
        self.SALESMAN_GENDER = StringVar()
        self.SALESMAN_AGE = IntVar()
        self.SALESMAN_ADDRESS = StringVar()

        self.system = System(self.SALESMAN_NUMBER.get(), self.SALESMAN_NAME.get(
        ), self.SALESMAN_GENDER.get(), self.SALESMAN_AGE.get(), self.SALESMAN_ADDRESS.get())

        information_dashboard_frame = CTkFrame(
            window, height=100, width=1400, fg_color=("#209ce8", "#0c3d5c"))
        information_dashboard_frame.place(x=0.1, y=0.1)

        image = Image.open(
            "assets/icon/search.png").resize((30, 30), Image.ANTIALIAS)
        search_image = ImageTk.PhotoImage(image)

        logo_label = CTkLabel(information_dashboard_frame, image=search_image,
                              relief=GROOVE, borderwidth=0, bg="#0c3d5c")
        logo_label.place(x=910, y=50)

        search_entry = Entry(information_dashboard_frame, textvariable=self.SEARCH)
        search_entry.place(x=1000, y=50)
        search_entry.bind("<Key>", self.search)

        image_label = Image.open(
            "assets/logo3.png").resize((100, 100), Image.ANTIALIAS)
        resize_image = ImageTk.PhotoImage(image_label)

        logo_label = CTkLabel(information_dashboard_frame, image=resize_image,
                              relief=GROOVE, borderwidth=0, bg="#0c3d5c")
        logo_label.place(x=0.1, y=0.1)

        company_label = CTkLabel(information_dashboard_frame, text="Canime Co. | Sales Management Dashboard", text_font=(
            "Gluten", 30), bg_color="#0c3d5c", text_color=('#000000', '#faf7f7'))
        company_label.place(x=200, y=25)

        # Frame for sidebar_information
        self.side_information_frame = Frame(window, height=500, width=300)
        self.side_information_frame.place(x=0.1, y=100)

        # for image or logo of the salesman
        image_label = Image.open(
            "assets/icon/user.png").resize((100, 100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image_label)
        self.canvas = CTkLabel(self.side_information_frame, image=image)
        self.canvas.place(x=85, y=50)

        self.salesman_number_Entry = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                              width=200, text_font="Gluten 20", state="disabled", textvariable=self.SALESMAN_NUMBER)
        self.salesman_number_Entry.place(x=40, y=170)

        self.salesman_name_Entry = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                            width=200, text_font="Gluten 20", state="disabled", textvariable=self.SALESMAN_NAME)
        self.salesman_name_Entry.place(x=40, y=220)

        self.salesman_gender_Entry = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                              width=200, text_font="Gluten 20", state="disabled", textvariable=self.SALESMAN_GENDER)
        self.salesman_gender_Entry.place(x=40, y=270)

        self.salesman_age_Entry = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                           width=200, text_font="Gluten 20", state="disabled", textvariable=self.SALESMAN_AGE)
        self.salesman_age_Entry.place(x=40, y=320)

        self.salesman_address_Entry = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                               width=200, text_font="Gluten 20", state="disabled", textvariable=self.SALESMAN_ADDRESS)
        self.salesman_address_Entry.place(x=40, y=370)

        # Frame for treeview_information
        treeview_information_frame = Frame(window, height=400, width=1100)
        treeview_information_frame.place(x=300, y=100)

        self.treeview_column = ('1', '2', '3', '4', '5')

        self.treeview = Treeview(
            treeview_information_frame, columns=self.treeview_column, show='headings', height=21)

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

        # Frame for buttons
        button_information_frame = Frame(window, height=100, width=1100)
        button_information_frame.place(x=300, y=500)

        # Photo image icons
        image_size = 20

        add_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/add-user.png").resize((image_size, image_size)))
        edit_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/settings.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/bell.png").resize((image_size, image_size)))
        sales_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/shop.png").resize((image_size, image_size)))

        add_button = CTkButton(button_information_frame, width=200, height=60, text="Add", image=add_photo,
                               compound="left", command=self.create_salesman, fg_color="#4B8673", hover_color="#5FD068")
        add_button.place(x=50, y=30)

        edit_button = CTkButton(button_information_frame, width=200, height=60, text="Edit", image=edit_photo,
                                compound="left", command=self.edit_information, fg_color="#47B5FF", hover_color="#1363DF")
        edit_button.place(x=300, y=30)

        delete_button = CTkButton(button_information_frame, width=200, height=60, text="Delete", image=delete_photo,
                                  compound="left", command=self.delete_information, fg_color="#D82148", hover_color="#FF1818")
        delete_button.place(x=550, y=30)

        self.sales_button = CTkButton(button_information_frame, width=200, height=60, text="Sales", image=sales_photo,
                                      compound="left", command=self.sales_gui, fg_color="#9EB23B", hover_color="#C7D36F", state="disabled")
        self.sales_button.place(x=800, y=30)

        self.display_salesman_information(self.treeview)

        window.mainloop()


    def search(self, event):
        conn = sqlite3.connect("SalesFile.db").cursor()
        try:
           #sql = ""
            conn.execute("SELECT * FROM salesman WHERE salesman_name LIKE '%"+ self.SEARCH.get()+"%' ")
            row = conn.fetchall()

            if len(row)>0:
                self.treeview.delete(*self.treeview.get_children())
                for i in row:
                    self.treeview.insert('', END, values=(i[1], i[2], i[3], i[4], [5]))
            else:
                self.treeview.delete(*self.treeview.get_children())
        except Exception as e:
            messagebox.showerror(message=f"Error Due to {str(e)}")
    # show data in the self.side_information_frame

    def showValue(self, event):
        try:
            global salesman_number

            treeview = self.treeview.focus()
            content = (self.treeview.item(treeview))
            selecteditem = content['values']

            self.salesman_number = selecteditem[0]
            # print(self.salesman_number)

            row_id = self.treeview.selection()[0]
            self.setlist = self.treeview.set(row_id)

            self.salesman_number_Entry.config(state="normal")
            self.salesman_name_Entry.config(state="normal")
            self.salesman_gender_Entry.config(state="normal")
            self.salesman_age_Entry.config(state="normal")
            self.salesman_address_Entry.config(state="normal")

            self.sales_button.config(state="disabled")

            self.salesman_number_Entry.delete(0, END)
            self.salesman_name_Entry.delete(0, END)
            self.salesman_gender_Entry.delete(0, END)
            self.salesman_age_Entry.delete(0, END)
            self.salesman_address_Entry.delete(0, END)

            #self.edit_entry_name.delete(0, END)
            #self.edit_entry_number.delete(0, END)
            #self.edit_entry_age.delete(0, END)
            #self.edit_entry_address.delete(0, END)

            self.salesman_number_Entry.insert(0, self.setlist['1'])
            self.salesman_name_Entry.insert(0, self.setlist['2'])
            self.salesman_gender_Entry.insert(0, self.setlist['3'])
            self.salesman_age_Entry.insert(0, self.setlist['4'])
            self.salesman_address_Entry.insert(0, self.setlist['5'])

            #self.edit_entry_name.insert(0, self.setlist['2'])
            #self.edit_entry_number.insert(0, self.setlist['1'])
            #self.edit_entry_age.insert(0, self.setlist['4'])
            #self.edit_entry_address.insert(0, self.setlist['5'])

            self.salesman_number_Entry.config(state="disabled")
            self.salesman_name_Entry.config(state="disabled")
            self.salesman_gender_Entry.config(state="disabled")
            self.salesman_age_Entry.config(state="disabled")
            self.salesman_address_Entry.config(state="disabled")

            self.sales_button.config(state="normal")
        except Exception as error:
            messagebox.showerror(title="Coanime Co. | Failed",
                                 message="COanime Co. | Please Try Again")
    # display data

    def display_salesman_information(self, listbox):
        listbox.delete(*listbox.get_children())

        cursor = sqlite3.connect("SalesFile.db").cursor()

        cursor.execute("SELECT * FROM salesman ORDER BY salesman_no ASC")

        self.rows = cursor.fetchall()

        #self.data = []

        for row in self.rows:
            listbox.insert('', 'end', values=(
                row[1], row[2], row[3], row[4], row[5]))

    def create_salesman(self):
        create_window = CTkToplevel()
        create_window.title("Canime Co. | Edit Salesman Information")
        create_window.geometry("550x500")

        # VARIABLE
        SALESMAN_NUMBER = IntVar()
        SALESMAN_NAME = StringVar()
        SALESMAN_GENDER = StringVar()
        SALESMAN_AGE = IntVar()
        SALESMAN_ADDRESS = StringVar()

        def create():
            self.system = System(salesman_number=SALESMAN_NUMBER.get(), salesman_name=SALESMAN_NAME.get(), salesman_gender=SALESMAN_GENDER.get(),
                                 salesman_age=SALESMAN_AGE.get(), salesman_address=SALESMAN_ADDRESS.get()).create_salesman()
            if self.system:
                messagebox.showinfo(
                    title="Canime Co. | Successfully Create Salesman", message="Successfully Created")
                create_window.destroy()
                self.display_salesman_information(self.treeview)
            else:
                messagebox.showerror(
                    title="Canime Co. | Failed Create Salesman", message="Please Try Again")

        # Frame for widgets
        self.sales_information_create_frame = CTkFrame(
            create_window, height=500, width=300)
        self.sales_information_create_frame.place(x=60)

        self.create_label = CTkLabel(
            self.sales_information_create_frame, text="Create Salesman", text_font="Gluten 20")
        self.create_label.grid(row=1, column=1, padx=10, pady=50)

        self.create_label_number = CTkLabel(
            self.sales_information_create_frame, text="Salesman Number: ", text_font="Roboto 15")
        self.create_label_number.grid(row=2, column=1)

        self.create_entry_number = CTkEntry(
            self.sales_information_create_frame, text_font="Roboto 15", width=200, textvariable=SALESMAN_NUMBER)
        self.create_entry_number.grid(row=2, column=2)

        self.create_label_name = CTkLabel(
            self.sales_information_create_frame, text="Salesman Name: ", text_font="Roboto 15")
        self.create_label_name.grid(row=3, column=1)

        self.create_entry_name = CTkEntry(
            self.sales_information_create_frame, text_font="Roboto 15", width=200, textvariable=SALESMAN_NAME)
        self.create_entry_name.grid(row=3, column=2)

        self.create_label_age = CTkLabel(
            self.sales_information_create_frame, text="Salesman Age: ", text_font="Roboto 15")
        self.create_label_age.grid(row=4, column=1)

        self.create_entry_age = CTkEntry(
            self.sales_information_create_frame, text_font="Roboto 15", width=200, textvariable=SALESMAN_AGE)
        self.create_entry_age.grid(row=4, column=2)

        self.create_label_gender = CTkLabel(
            self.sales_information_create_frame, text="Salesman Gender: ", text_font="Roboto 15")
        self.create_label_gender.grid(row=5, column=1)

        self.create_option_gender = CTkRadioButton(
            self.sales_information_create_frame, text="Male", value="Male", variable=SALESMAN_GENDER)
        self.create_option_gender.grid(row=5, column=2)

        self.create_option_gender = CTkRadioButton(
            self.sales_information_create_frame, text="Female", value="Female", variable=SALESMAN_GENDER)
        self.create_option_gender.grid(row=5, column=3)

        self.create_label_address = CTkLabel(
            self.sales_information_create_frame, text="Salesman Address: ", text_font="Roboto 15")
        self.create_label_address.grid(row=6, column=1)

        self.create_entry_address = CTkEntry(
            self.sales_information_create_frame, text_font="Roboto 15", width=200, textvariable=SALESMAN_ADDRESS)
        self.create_entry_address.grid(row=6, column=2)

        image_size = 20
        add_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/add-user.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/icons/cross-circle.png").resize((image_size, image_size)))

        add_button = CTkButton(create_window, width=200, height=60, text="Add", image=add_photo,
                               compound="left", command=create, fg_color="#4B8673", hover_color="#5FD068")
        add_button.place(x=50, y=300)

        delete_button = CTkButton(create_window, width=200, height=60, text="Cancel", image=delete_photo,
                                  compound="left", command=create_window.destroy, fg_color="#D82148", hover_color="#FF1818")
        delete_button.place(x=300, y=300)

        create_window.mainloop()

    def edit_information(self):
        create_window = CTkToplevel()
        create_window.title("Canime Co. | Edit Salesman Information")
        create_window.geometry("550x500")

        # VARIABLE
        SALESMAN_NUMBER = IntVar()
        SALESMAN_NAME = StringVar()
        SALESMAN_GENDER = StringVar()
        SALESMAN_AGE = IntVar()
        SALESMAN_ADDRESS = StringVar()

        def edit():
            system = System(self.setlist['1'], self.SALESMAN_NAME.get(), self.SALESMAN_GENDER.get(
            ), self.SALESMAN_AGE.get(), self.SALESMAN_ADDRESS.get()).update_salesman()
            if system:
                #update = System.update_salesman(self.SALESMAN_NAME, self.SALESMAN_GENDER, self.SALESMAN_AGE, self.SALESMAN_ADDRESS, self.setlist['1'])
                messagebox.showinfo(
                    message="Coanime Co. | Successfully Update", title="Success Update")
                self.display_salesman_information(self.treeview)
                create_window.destroy()
            else:
                messagebox.showerror(
                    message="Coanime Co. | Failed", title="Please Try Again")

        # Frame for widgets
        self.sales_information_edit_frame = CTkFrame(
            create_window, height=500, width=300)
        self.sales_information_edit_frame.place(x=60)

        self.edit_label = CTkLabel(
            self.sales_information_edit_frame, text="Edit Salesman", text_font="Gluten 20")
        self.edit_label.grid(row=1, column=1, padx=10, pady=50)

        self.edit_label_number = CTkLabel(
            self.sales_information_edit_frame, text="Salesman Number: ", text_font="Gluten 20")
        self.edit_label_number.grid(row=2, column=1)

        self.edit_entry_number = CTkEntry(self.sales_information_edit_frame, text_font="Roboto 15",
                                          width=200, textvariable=self.SALESMAN_NUMBER, state="disabled")
        self.edit_entry_number.grid(row=2, column=2)

        self.edit_label_name = CTkLabel(
            self.sales_information_edit_frame, text="Salesman Name: ", text_font="Roboto 15")
        self.edit_label_name.grid(row=3, column=1)

        self.edit_entry_name = CTkEntry(self.sales_information_edit_frame,
                                        text_font="Roboto 15", width=200, textvariable=self.SALESMAN_NAME)
        self.edit_entry_name.grid(row=3, column=2)

        self.edit_label_age = CTkLabel(
            self.sales_information_edit_frame, text="Salesman Age: ", text_font="Roboto 15")
        self.edit_label_age.grid(row=4, column=1)

        self.edit_entry_age = CTkEntry(self.sales_information_edit_frame,
                                       text_font="Roboto 15", width=200, textvariable=self.SALESMAN_AGE)
        self.edit_entry_age.grid(row=4, column=2)

        self.edit_label_gender = CTkLabel(
            self.sales_information_edit_frame, text="Salesman Gender: ", text_font="Roboto 15")
        self.edit_label_gender.grid(row=5, column=1)

        self.edit_option_gender = CTkRadioButton(
            self.sales_information_edit_frame, text="Male", value="Male")
        self.edit_option_gender.grid(row=5, column=2)

        self.edit_option_gender = CTkRadioButton(
            self.sales_information_edit_frame, text="Female", value="Female", textvariable=self.SALESMAN_GENDER)
        self.edit_option_gender.grid(row=5, column=3)

        self.edit_label_address = CTkLabel(
            self.sales_information_edit_frame, text="Salesman Address: ", text_font="Roboto 15")
        self.edit_label_address.grid(row=6, column=1)

        self.edit_entry_address = CTkEntry(
            self.sales_information_edit_frame, text_font="Roboto 15", width=200, textvariable=self.SALESMAN_ADDRESS)
        self.edit_entry_address.grid(row=6, column=2)

        image_size = 20
        add_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/add-user.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/icons/cross-circle.png").resize((image_size, image_size)))

        add_button = CTkButton(create_window, width=200, height=60, text="Add", image=add_photo,
                               compound="left", command=edit, fg_color="#4B8673", hover_color="#5FD068")
        add_button.place(x=50, y=300)

        delete_button = CTkButton(create_window, width=200, height=60, text="Cancel", image=delete_photo,
                                  compound="left", command=create_window.destroy, fg_color="#D82148", hover_color="#FF1818")
        delete_button.place(x=300, y=300)

        create_window.mainloop()

    def delete_information(self):
        # print(self.SALESMAN_NUMBER.get())
        delete = System.delete_salesman(self.SALESMAN_NUMBER.get(), self.SALESMAN_NAME.get())
        if delete:
            messagebox.showinfo(message="Canime Co. | Success",
                                title="Canime Co. | The Salesman has been deleted")
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
            self.display_salesman_information(self.treeview)

            self.salesman_number_Entry.config(state="disabled")
            self.salesman_name_Entry.config(state="disabled")
            self.salesman_gender_Entry.config(state="disabled")
            self.salesman_age_Entry.config(state="disabled")
            self.salesman_address_Entry.config(state="disabled")

        else:
            messagebox.showerror(message="Canime Co. | Failed",
                                 title="Canime Co. | Please Try Again")


#==============================BELOW THIS CODE IS SALES UI AND FUNCTIONS ==============================#

    def display_sales_information(self, listbox):
        listbox.delete(*listbox.get_children())

        cursor = sqlite3.connect("SalesFile.db").cursor()

        value = (self.SALESMAN_NUMBER.get(),)
        cursor.execute(
            "SELECT * FROM sales  WHERE salesman_number = ? ORDER BY salesman_number", value)

        self.row_sale = cursor.fetchall()

        #self.image_path = []
        for row in self.row_sale:
            listbox.insert('', 'end', values=(
                row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    def sales_gui(self):

        window = Toplevel()
        window.geometry("1400x800")
        window.title(
            f"Coanime Co. | {self.setlist['2']} Sales Management Dashboard")

        information_dashboard_frame = CTkFrame(
            window, height=100, width=1400, fg_color=("#5FD068", "#4B8673"))
        information_dashboard_frame.place(x=0.1, y=0.1)

        self.STOCK_NUMBER = IntVar()
        self.SALES_NAME_NEW = StringVar()
        self.SALES = StringVar()
        self.STOCK = IntVar()
        self.UNIT = StringVar()
        self.QUANTITY_NEW = IntVar()
        self.DESCRIPTION_NEW = StringVar()
        self.PRICE = IntVar()
        self.AMOUNT = IntVar()
        self.COMMISSION_NEW = IntVar()
        self.NET = IntVar()
        self.SEARCH_SALE = StringVar()

        image_label = Image.open(
            "assets/logo3.png").resize((100, 100), Image.ANTIALIAS)
        resize_image = ImageTk.PhotoImage(image_label)

        logo_label = CTkLabel(information_dashboard_frame, image=resize_image,
                              relief=GROOVE, borderwidth=0, bg="#243A73")
        logo_label.place(x=1300, y=0.1)

        company_label = CTkLabel(information_dashboard_frame, text=f"Canime Co. | {self.setlist['2']} Sales Management Dashboard", text_font=(
            "Gluten", 30), bg_color="#4B8673", text_color=('#000000', '#faf7f7'))
        company_label.place(x=200, y=25)

        # Frame for sidebar_information
        self.side_information_frame = Frame(window, height=700, width=300)
        self.side_information_frame.place(x=0.1, y=100)

        # for image or logo of the salesman
        image_size = 50

        image_resize = Image.open(
            "assets/icon/store-alt.png").resize((100, 100), Image.ANTIALIAS)
        canvas_image = ImageTk.PhotoImage(image_resize)

        self.canvas = CTkLabel(self.side_information_frame,
                               image=canvas_image, relief=GROOVE, borderwidth=0, bg="#243A73")
        self.canvas.place(x=80, y=40)
        #self.canvas.create_image(20, 20, image=add_photo)

        self.salesman_number_entry2 = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                               width=200, text_font="Roboto 13", state="normal", textvariable=self.SALESMAN_NUMBER)
        self.salesman_number_entry2.place(x=40, y=170)

        self.salesman_name_entry2 = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                             width=200, text_font="Roboto 13", state="normal", textvariable=self.SALESMAN_NAME)
        self.salesman_name_entry2.place(x=40, y=210)

        self.sales = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                         width=200, text_font="Roboto 13", textvariable=self.SALES_NAME_NEW)
        self.sales.place(x=40, y=250)

        self.stock = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.STOCK_NUMBER)
        self.stock.place(x=40, y=290)

        self.unit = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.UNIT)
        self.unit.place(x=40, y=330)

        self.quantity = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.QUANTITY_NEW)
        self.quantity.place(x=40, y=370)

        self.description = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.DESCRIPTION_NEW)
        self.description.place(x=40, y=410)

        self.price = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.PRICE)
        self.price.place(x=40, y=450)

        self.amount = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.AMOUNT)
        self.amount.place(x=40, y=490)

        self.commission = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.COMMISSION_NEW)
        self.commission.place(x=40, y=530)
        
        self.net = CTkEntry(self.side_information_frame, fg="#fcfcfc", bg=self.color,
                                          width=200, text_font="Roboto 13", textvariable=self.NET)
        self.net.place(x=40, y=570)

        # Frame for treeview_information
        treeview_information_frame = Frame(window, height=600, width=1100)
        treeview_information_frame.place(x=300, y=100)

        self.treeview_column = ('1', '2', '3', '4', '5',
                                '6', '7', '8', '9')

        self.treeview_sales = Treeview(
            treeview_information_frame, columns=self.treeview_column, show='headings', height=21)

        self.treeview_sales.heading('1', text="Sales Name")
        self.treeview_sales.column("#1", width=120)
        self.treeview_sales.heading('2', text="Stock Number")
        self.treeview_sales.column("#2", width=120)
        self.treeview_sales.heading('3', text="Sales Quantity")
        self.treeview_sales.column("#3", width=120)
        self.treeview_sales.heading('4', text="Sales Unit")
        self.treeview_sales.column("#4", width=120)
        self.treeview_sales.heading('5', text="Sales Description")
        self.treeview_sales.column("#5", width=120)
        self.treeview_sales.heading('6', text="Sales Selling Price")
        self.treeview_sales.column("#6", width=120)
        self.treeview_sales.heading('7', text="Amount")
        self.treeview_sales.column("#7", width=120)
        self.treeview_sales.heading('8', text="Commission")
        self.treeview_sales.column("#8", width=120)
        self.treeview_sales.heading('9', text="Net Amount")
        self.treeview_sales.column("#9", width=120)
        self.treeview_sales.grid()

        self.treeview_sales.bind("<Double-Button-1>", self.show_value_sales)

        # Frame for buttons
        button_information_frame = Frame(window, height=100, width=1100)
        button_information_frame.place(x=300, y=500)

        # Photo image icons
        image_size = 20

        add_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/add-user.png").resize((image_size, image_size)))
        edit_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/settings.png").resize((image_size, image_size)))
        delete_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/bell.png").resize((image_size, image_size)))
        sales_photo = ImageTk.PhotoImage(Image.open(
            "assets/icon/shop.png").resize((image_size, image_size)))

        saerch = ImageTk.PhotoImage(Image.open(
            "assets/icon/search.png").resize((20, 20)))

        search_label_image = CTkLabel(button_information_frame, image=saerch, textvariable=self.SEARCH_SALE)
        search_label_image.place(x=570, y=35)

        search_entry = CTkEntry(button_information_frame, textvariable=self.SEARCH_SALE, width=150, text_font=("Roboto 15"))
        search_entry.place(x=650, y=30)
        search_entry.bind("<Key>", self.search_sale)

        add_button = CTkButton(button_information_frame, width=200, height=60, text="Add", image=add_photo,
                               compound="left", command=self.create_sales, fg_color="#4B8673", hover_color="#5FD068")
        add_button.place(x=50, y=30)

        delete_button = CTkButton(button_information_frame, width=200, height=60, text="Delete", image=delete_photo,
                                  compound="left", command=self.delete_sales, fg_color="#D82148", hover_color="#FF1818")
        delete_button.place(x=350, y=30)

        self.display_sales_information(self.treeview_sales)

        window.mainloop()


    def search_sale(self, event):
        try:

            conn = sqlite3.connect("SalesFile.db").cursor()

            conn.execute("SELECT * FROM sales WHERE sales_name LIKE '%"+ self.SEARCH_SALE.get()+"%'")

            row = conn.fetchall()

            if len(row)>0:
                self.treeview_sales.delete(*self.treeview_sales.get_children())
                for i in row:
                    self.treeview_sales.insert('', END, values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            else:
                self.treeview_sales.delete(*self.treeview.get_children())
        except Exception as e:
            pass

    def show_value_sales(self, event):
        #global image_path
        treeview = self.treeview_sales.focus()
        content = (self.treeview_sales.item(treeview))
        selecteditem = content['values']

        sales = selecteditem[0]
        #print(sales)


        
        row_id = self.treeview_sales.selection()[0]
        self.setlist_sale = self.treeview_sales.set(row_id)
        setlist_sale = self.treeview_sales.set(row_id)

        self.sales.delete(0, END)
        self.stock.delete(0, END)
        self.unit.delete(0, END)
        self.quantity.delete(0, END)
        self.description.delete(0, END)
        self.price.delete(0, END)
        self.amount.delete(0, END)
        self.commission.delete(0, END)
        self.net.delete(0, END)

        self.sales.insert(0, setlist_sale['1'])
        self.stock.insert(0, setlist_sale['2'])
        self.unit.insert(0, setlist_sale['3'])
        self.quantity.insert(0, setlist_sale['4'])
        self.description.insert(0, setlist_sale['5'])
        self.price.insert(0, setlist_sale['6'])
        self.amount.insert(0, setlist_sale['7'])
        self.commission.insert(0,setlist_sale['8'])
        self.net.insert(0, setlist_sale['9'])


        #self.sales_name_label.config(text=f"Sales Name: {self.setlist_sale['1']}")

    def new_window_information_dashboard(self, event):
        create_win = CTkToplevel()

        create_win.geometry("550x600")
        create_win.title("Coanime Co. | Display Data")

        frame = CTkFrame(create_win, width=400, height=500)
        frame.place(x=1, y=1)

        salesman_name = CTkLabel()
    #=============CRUD FUNCTION STARTS HERE=============#

    def create_sales(self):
        create_window = CTkToplevel()
        create_window.title("Canime Co. | Create Sale Product")
        create_window.geometry("550x600")

        # VARIABLE FOR CREATING SALES
        self.ITEM_IMAGE_PATH = StringVar()
        self.SALES_NAME = StringVar()
        self.STOCK_NO = IntVar()
        self.QUANTITY = IntVar()
        self.DESCRIPTION = StringVar()
        self.UNIT = StringVar()
        self.SELLING_PRICE = IntVar()
        self.AMOUNT = 0
        self.COMMISSION = 0
        self.NET_AMOUNT = 0

        #create function
        def create_system_sale():
            sales_system = Sales_system(self.SALESMAN_NUMBER.get(), self.SALESMAN_GENDER.get(), self.SALESMAN_AGE.get(), self.SALESMAN_ADDRESS.get(),
                                        self.SALES_NAME.get(), self.STOCK_NO.get(), self.QUANTITY.get(
            ), self.UNIT.get(), self.DESCRIPTION.get(),
                self.SELLING_PRICE.get(), self.AMOUNT, self.COMMISSION, self.NET_AMOUNT)
            if sales_system.create_sales():
                messagebox.showinfo(
                    message="Coanime Co. | Sales Created!", title="Coanime Co. | Created!")
                self.display_sales_information(self.treeview_sales)
                create_window.destroy()
            else:
                messagebox.showinfo(
                    message="Coanime Co. | Sales Creation Failed!", title="Coanime Co. | Please Try Again")


        self.create_sale_frame = CTkFrame(
            create_window, height=500, width=420, fg_color="#413F42")
        self.create_sale_frame.place(x=60, y=0.1)

        create_sale_label = CTkLabel(
            self.create_sale_frame, text="Create Sale Product", text_font=("Gluten 20"))
        create_sale_label.place(x=20, y=10)

        salesman_name_label = CTkLabel(
            self.create_sale_frame, text="Salesman Number: ", text_font=("Roboto 15"))
        salesman_name_label.place(x=10, y=50)

        self.salesman_name_sales_entry = CTkEntry(
            self.create_sale_frame, width=150, text=self.SALESMAN_NUMBER, state="disabled")
        self.salesman_name_sales_entry.place(x=150, y=50)

        sales_name_product_label = CTkLabel(
            self.create_sale_frame, text="Sales Name: ", text_font=("Roboto 15"))
        sales_name_product_label.place(x=10, y=90)

        self.sales_name_product_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.SALES_NAME)
        self.sales_name_product_entry.place(x=150, y=90)

        sales_stock_no_label = CTkLabel(
            self.create_sale_frame, text="Sales Stock: ", text_font=("Roboto 15"))
        sales_stock_no_label.place(x=10, y=130)

        self.sales_stock_no_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.STOCK_NO)
        self.sales_stock_no_entry.place(x=150, y=130)

        sales_quantity_label = CTkLabel(
            self.create_sale_frame, text="Sales Quantity: ", text_font=("Roboto 15"))
        sales_quantity_label.place(x=10, y=170)

        self.sales_quantity_create_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.QUANTITY)
        self.sales_quantity_create_entry.place(x=150, y=170)

        sales_description_label = CTkLabel(
            self.create_sale_frame, text="Sales Description: ", text_font=("Roboto 15"))
        sales_description_label.place(x=10, y=210)

        self.sales_description_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.DESCRIPTION)
        self.sales_description_entry.place(x=150, y=210)

        sales_unit_label = CTkLabel(
            self.create_sale_frame, text="Sales Unit: ", text_font=("Roboto 15"))
        sales_unit_label.place(x=10, y=250)

        self.sales_unit_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.UNIT)
        self.sales_unit_entry.place(x=150, y=250)

        sales_selling_price_label = CTkLabel(
            self.create_sale_frame, text="Sales Price: ", text_font=("Roboto 15"))
        sales_selling_price_label.place(x=10, y=290)

        self.sales_selling_price_create_entry = CTkEntry(
            self.create_sale_frame, width=150, textvariable=self.SELLING_PRICE)
        self.sales_selling_price_create_entry.place(x=150, y=290)

        self.sales_amount_label = CTkLabel(
            self.create_sale_frame, text="Sales Amount: ", text_font=("Roboto 15"))
        self.sales_amount_label.place(x=10, y=330)

        self.sales_commission_label = CTkLabel(
            self.create_sale_frame, text="Sales Commission: ", text_font=("Roboto 15"))
        self.sales_commission_label.place(x=10, y=370)

        self.sales_net_amount_label = CTkLabel(
            self.create_sale_frame, text="Sales Net Amount: ", text_font=("Roboto 15"))
        self.sales_net_amount_label.place(x=10, y=410)

        # image for button
        image_size = 20
        image_download = ImageTk.PhotoImage(Image.open(
            "assets/icon/picture.png").resize((image_size, image_size)))
        add_png = ImageTk.PhotoImage(Image.open(
            "assets/icon/shop_add.png").resize((image_size, image_size)))
        ban_png = ImageTk.PhotoImage(Image.open(
            "assets/icon/ban.png").resize((image_size, image_size)))

        # FRAME FOR BUTTONS
        button_frame = CTkFrame(create_window, width=400,
                                height=50, fg_color="#7F8487")
        button_frame.place(x=70, y=520)

        self.create_sale_button = CTkButton(button_frame, width=100, height=45, image=add_png, text="Create", text_font=(
            "Gluten 15"), fg_color="#4E944F", hover_color="#83BD75", command=create_system_sale)
        self.create_sale_button.place(x=60, y=1)

        self.cancel_sale_button = CTkButton(button_frame, width=100, height=45, image=ban_png, text="Cancel", text_font=(
            "Gluten 15"), fg_color="#FD5D5D", hover_color="#FF8080", command=create_window.destroy)
        self.cancel_sale_button.place(x=230, y=1)

        def calculate(event):
            try:

                quantity = self.QUANTITY.get()
                selling_price = self.SELLING_PRICE.get()

                amount = float(quantity) * float(selling_price)
                self.AMOUNT = amount

                self.sales_amount_label.config(text=f"Sales Amount:  {amount}")

                if selling_price == 0 or quantity == 0 or selling_price == None or quantity == None:
                    self.sales_amount_label.config(text=f"Sales Amount: ")
                    self.sales_commission_label.config(
                        text=f"Sales Commission: ")
                    self.sales_net_amount_label.config(
                        text=f"Sales Net Amount: ")
                else:
                    if amount >= 50000:
                        commission = (0.25) * float(amount)
                        net_amount_data = float(amount) - float(commission)

                        self.sales_commission_label.config(
                            text=f"Sales Commission:  {commission:.2f}")
                        self.sales_net_amount_label.config(
                            text=f"Sales Net Amount:  {net_amount_data}")

                        self.COMMISSION = commission
                        self.NET_AMOUNT = net_amount_data
                    elif amount >= 40000:
                        commission = (0.20) * float(amount)
                        net_amount_data = float(amount) - float(commission)

                        self.sales_commission_label.config(
                            text=f"Sales Commission:  {commission:.2f}")
                        self.sales_net_amount_label.config(
                            text=f"Sales Net Amount:  {net_amount_data}")

                        self.COMMISSION = commission
                        self.NET_AMOUNT = net_amount_data
                    elif amount >= 30000:
                        commission = (0.15) * float(amount)
                        net_amount_data = float(amount) - float(commission)

                        self.sales_commission_label.config(
                            text=f"Sales Commission:  {commission:.2f}")
                        self.sales_net_amount_label.config(
                            text=f"Sales Net Amount:  {net_amount_data}")

                        self.COMMISSION = commission
                        self.NET_AMOUNT = net_amount_data
                    elif amount >= 20000:
                        commission = (0.10) * float(amount)
                        net_amount_data = float(amount) - float(commission)

                        self.sales_commission_label.config(
                            text=f"Sales Commission:  {commission:.2f}")
                        self.sales_net_amount_label.config(
                            text=f"Sales Net Amount:  {net_amount_data}")

                        self.COMMISSION = commission
                        self.NET_AMOUNT = net_amount_data
                    else:
                        self.sales_commission_label.config(
                            text=f"Sales Commission: 0")
                        self.sales_net_amount_label.config(
                            text=f"Sales Net Amount: 0")
                        self.COMMISSION = 0
                        self.NET_AMOUNT = 0
            except Exception as e:
                pass

        def calculate_data():
            self.sales_selling_price_create_entry.bind(
                "<KeyRelease>", calculate)
            self.sales_quantity_create_entry.bind("<KeyRelease>", calculate)
            #self.sales_selling_price_create_entry.bind("<KeyRelease>", ca)

        #self.sales_quantity_create_entry.bind("<KeyRelease>", calculate)
        calculate_data()

        #create_window.mainloop()
    def delete_sales(self):
        def delete():
            conn = sqlite3.connect("SalesFile.db")

            sql = "DELETE from sales where sales_name = ? AND sales_stock = ? AND salesman_number = ?"

            value = (self.SALES_NAME_NEW.get(), self.STOCK_NUMBER.get(), self.SALESMAN_NUMBER.get(), )

            conn.execute(sql, value)
            conn.commit()
            return True
        if delete():
            messagebox.showinfo(message="Canime Co. | Successfully Deleted", title="Canime Co. | Deleted!")
            self.display_sales_information(self.treeview_sales)
            #self.salesman_number_entry2.delete(0, END)
            #self.salesman_name_entry2.delete(0, END)
            self.sales.delete(0, END)
            self.stock.delete(0, END)
            self.unit.delete(0, END)
            self.quantity.delete(0, END)
            self.description.delete(0, END)
            self.price.delete(0, END)
            self.amount.delete(0, END)
            self.commission.delete(0, END)
            self.net.delete(0, END)
        else:
            messagebox.showerror(message="Canime Co. | Please Try Again", title="Canime Co. | Please Try Again")
            

app = mainGUI()
#app.sales_gui()
app.mainloop()
