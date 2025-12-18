from tkinter import *
from tkinter import messagebox
import sqlite3
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("600x500+450+150")
        self.root.config(bg="yellow")

        title = Label(self.root, text="Login Page", font=("goudy old style", 30, "bold"),
                      bg="light blue", fg="light yellow").place(x=0, y=0, relwidth=1, height=65)

        heading = Label(self.root, text="Sign In Form", font=("goudy old style", 35, "bold"),
                        bg="green", fg="light yellow").place(x=150, y=90)

        lbl_email = Label(self.root, text="Email Address", font=("goudy old style", 15, "bold"),
                          bg="yellow", fg="red").place(x=100, y=180)
        self.txt_email = Entry(self.root, font=("goudy old style", 15), bg="light yellow")
        self.txt_email.place(x=100, y=210, width=350)

        lbl_pass = Label(self.root, text="Password", font=("goudy old style", 15, "bold"),
                         bg="yellow", fg="red").place(x=100, y=260)
        self.txt_pass = Entry(self.root, font=("goudy old style", 15), bg="light yellow", show="*")
        self.txt_pass.place(x=100, y=290, width=350)

        btn_login = Button(self.root, text="Sign In", font=("goudy old style", 20, "bold"),
                           bg="blue", fg="white", cursor="hand2", command=self.login)
        btn_login.place(x=180, y=360, width=200, height=50)

        btn_signup = Button(self.root, text="Create New Account", font=("goudy old style", 15, "bold"),
                            bg="green", fg="white", cursor="hand2", command=self.open_register)
        btn_signup.place(x=170, y=430, width=240, height=40)

    def login(self):
        email = self.txt_email.get()
        password = self.txt_pass.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        
        try:
            con = sqlite3.connect("users.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome {row[1]}!", parent=self.root)
                self.root.destroy()
                os.system("python dashboard.py")

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def open_register(self):
     self.root.destroy()
     import register
     root = Tk()
     obj = register.Register(root)
     root.mainloop()



if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
