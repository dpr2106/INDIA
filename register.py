from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1450x900+0+0")
        self.root.config(bg="yellow")

        # ---- DATABASE CONNECTION ----
        self.con = sqlite3.connect("users.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT,
            lname TEXT,
            contact TEXT,
            email TEXT UNIQUE,
            question TEXT,
            answer TEXT,
            password TEXT
        )
        """)
        self.con.commit()

        # ---- UI CODE STARTS ----
        title=Label(self.root,text="Register Page",font=("goudy old style",30,"bold"),
                    bg="light blue",fg="light yellow").place(x=0,y=0,relwidth=1,height=69)
        title=Label(self.root,text="Registration Form",font=("goudy old style",40,"bold"),
                    bg="green",fg="light yellow").place(x=450,y=100) 

        f_name=Label(self.root,text="First Name",font=("goudy old style",15,"bold"),
                    bg="light yellow",fg="red").place(x=200,y=190)
        self.txt_fname=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_fname.place(x=200,y=220,width=300)

        l_name=Label(self.root,text="Last Name",font=("goudy old style",15,"bold"),
                    bg="light yellow",fg="red").place(x=750,y=190) 
        self.txt_l_name=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_l_name.place(x=750,y=220,width=300)

        contact_no=Label(self.root,text="Contact No",font=("goudy old style",15,"bold"),
                         bg="light yellow",fg="red").place(x=200,y=275) 
        self.txt_contact_no=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_contact_no.place(x=200,y=308,width=300)

        email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),
                    bg="light yellow",fg="red").place(x=750,y=275) 
        self.txt_email=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_email.place(x=750,y=308,width=300)

        s_question=Label(self.root,text="Security Question",font=("goudy old style",15,"bold"),
                         bg="light yellow",fg="red").place(x=200,y=350) 
        self.txt_s_question=ttk.Combobox(self.root,font=("goudy old style",16),state='readonly',justify=CENTER)
        self.txt_s_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.txt_s_question.place(x=200,y=390,width=300)
        self.txt_s_question.set("Select")

        answer=Label(self.root,text="Answer",font=("goudy old style",15,"bold"),
                     bg="light yellow",fg="red").place(x=750,y=350) 
        self.txt_answer=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_answer.place(x=750,y=390,width=300)

        password=Label(self.root,text="Password",font=("goudy old style",15,"bold"),
                       bg="light yellow",fg="red").place(x=200,y=450) 
        self.txt_password=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_password.place(x=200,y=480,width=300)

        confirm_password=Label(self.root,text="Confirm Password",font=("goudy old style",15,"bold"),
                               bg="light yellow",fg="red").place(x=750,y=450) 
        self.txt_confirm_password=Entry(self.root,font=("goudy old style",15),bg="light yellow")
        self.txt_confirm_password.place(x=750,y=480,width=300)

        self.var_chk=IntVar()
        Checkbutton(self.root,text="I Agree The Terms & Conditions",
                    font=("arial black",12,"bold"),bg="light yellow",
                    variable=self.var_chk,onvalue=1,offvalue=0,
                    fg="red").place(x=195,y=540)

        Button(self.root,text="Register Now",font=("goudy old style",20,"bold"),
               bg="blue",fg="white",cursor="hand2",command=self.register_data)\
               .place(x=450,y=600,width=300,height=50)

        Button(self.root,text="Sign In",font=("times new roman",20,"bold"),
               bg="green",fg="white",cursor="hand2")\
               .place(x=450,y=670,width=300,height=50)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_s_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirm_password.get()=="" or self.txt_contact_no.get()=="":

            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        
        elif self.txt_password.get()!=self.txt_confirm_password.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)

        else:
            try:
                self.cur.execute("SELECT * FROM users WHERE email=?", (self.txt_email.get(),))
                row = self.cur.fetchone()

                if row is not None:
                    messagebox.showerror("Error","User Already Exists, try another email",parent=self.root)
                else:
                    self.cur.execute(
                        "INSERT INTO users(fname,lname,contact,email,question,answer,password) VALUES (?,?,?,?,?,?,?)",
                        (
                            self.txt_fname.get(),
                            self.txt_l_name.get(),
                            self.txt_contact_no.get(),
                            self.txt_email.get(),
                            self.txt_s_question.get(),
                            self.txt_answer.get(),
                            self.txt_password.get()
                        )
                    )
                    self.con.commit()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    def open_login(self):
        self.root.destroy()
        os.system("login.py")

if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
