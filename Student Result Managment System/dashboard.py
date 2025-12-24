from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass    
from result import resultClass
from report import reportClass
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        self.logo_img=Image.open("images/logo.png")
        self.logo_img=self.logo_img.resize((60,60),Image.LANCZOS)
        self.logo_dash=ImageTk.PhotoImage(self.logo_img)
        title=Label(self.root,
                    text="Student Result Management System",
                    padx=10,
                    compound=LEFT,
                    image=self.logo_dash,
                    font=("goudy old style",30,"bold"),
                    bg="light blue",
                    fg="black",).place(x=0,y=0,relwidth=1,height=69)
        M_Frame=LabelFrame(self.root,
                                       text="Menus",
                                       font=("arial black",15),
                                       bg="white",
                                       bd=1,  
                                       relief="solid",       
                                       highlightthickness=0,
                                       labelanchor="nw",       
                                       padx=5, pady=2
                                       )
        M_Frame.place(x=0,
                      y=80,
                      width=1350,
                      height=70)
        btn_course=Button(M_Frame,
                          text="Course",
                          font=("Arial black",14,"bold"),
                          bg="#003049",
                          fg="white",
                          cursor="hand2",
                          command=self.add_course).place(x=20,y=2,width=150,height=30)
        btn_student=Button(M_Frame,
                          text="Students",
                          font=("Arial black",14,"bold"),
                          bg="#003049",
                          fg="white",
                          cursor="hand2",
                          command=self.add_student).place(x=190,y=2,width=150,height=30)
        btn_result=Button(M_Frame,
                          text="Result",
                          font=("Arial black",14,"bold"),
                          bg="#003049",
                          fg="white",
                          cursor="hand2",command=self.add_result).place(x=360,y=2,width=150,height=30)
        btn_view=Button(M_Frame,
                          text="View Student Results",
                          font=("Arial black",12,"bold"),
                          bg="#003049",
                          fg="white",
                          cursor="hand2",
                          command=self.add_report).place(x=524,y=2,width=200,height=30)
        btn_logout=Button(M_Frame,
                            text="Logout",
                            font=("Arial black",14,"bold"),
                            bg="#003049",
                            fg="white",
                            cursor="hand2",
                            command=self.logout).place(x=740,y=2,width=150,height=30)
        btn_exit=Button(M_Frame,
                            text="Exit",
                            font=("Arial black",14,"bold"),
                            bg="#003049",
                            fg="white",
                            cursor="hand2",
                            command=self.exit_).place(x=910,y=2,width=150,height=30)
        

        self.bg_img=Image.open("images/c3.jpg")
        self.bg_img=img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,
                          image=self.bg_img).place(x=400,y=180,width=920,height=350)
        


        self.lbl_course=Label(self.root,
                              text="Total Courses\n[ 0 ]",
                              font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        
        self.lbl_student=Label(self.root,
                              text="Total Students\n[ 0 ]",
                              font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        
        self.lbl_result=Label(self.root,
                              text="Total Results\n[ 0 ]",
                              font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        self.footer=Label(self.root,
                    text="SRMS - Student Result Management System\n Contact us for any technical issue : +91987xxxxx01",
                    font=("goudy old style",15),
                    bg="black",
                    fg="white")
        self.footer.place(relx=0, rely=1, anchor="sw", relwidth=1, height=40)
        self.footer.lift()

        # >>>>>>>>>> NEW LINE ADDED HERE <<<<<<<<<<
        self.update_details()


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            import login
            root=Tk()
            obj=login.Login(root)

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {str(len(cr))} ]")

            cur.execute("SELECT * FROM student")
            st=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {str(len(st))} ]")

            cur.execute("SELECT * FROM result")
            rs=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {str(len(rs))} ]")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

        # >>>>>>>>>> AUTO REFRESH EVERY 2 SEC <<<<<<<<<<      i aa/a
        self.root.after(2000, self.update_details)


if __name__ == "__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
