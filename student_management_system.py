# ==================imports===================
import sqlite3
import re
import string
# from tkinter import *
from tkinter import END, HORIZONTAL, NO, VERTICAL, W, Button, Entry, Label, PhotoImage, Scrollbar, Tk, Toplevel, messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
# ============================================

root = Tk()
root.geometry("1366x768")
root.title("1")
root.resizable(0, 0)

global student_window
global page1
student_window = Toplevel()

#Connection to database
with sqlite3.connect("C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\Database\\student.db") as db:
    cur = db.cursor()


def valid_phone(phn):
    """    
    used regex (regular expression for validation)
    [09] Checks is phone starts with 0, 9
    \d    Match a digit (0-9 and anything else that is a "digit" in the regex engine)
    {10}  Repeat the previous "\d" 11 times (11 digits)
    $     Match the end of the string
    Valid sample 09123456789

    """
    if re.match(r"^[09]\d{10}$", phn):
        return True
    return False

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        student_window.destroy()
        root.destroy()

# ============   Student Window   ==============
class Student:
    def __init__(self, top=None):
       
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Student Management")

        self.window_title = Label(student_window)
        self.window_title.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\img\\StudentManageMentUI.png")
        self.window_title.configure(image=self.img)

        self.final_project = Label(student_window)
        self.final_project.place(relx=0.046, rely=0.055, width=136, height=30)
        self.final_project.configure(font="-family {Poppins} -size 10")
        self.final_project.configure(foreground="#000000")
        self.final_project.configure(background="#ffffff")
        self.final_project.configure(text="""Final Project""")
        self.final_project.configure(anchor="w")

        self.clock = Label(student_window)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.search_entry = Entry(student_window)
        self.search_entry.place(relx=0.040, rely=0.286, width=240, height=28)
        self.search_entry.configure(font="-family {Poppins} -size 12")
        self.search_entry.configure(relief="flat")

        self.search_std_btn = Button(student_window)
        self.search_std_btn.place(relx=0.232, rely=0.288, width=75, height=22)
        self.search_std_btn.configure(relief="flat")
        self.search_std_btn.configure(overrelief="flat")
        self.search_std_btn.configure(activebackground="#5BB2FE")
        self.search_std_btn.configure(cursor="hand2")
        self.search_std_btn.configure(foreground="#ffffff")
        self.search_std_btn.configure(background="#5BB2FE")
        self.search_std_btn.configure(font="-family {Poppins SemiBold} -size 10")
        self.search_std_btn.configure(borderwidth="0")
        self.search_std_btn.configure(text="""Search""")
        self.search_std_btn.configure(command=self.search_student)

        self.add_std_btn = Button(student_window)
        self.add_std_btn.place(relx=0.052, rely=0.426, width=306, height=28)
        self.add_std_btn.configure(relief="flat")
        self.add_std_btn.configure(overrelief="flat")
        self.add_std_btn.configure(activebackground="#5BB2FE")
        self.add_std_btn.configure(cursor="hand2")
        self.add_std_btn.configure(foreground="#ffffff")
        self.add_std_btn.configure(background="#5BB2FE")
        self.add_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.add_std_btn.configure(borderwidth="0")
        self.add_std_btn.configure(text="""Add Student""")
        self.add_std_btn.configure(command=self.add_student)

        self.update_std_btn = Button(student_window)
        self.update_std_btn.place(relx=0.052, rely=0.5, width=306, height=28)
        self.update_std_btn.configure(relief="flat")
        self.update_std_btn.configure(overrelief="flat")
        self.update_std_btn.configure(activebackground="#5BB2FE")
        self.update_std_btn.configure(cursor="hand2")
        self.update_std_btn.configure(foreground="#ffffff")
        self.update_std_btn.configure(background="#5BB2FE")
        self.update_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.update_std_btn.configure(borderwidth="0")
        self.update_std_btn.configure(text="""Update Student""")
        self.update_std_btn.configure(command=self.update_student)

        self.delete_std_btn = Button(student_window)
        self.delete_std_btn.place(relx=0.052, rely=0.57, width=306, height=27)
        self.delete_std_btn.configure(relief="flat")
        self.delete_std_btn.configure(overrelief="flat")
        self.delete_std_btn.configure(activebackground="#5BB2FE")
        self.delete_std_btn.configure(cursor="hand2")
        self.delete_std_btn.configure(foreground="#ffffff")
        self.delete_std_btn.configure(background="#5BB2FE")
        self.delete_std_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.delete_std_btn.configure(borderwidth="0")
        self.delete_std_btn.configure(text="""Delete Student""")
        self.delete_std_btn.configure(command=self.delete_student)

        self.Exit_btn = Button(student_window)
        self.Exit_btn.place(relx=0.135, rely=0.883, width=76, height=21)
        self.Exit_btn.configure(relief="flat")
        self.Exit_btn.configure(overrelief="flat")
        self.Exit_btn.configure(activebackground="#5BB2FE")
        self.Exit_btn.configure(cursor="hand2")
        self.Exit_btn.configure(foreground="#ffffff")
        self.Exit_btn.configure(background="#5BB2FE")
        self.Exit_btn.configure(font="-family {Poppins SemiBold} -size 12")
        self.Exit_btn.configure(borderwidth="0")
        self.Exit_btn.configure(text="""EXIT""")
        self.Exit_btn.configure(command=self.Exit)

        # ================= For the treeview ====================
        self.scrollbarx = Scrollbar(student_window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(student_window, orient=VERTICAL)
        self.tree = ttk.Treeview(student_window)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Student ID",
                "Name",
                "Sex",
                "Age",
                "Address",
                "College",
                "Year-Level",
                "Contact No.",
            )
        )

        self.tree.heading("Student ID", text="Student ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Sex", text="Sex", anchor=W)
        self.tree.heading("Age", text="Age", anchor=W)
        self.tree.heading("Year-Level", text="Year-Level", anchor=W)
        self.tree.heading("College", text="College", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Contact No.", text="Contact No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=280)
        self.tree.column("#3", stretch=NO, minwidth=0, width=50)
        self.tree.column("#4", stretch=NO, minwidth=0, width=50)
        self.tree.column("#5", stretch=NO, minwidth=0, width=100)
        self.tree.column("#6", stretch=NO, minwidth=0, width=100)
        self.tree.column("#7", stretch=NO, minwidth=0, width=120)
        self.tree.column("#8", stretch=NO, minwidth=0, width=97)

        self.DisplayData()

    #realtime View data in Treeview if called
    def DisplayData(self):
        cur.execute("SELECT * FROM student_data")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))


    def search_student(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.search_entry.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Student ID.", parent=student_window)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Student ID: {} found.".format(self.search_entry.get()), parent=student_window)
                    break
            else: 
                messagebox.showerror("Oops!!", "Student ID: {} not found.".format(self.search_entry.get()), parent=student_window)
    

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_student(self):
        val = []
        to_delete = []
        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Confirm Delete", parent=student_window)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%8==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    delete = "DELETE FROM student_data WHERE student_id = ?"
                    cur.execute(delete, [k])
                    db.commit()

                messagebox.showinfo("Success!!", "Student deleted from database.", parent=student_window)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a student.", parent=student_window)
    # =================================================== UPDATE ==========================================================
    def update_student(self):
        if len(self.sel)==1:
            global update_window
            update_window = Toplevel()
            page_up_win = Update_Student(update_window)
            page_up_win.time()
            update_window.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)

            page_up_win.std_name_entry.insert(0, valll[1])
            page_up_win.std_sex_entry.insert(0, valll[2])
            page_up_win.std_age_entry.insert(0, valll[4])
            page_up_win.std_addr_entry.insert(0, valll[5])
            page_up_win.std_college_entry.insert(0, valll[3])
            page_up_win.std_yrLvl_entry.insert(0, valll[6])
            page_up_win.std_contact_entry.insert(0, valll[7])


        elif len(self.sel)==0:
            messagebox.showerror("Error","Please choose a student to update.", parent=student_window)
        else:
            messagebox.showerror("Error","Can only update one student at a time.", parent=student_window)

        update_window.mainloop()

    def add_student(self):
        global add_window
        global page_add_window
        add_window = Toplevel()
        page_add_window = Add_student(add_window)
        page_add_window.time()
        add_window.mainloop()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=student_window)
        if sure == True:
            student_window.destroy()

    def ex2(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=update_window)
        if sure == True:
            update_window.destroy()
            student_window.deiconify()

# ============   ADD Window       ==============
class Add_student:
    def __init__(self, top=None):
        
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Student")

        self.label1 = Label(add_window)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\img\\AddStudent.png")
        self.label1.configure(image=self.img)

        self.clock = Label(add_window)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        
        self.std_name_entry = Entry(add_window)
        self.std_name_entry.place(relx=0.132, rely=0.296, width=996, height=30)
        self.std_name_entry.configure(font="-family {Poppins} -size 12")
        self.std_name_entry.configure(relief="flat")
        
        self.std_sex_entry = Entry(add_window)
        self.std_sex_entry.place(relx=0.132, rely=0.413, width=374, height=30)
        self.std_sex_entry.configure(font="-family {Poppins} -size 12")
        self.std_sex_entry.configure(relief="flat")

        
        self.std_age_entry = Entry(add_window)
        self.std_age_entry.place(relx=0.132, rely=0.529, width=374, height=30)
        self.std_age_entry.configure(font="-family {Poppins} -size 12")
        self.std_age_entry.configure(relief="flat")
        
        
        self.std_addr_entry = Entry(add_window)
        self.std_addr_entry.place(relx=0.132, rely=0.646, width=374, height=30)
        self.std_addr_entry.configure(font="-family {Poppins} -size 12")
        self.std_addr_entry.configure(relief="flat")
       
        
        self.std_college_entry = Entry(add_window)
        self.std_college_entry.place(relx=0.527, rely=0.413, width=374, height=30)
        self.std_college_entry.configure(font="-family {Poppins} -size 12")
        self.std_college_entry.configure(relief="flat")
       
        
        self.std_yrLvl_entry = Entry(add_window)
        self.std_yrLvl_entry.place(relx=0.527, rely=0.529, width=374, height=30)
        self.std_yrLvl_entry.configure(font="-family {Poppins} -size 12")
        self.std_yrLvl_entry.configure(relief="flat")
       
        
        self.std_contact_entry = Entry(add_window)
        self.std_contact_entry.place(relx=0.527, rely=0.646, width=374, height=30)
        self.std_contact_entry.configure(font="-family {Poppins} -size 12")
        self.std_contact_entry.configure(relief="flat")
       
        
        self.add_std_btn_addWin = Button(add_window)
        self.add_std_btn_addWin.place(relx=0.408, rely=0.836, width=96, height=34)
        self.add_std_btn_addWin.configure(relief="flat")
        self.add_std_btn_addWin.configure(overrelief="flat")
        self.add_std_btn_addWin.configure(activebackground="#5BB2FE")
        self.add_std_btn_addWin.configure(cursor="hand2")
        self.add_std_btn_addWin.configure(foreground="#ffffff")
        self.add_std_btn_addWin.configure(background="#5BB2FE")
        self.add_std_btn_addWin.configure(font="-family {Poppins SemiBold} -size 14")
        self.add_std_btn_addWin.configure(borderwidth="0")
        self.add_std_btn_addWin.configure(text="""ADD""")
        self.add_std_btn_addWin.configure(command=self.add)

        self.clr_std_btn_addWin = Button(add_window)
        self.clr_std_btn_addWin.place(relx=0.526, rely=0.836, width=86, height=34)
        self.clr_std_btn_addWin.configure(relief="flat")
        self.clr_std_btn_addWin.configure(overrelief="flat")
        self.clr_std_btn_addWin.configure(activebackground="#5BB2FE")
        self.clr_std_btn_addWin.configure(cursor="hand2")
        self.clr_std_btn_addWin.configure(foreground="#ffffff")
        self.clr_std_btn_addWin.configure(background="#5BB2FE")
        self.clr_std_btn_addWin.configure(font="-family {Poppins SemiBold} -size 14")
        self.clr_std_btn_addWin.configure(borderwidth="0")
        self.clr_std_btn_addWin.configure(text="""CLEAR""")
        self.clr_std_btn_addWin.configure(command=self.clearr)

    def add(self):

        add_student_name = self.std_name_entry.get()  
        add_sex = self.std_sex_entry.get()  
        add_age = self.std_age_entry.get()  
        add_address = self.std_addr_entry.get()  
        add_college = self.std_college_entry.get()
        add_yr_lvl = self.std_yrLvl_entry.get()  
        add_contact = self.std_contact_entry.get() 
        
        if add_student_name.strip():
            if add_sex.strip():
                if add_age.strip():
                    if add_address.strip():
                        if add_college.strip():
                            if add_yr_lvl.strip():
                                if valid_phone(add_contact):
                                    with sqlite3.connect("C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\Database\\student.db") as db:
                                        cur = db.cursor()
                                        insert =("""INSERT INTO student_data
                                                (
                                                student_name,
                                                sex, 
                                                age, 
                                                address, 
                                                college, 
                                                year_level, 
                                                contact_no
                                                ) 
                                                VALUES(?,?,?,?,?,?,?)"""
                                            )
                                    cur.execute(insert, [add_student_name, add_sex, add_age, add_address, add_college, add_yr_lvl, add_contact])
                                    db.commit()
                                    messagebox.showinfo("Success!!", "student successfully added in list.", parent=add_window)
                                
                                    Student.sel.clear()
                                    add_window.destroy()
                                    page1.tree.delete(*page1.tree.get_children())
                                    page1.DisplayData()
                                    add_window.destroy()
                                else:
                                    messagebox.showerror("Oops!", "Invalid phone number.", parent=add_window)
                            else:
                                messagebox.showerror("Oops!", "Please student year-level.", parent=add_window)
                        else:
                            messagebox.showerror("Oops!", "Please enter student college.", parent=add_window)
                    else:
                        messagebox.showerror("Oops!", "Please enter address.", parent=add_window)
                else:
                    messagebox.showerror("Oops!", "Please enter Student age.", parent=add_window)
            else:
                messagebox.showerror("Oops!", "Please enter Student sex.", parent=add_window)
        else:
            messagebox.showerror("Oops!", "Please enter Student name", parent=add_window)

    def clearr(self):
        self.std_name_entry.delete(0, END)
        self.std_sex_entry.delete(0, END)
        self.std_age_entry.delete(0, END)
        self.std_addr_entry.delete(0, END)
        self.std_college_entry.delete(0, END)
        self.std_yrLvl_entry.delete(0, END)
        self.std_contact_entry.delete(0, END)


    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

# ============  Update Window     ==============
class Update_Student:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Student")

        self.label1 = Label(update_window)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\img\\UpdateStudent.png")
        self.label1.configure(image=self.img)

        self.clock = Label(update_window)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.std_name_entry = Entry(update_window)
        self.std_name_entry.place(relx=0.132, rely=0.296, width=996, height=30)
        self.std_name_entry.configure(font="-family {Poppins} -size 12")
        self.std_name_entry.configure(relief="flat")

        self.std_sex_entry = Entry(update_window)
        self.std_sex_entry.place(relx=0.132, rely=0.413, width=374, height=30)
        self.std_sex_entry.configure(font="-family {Poppins} -size 12")
        self.std_sex_entry.configure(relief="flat")

        self.std_age_entry = Entry(update_window)
        self.std_age_entry.place(relx=0.132, rely=0.529, width=374, height=30)
        self.std_age_entry.configure(font="-family {Poppins} -size 12")
        self.std_age_entry.configure(relief="flat")

        self.std_addr_entry = Entry(update_window)
        self.std_addr_entry.place(relx=0.132, rely=0.646, width=374, height=30)
        self.std_addr_entry.configure(font="-family {Poppins} -size 12")
        self.std_addr_entry.configure(relief="flat")

        self.std_college_entry = Entry(update_window)
        self.std_college_entry.place(relx=0.527, rely=0.413, width=374, height=30)
        self.std_college_entry.configure(font="-family {Poppins} -size 12")
        self.std_college_entry.configure(relief="flat")

        self.std_yrLvl_entry = Entry(update_window)
        self.std_yrLvl_entry.place(relx=0.527, rely=0.529, width=374, height=30)
        self.std_yrLvl_entry.configure(font="-family {Poppins} -size 12")
        self.std_yrLvl_entry.configure(relief="flat")

        self.std_contact_entry = Entry(update_window)
        self.std_contact_entry.place(relx=0.527, rely=0.646, width=374, height=30)
        self.std_contact_entry.configure(font="-family {Poppins} -size 12")
        self.std_contact_entry.configure(relief="flat")
       
        self.up_std_btn_upWin = Button(update_window)
        self.up_std_btn_upWin.place(relx=0.408, rely=0.836, width=96, height=34)
        self.up_std_btn_upWin.configure(relief="flat")
        self.up_std_btn_upWin.configure(overrelief="flat")
        self.up_std_btn_upWin.configure(activebackground="#5BB2FE")
        self.up_std_btn_upWin.configure(cursor="hand2")
        self.up_std_btn_upWin.configure(foreground="#ffffff")
        self.up_std_btn_upWin.configure(background="#5BB2FE")
        self.up_std_btn_upWin.configure(font="-family {Poppins SemiBold} -size 14")
        self.up_std_btn_upWin.configure(borderwidth="0")
        self.up_std_btn_upWin.configure(text="""UPDATE""")
        self.up_std_btn_upWin.configure(command=self.update)

        self.clr_std_btn_upWin = Button(update_window)
        self.clr_std_btn_upWin.place(relx=0.526, rely=0.836, width=86, height=34)
        self.clr_std_btn_upWin.configure(relief="flat")
        self.clr_std_btn_upWin.configure(overrelief="flat")
        self.clr_std_btn_upWin.configure(activebackground="#5BB2FE")
        self.clr_std_btn_upWin.configure(cursor="hand2")
        self.clr_std_btn_upWin.configure(foreground="#ffffff")
        self.clr_std_btn_upWin.configure(background="#5BB2FE")
        self.clr_std_btn_upWin.configure(font="-family {Poppins SemiBold} -size 14")
        self.clr_std_btn_upWin.configure(borderwidth="0")
        self.clr_std_btn_upWin.configure(text="""CLEAR""")
        self.clr_std_btn_upWin.configure(command=self.clearr)

    def update(self):

        up_student_name = self.std_name_entry.get() 
        up_sex = self.std_sex_entry.get()  
        up_age = self.std_age_entry.get()
        up_address = self.std_addr_entry.get()  
        up_college = self.std_college_entry.get()  
        up_yr_lvl = self.std_yrLvl_entry.get()  
        up_contact = self.std_contact_entry.get()  

        # input validation
        #.strip removes white trails both leading and ending
        if up_student_name.strip():
            if up_sex.strip():
                if up_age.strip():
                    if up_address.strip():
                        if up_college.strip():
                            if up_yr_lvl.strip():
                                if valid_phone(up_contact):
                                    student_id = valll[0]
                                    with sqlite3.connect("C:\\Users\\Gigabyte\\Desktop\\2nd SY. 2021-2022\\Advance-OOP\\Final_Project\\Database\\student.db") as db:
                                        cur = db.cursor()
                                    update = (
                                    """UPDATE student_data SET 
                                        student_name = ?, 
                                        sex = ?, age = ?, 
                                        address = ?, 
                                        college = ?, 
                                        year_level = ?, 
                                        contact_no = ? 
                                        WHERE student_id = ?"""
                                    )
                                    cur.execute(update, [up_student_name, up_sex, up_age, up_address, up_college, up_yr_lvl, up_contact, student_id])
                                    db.commit()
                                    messagebox.showinfo("Success!!", "student successfully updated in list.", parent=update_window)
                                    valll.clear()
                                    Student.sel.clear()
                                    page1.tree.delete(*page1.tree.get_children())
                                    page1.DisplayData()
                                    update_window.destroy()
                                else:
                                    messagebox.showerror("Oops!", "Invalid phone number.", parent=update_window)
                            else:
                                messagebox.showerror("Oops!", "Please student year-level.", parent=update_window)
                        else:
                            messagebox.showerror("Oops!", "Please enter student college.", parent=update_window)
                    else:
                        messagebox.showerror("Oops!", "Please enter address.", parent=update_window)
                else:
                    messagebox.showerror("Oops!", "Please enter Student age.", parent=update_window)
            else:
                messagebox.showerror("Oops!", "Please enter Student sex.", parent=update_window)
        else:
            messagebox.showerror("Oops!", "Please enter Student name", parent=update_window)

    def clearr(self):
        self.std_name_entry.delete(0, END)
        self.std_sex_entry.delete(0, END)
        self.std_age_entry.delete(0, END)
        self.std_addr_entry.delete(0, END)
        self.std_college_entry.delete(0, END)
        self.std_yrLvl_entry.delete(0, END)
        self.std_contact_entry.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


root.withdraw()
page1 = Student(student_window)
page1.time()
root.mainloop()



# References 
""" 
with 
https://www.geeksforgeeks.org/with-statement-in-python/

re (regex)
https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html

strip()
https://www.programiz.com/python-programming/methods/string/strip

"""