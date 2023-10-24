from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x750+0+0")
        self.title_x = 0

        self.login_frame = Frame(self.root, bg="aqua")
        self.login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.username_label = Label(self.login_frame, text="Username:", font=("bookman old style", 15, "bold"),bg="aqua")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = Entry(self.login_frame, font=("bookman old style", 15, "bold"))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_label = Label(self.login_frame, text="Password:", font=("bookman old style", 15, "bold"),bg="aqua")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = Entry(self.login_frame, show="*", font=("bookman old style", 15, "bold"))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.login_button = Button(self.login_frame, text="Login", command=self.login,font=("bookman old style", 15, "bold"), bg="green", fg="white")
        self.login_button.grid(row=2, columnspan=2, pady=10)

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("bookman old style", 35, "bold"), bg="red", fg="black")
        title.pack(side=TOP, fill=X)

        self.prn_var=StringVar()
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.gender_var=StringVar()
        self.email_var=StringVar()
        self.div_var=StringVar()
        self.attd_var=StringVar()
        self.dbms_var=StringVar()
        self.cns_var=StringVar()
        self.spos_var=StringVar()
        self.toc_var=StringVar()
        self.iot_var=StringVar()
        self.addr_var=StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

    # Manage Frame
        self.Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="thistle")  # aqua, cornsilk ,thistle
        #self.Manage_Frame.place(x=20,y=100,width=1500,height=690)

        manage_title=Label(self.Manage_Frame,text="\t\t  MANAGE STUDENT DATA",bg="thistle",fg="dark slate gray",font=("bookman old style",30, "bold"),justify="center")
        manage_title.grid(row=0,columnspan=2,pady=20)
        lbl_prn = Label(self.Manage_Frame, text="PRN_No", bg="thistle", fg="black", font=("bookman old style", 20, "bold"))
        lbl_prn.grid(row=1, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_prn = Entry(self.Manage_Frame, textvariable=self.prn_var,bg="white", fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_prn.grid(row=1, column=1, pady=10, padx=50, sticky="w")

        lbl_roll = Label(self.Manage_Frame, text="Roll_No", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_roll.grid(row=1, column=2, pady=10, padx=(20, 50), sticky="w")
        txt_roll = Entry(self.Manage_Frame,textvariable=self.roll_var, bg="white", fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=3, pady=10, padx=50, sticky="w")

        lbl_Name = Label(self.Manage_Frame, text="Name", bg="thistle", fg="dark slate gray", font=("bookman old style", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_Name = Entry(self.Manage_Frame, textvariable=self.name_var,bg="white", fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=50, sticky="w")

        lbl_Gender = Label(self.Manage_Frame, text="Gender", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_Gender.grid(row=2, column=2, pady=10, padx=(20, 50), sticky="w")
        combo_gender = ttk.Combobox(self.Manage_Frame, textvariable=self.gender_var,font=("bookman old style", 10, "bold"),state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=2, column=3, pady=10, padx=50, sticky="w")

        lbl_email = Label(self.Manage_Frame, text="Email ID", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_email = Entry(self.Manage_Frame, textvariable=self.email_var,bg="white", fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=50, sticky="w")

        lbl_class = Label(self.Manage_Frame, text="Class", bg="thistle", fg="dark slate gray", font=("bookman old style", 20, "bold"))
        lbl_class.grid(row=3, column=2, pady=10, padx=(20, 50), sticky="w")
        combo_class=ttk.Combobox(self.Manage_Frame,textvariable=self.div_var,font=("bookman old style", 10, "bold"),state='readonly')
        combo_class['values'] = ("TE_1-P", "TE_1-Q", "TE_1-R")
        combo_class.grid(row=3, column=3, pady=10, padx=50, sticky="w")
        #txt_class = Entry(Manage_Frame, bg="white", fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        #txt_class.grid(row=3, column=3, pady=10, padx=50, sticky="w")

        lbl_attd = Label(self.Manage_Frame, text="Attendance", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_attd.grid(row=4, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_attd = Entry(self.Manage_Frame, bg="white", textvariable=self.attd_var,fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_attd.grid(row=4, column=1, pady=10, padx=50, sticky="w")

        lbl_DBMS = Label(self.Manage_Frame, text="DBMS Marks", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_DBMS.grid(row=4, column=2, pady=10, padx=(20, 50), sticky="w")
        txt_DBMS = Entry(self.Manage_Frame, bg="white", textvariable=self.dbms_var,fg="black", font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_DBMS.grid(row=4, column=3, pady=10, padx=50, sticky="w")

        lbl_CNS = Label(self.Manage_Frame, text="CNS Marks", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_CNS.grid(row=5, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_CNS = Entry(self.Manage_Frame, bg="white", fg="black", textvariable=self.cns_var,font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_CNS.grid(row=5, column=1, pady=10, padx=50, sticky="w")

        lbl_SPOS = Label(self.Manage_Frame, text="SPOS Marks", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_SPOS.grid(row=5, column=2, pady=10, padx=(20, 50), sticky="w")
        txt_SPOS = Entry(self.Manage_Frame, bg="white", fg="black", textvariable=self.spos_var,font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_SPOS.grid(row=5, column=3, pady=10, padx=50, sticky="w")

        lbl_ToC = Label(self.Manage_Frame, text="ToC Marks", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_ToC.grid(row=6, column=0, pady=10, padx=(20, 50), sticky="w")
        txt_ToC = Entry(self.Manage_Frame, bg="white", fg="black", textvariable=self.toc_var,font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_ToC.grid(row=6, column=1, pady=10, padx=50, sticky="w")

        lbl_IOT = Label(self.Manage_Frame, text="IOT Marks", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_IOT.grid(row=6, column=2, pady=10, padx=(20, 50), sticky="w")
        txt_IOT = Entry(self.Manage_Frame, bg="white", fg="black", textvariable=self.iot_var,font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_IOT.grid(row=6, column=3, pady=10, padx=50, sticky="w")

        lbl_addr = Label(self.Manage_Frame, text="Address", bg="thistle", fg="dark slate gray",font=("bookman old style", 20, "bold"))
        lbl_addr.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_IOT = Entry(self.Manage_Frame, bg="white", fg="black", textvariable=self.addr_var,font=("bookman old style", 10, "bold"), bd=5,relief=GROOVE)
        txt_IOT.grid(row=7, column=1, pady=10, padx=50, sticky="w")

        #Button Frame

        # Button Frame
        self.Btn_frame = Frame(self.Manage_Frame, bd=15, relief=RIDGE, bg="teal")
        self.Btn_frame.place(x=16, y=550, width=1470)

        # Add Button
        Add_Btn = Button(self.Btn_frame, text="ADD", width=30,command=self.add_students)
        Add_Btn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Update Button
        updt_Btn = Button(self.Btn_frame, text="UPDATE", width=30,command=self.update_data)
        updt_Btn.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        # Delete Button
        delete_Btn = Button(self.Btn_frame, text="DELETE", width=30,command=self.delete_data)
        delete_Btn.grid(row=0, column=2, pady=10, padx=10, sticky="nsew")

        # Cancel Button
        canc_Btn = Button(self.Btn_frame, text="CANCEL", width=30,command=self.clear)
        canc_Btn.grid(row=0, column=3, pady=10, padx=10, sticky="nsew")

        #search button
        search_Btn = Button(self.Btn_frame, text="SEARCH", width=30,command=self.switch_frames)
        search_Btn.grid(row=0, column=4, pady=10, padx=10, sticky="nsew")

        exit_btn = Button(self.Btn_frame, text="EXIT", width=30,command=self.exit_app)
        exit_btn.grid(row=0, column=5, pady=10, padx=10, sticky="nsew")

        # Detail Frame

        self.Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="thistle")  # aqua,cornsilk,thistle
        #self.Detail_Frame.place(x=500,y=100,width=800,height=690)

        lbl_search=Label(self.Detail_Frame,text="Search By",bg="white",fg="black",font=("bookman old style", 10, "bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(self.Detail_Frame,textvariable=self.search_by,width=10,font=("bookman old style", 13, "bold"))
        combo_search['values']=("Roll_No","Name","PRN_No")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(self.Detail_Frame,textvariable=self.search_txt,width=20,font=("bookman old style", 10, "bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(self.Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(self.Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        backbtn = Button(self.Detail_Frame, text="Go Back", width=10, pady=5,command=self.switch_manage).grid(row=0, column=10, padx=10, pady=15)

        exit_btn_detail = Button(self.Detail_Frame, text="Exit", width=10, pady=5, command=self.exit_app)
        exit_btn_detail.grid(row=0, column=19, padx=10, pady=15)

        self.Detail_Frame.grid_forget()

        # Table Frame
        self.Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="thistle")  # aqua,cornsilk,thistle
        self.Table_Frame.place(x=10,y=70,width=1500,height=600)

        scroll_x=Scrollbar(self.Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.Table_Frame,orient=VERTICAL)
        self.Student_Table=ttk.Treeview(self.Table_Frame,columns=("PRN_No","Roll_No","Name","Gender","Email ID","Class","Attendance","DBMS_Marks","CNS_Marks","SPOS_Marks","ToC_Marks","IOT_Marks","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("PRN_No",text="PRN_No")
        self.Student_Table.heading("Roll_No",text="Roll_No")
        self.Student_Table.heading("Name",text="Name")
        self.Student_Table.heading("Gender",text="Gender")
        self.Student_Table.heading("Email ID",text="Email ID")
        self.Student_Table.heading("Class",text="Class")
        self.Student_Table.heading("Attendance",text="Attendance")
        self.Student_Table.heading("DBMS_Marks",text="DBMS_Marks")
        self.Student_Table.heading("CNS_Marks",text="CNS_Marks")
        self.Student_Table.heading("SPOS_Marks",text="SPOS_Marks")
        self.Student_Table.heading("ToC_Marks",text="ToC_Marks")
        self.Student_Table.heading("IOT_Marks",text="IOT_Marks")
        self.Student_Table.heading("Address",text="Address")
        self.Student_Table['show']='headings'


        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if (self.roll_var.get()==""  or self.name_var.get()=="" or self.prn_var.get()=="" or self.gender_var.get()=="" or self.email_var.get()=="" or self.attd_var.get()=="" or self.dbms_var.get()=="" or self.cns_var.get()=="" or self.spos_var.get()=="" or self.toc_var.get()=="" or self.iot_var=="" or self.addr_var==""):
            messagebox.showerror("Error !!","All fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="Vaishu@1512",db="students")
            cur=con.cursor()
            cur.execute("INSERT INTO stud_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.prn_var.get(), self.roll_var.get(), self.name_var.get(), self.gender_var.get(),self.email_var.get(),self.div_var.get(), self.attd_var.get(), self.dbms_var.get(), self.cns_var.get(),self.spos_var.get(),self.toc_var.get(), self.iot_var.get(), self.addr_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success !!","Records added Successfully!!")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Vaishu@1512", db="students")
        cur = con.cursor()
        cur.execute("SELECT * FROM stud_data")
        row=cur.fetchall()
        if (len(row)!=0):
            self.Student_Table.delete(*self.Student_Table.get_children())
            for i in row:
                self.Student_Table.insert('',END,values=i)
            con.commit()
        con.close()

    def clear(self):
        self.prn_var.set("")
        self.roll_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.div_var.set("")
        self.attd_var.set("")
        self.dbms_var.set("")
        self.cns_var.set("")
        self.spos_var.set("")
        self.toc_var.set("")
        self.iot_var.set("")
        self.addr_var.set("")

    def get_cursor(self, ev):
    cursor_row = self.Student_Table.focus()
    if cursor_row:
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        if row:
            self.prn_var.set(row[0])
            self.roll_var.set(row[1])
            self.name_var.set(row[2])
            self.gender_var.set(row[3])
            self.email_var.set(row[4])
            self.div_var.set(row[5])
            self.attd_var.set(row[6])
            self.dbms_var.set(row[7])
            self.cns_var.set(row[8])
            self.spos_var.set(row[9])
            self.toc_var.set(row[10])
            self.iot_var.set(row[11])
            self.addr_var.set(row[12])


    def update_data(self):
        if (self.roll_var.get()==""  or self.name_var.get()=="" or self.prn_var.get()=="" or self.gender_var.get()=="" or self.email_var.get()=="" or self.attd_var.get()=="" or self.dbms_var.get()=="" or self.cns_var.get()=="" or self.spos_var.get()=="" or self.toc_var.get()=="" or self.iot_var=="" or self.addr_var==""):
            messagebox.showerror("Error !!","All fields are required!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="Vaishu@1512", db="students")
            cur = con.cursor()
            cur.execute("UPDATE stud_data SET Name=%s, Gender=%s, Email_ID=%s, Class=%s, Attendance=%s, DBMS_Marks=%s, CNS_Marks=%s, SPOS_Marks=%s, ToC_Marks=%s, IOT_Marks=%s, Address=%s WHERE Roll_No=%s",(self.name_var.get(), self.gender_var.get(), self.email_var.get(), self.div_var.get(), self.attd_var.get(),self.dbms_var.get(), self.cns_var.get(), self.spos_var.get(), self.toc_var.get(), self.iot_var.get(),self.addr_var.get(), self.roll_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success !!","Record updated successfully!!")

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Vaishu@1512", db="students")
        cur = con.cursor()
        cur.execute("SELECT * FROM stud_data WHERE " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        row=cur.fetchall()
        if len(row) == 0:
            messagebox.showerror("No Results", "No matching records found.")
        else:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for i in row:
                self.Student_Table.insert('',END,values=i)
            con.commit()
        con.close()

    def switch_frames(self):
        self.Detail_Frame.pack(side=TOP, fill=BOTH, expand=True)
        self.Manage_Frame.pack_forget()

    def switch_manage(self):
        self.Detail_Frame.pack_forget()
        self.Manage_Frame.pack(side=TOP, fill=BOTH, expand=True)

    def delete_data(self):
        if not self.roll_var.get():
            messagebox.showerror("Error", "No record selected for deletion.")
        else:

            con = pymysql.connect(host="localhost", user="root", password="Vaishu@1512", db="students")
            cur = con.cursor()
            cur.execute("DELETE FROM stud_data WHERE Roll_No=%s",self.roll_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            messagebox.showinfo("Success !!","Records deleted successfully !!")
            self.clear()

    def exit_app(self):
        self.root.destroy()

    def login(self):
        if self.username_entry.get() == "AYUSH" and self.password_entry.get() == "Password_is_very_hard~!%^@":
            messagebox.showinfo("Success !!","You have logged in successfully!!")
            self.login_frame.destroy()
            self.switch_manage()
        elif self.username_entry.get() == "GINGER" and self.password_entry.get() == "Memoryisverysharp#1220":
            messagebox.showinfo("Success !!","You have logged in successfully!!")
            self.login_frame.destroy()
            self.switch_manage()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
