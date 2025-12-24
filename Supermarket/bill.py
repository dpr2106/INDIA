from tkinter import*
import random,math,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,
                    text="Billing Software",
                    font=("Showcard Gothic",30,"bold"),
                    bg="yellow",
                    fg="red",
                    bd=12,
                    relief=GROOVE).place(x=0,y=0,relwidth=1,height=80)
        
        ############variables#############
        self.soap=IntVar()
        self.colgate=IntVar()
        self.cream=IntVar()
        self.vaseline=IntVar()
        self.bodylotion=IntVar()
        self.surfexcel=IntVar()
        self.lipstick=IntVar()
#################grocery variables#################
        self.rice=IntVar()
        self.chips=IntVar()
        self.coke=IntVar()
        self.choclate=IntVar()
        self.biscuits=IntVar()
        self.flour=IntVar()
        self.oil=IntVar()
        ##################product price & tax variables##############
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        ###############customer##################
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        
        ##################### Customer Frame #####################
        
        F1=LabelFrame(self.root,
                      text="Customer Details",
                      font=("Arial Black",15,"bold"),
                      bg="#003049",
                      fg="white",
                      bd=12,
                      relief=GROOVE).place(x=0,y=70,relwidth=1,height=110)
        
        cname_lbl=Label(F1,
                        text="Customer Name:",
                        font=("Arial Black",12,"bold"),
                        bg="#003049",       
                        fg="white").place(x=19,y=125)
        cname_lbl=Entry(F1,
                        font=("Arial Black",12,"bold"),
                        textvariable=self.c_name,
                               bg="light yellow",width=13,
                               bd=7,
                               relief=SUNKEN).place(x=180,y=120)
        

        cphn_lbl=Label(F1,
                        text="Customer Phone No:",
                        font=("Arial Black",12,"bold"),
                        bg="#003049",       
                        fg="white").place(x=360,y=127)
        cphn_lbl=Entry(F1,
                        font=("Arial Black",12,"bold"),
                        textvariable=self.c_phon,
                               bg="light yellow",width=15,
                               bd=7,
                               relief=SUNKEN).place(x=560,y=123)
        

        billn_lbl=Label(F1,
                        text="Bill Number:",
                        font=("Arial Black",12,"bold"),
                        bg="#003049",       
                        fg="white").place(x=780,y=125)
        billn_lbl=Entry(F1,
                        font=("Arial Black",12,"bold"),
                        textvariable=self.search_bill,
                               bg="light yellow",width=15,
                               bd=7,
                               relief=SUNKEN).place(x=920,y=123)
        
        billn_button=Button(F1,
                        text="Search",
                        font=("Arial Black",12,"bold"),
                        bg="light yellow",       
                        fg="black",cursor="hand2",
                        command=self.find_bill).place(x=1150,y=125,width=100,height=30)
        

        F2=LabelFrame(self.root,
                      text="Cosmetics",
                      font=("Arial Black",15,"bold"),
                      bg="#003049",
                      fg="white",
                      bd=12,
                      relief=GROOVE).place(x=0,y=180,width=400,height=385)
        bath_lbl=Label(F2,
                       text=" ● Mysore Sandal:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=220)
        bath_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.soap,
                       bg="light yellow").place(x=215,y=223,width=150,height=30)   
        
        colgate_lbl=Label(F2,
                       text=" ● Colgate:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=270)
        colgate_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.colgate,
                       bg="light yellow").place(x=215,y=273,width=150,height=30)   
        
        ponds_lbl=Label(F2,
                       text=" ● Pond's Cream:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=320)
        ponds_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.cream,
                       bg="light yellow").place(x=215,y=323,width=150,height=30)   
        vaseline_lbl=Label(F2,
                       text=" ● Vaseline:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=370)
        vaseline_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.vaseline,
                       bg="light yellow").place(x=215,y=373,width=150,height=30)  

        bodyl_lbl=Label(F2,
                       text=" ● Body Lotion:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=420)
        bodyl_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.bodylotion,
                       bg="light yellow").place(x=215,y=423,width=150,height=30) 
        
        surfe_lbl=Label(F2,
                       text=" ● Surf Excel:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=470)
        surfe_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.surfexcel,
                       bg="light yellow").place(x=215,y=473,width=150,height=30) 
        lipstick_lbl=Label(F2,
                       text=" ● Lipstick:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=12,y=516)
        lipstick_txt=Entry(F2,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.lipstick,
                       bg="light yellow").place(x=215,y=519,width=150,height=30) 
        
        F5=LabelFrame(self.root,
                      bg="red").place(x=400,y=180,width=400,height=385)

        
        F3=LabelFrame(self.root,
                      text="Grocery",
                      font=("Arial Black",15,"bold"),
                      bg="#003049",
                      fg="white",
                      bd=12,
                      relief=GROOVE).place(x=435,y=180,width=400,height=385)

        rice_lbl=Label(F3,
                       text=" ● Rice:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=220)
        rice_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.rice,
                       bg="light yellow").place(x=625,y=223,width=150,height=30)  

        chips_lbl=Label(F3,
                       text=" ● Chips:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=270)
        chips_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.chips,
                       bg="light yellow").place(x=625,y=273,width=150,height=30) 
        coke_lbl=Label(F3,
                       text=" ● Coke:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=320)
        coke_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.coke,
                       bg="light yellow").place(x=625,y=323,width=150,height=30) 
        choclate_lbl=Label(F3,
                       text=" ● Choclate:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=370)
        choclate_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.choclate,
                       bg="light yellow").place(x=625,y=373,width=150,height=30) 
        biscuits_lbl=Label(F3,
                       text=" ● Biscuits:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=420)
        biscuits_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.biscuits,
                       bg="light yellow").place(x=625,y=423,width=150,height=30) 
        flour_lbl=Label(F3,
                       text=" ● Flour:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=470)
        flour_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.flour,
                       bg="light yellow").place(x=625,y=473,width=150,height=30)
        oil_lbl=Label(F3,
                       text=" ● Oil:",
                       font=("Arial Black",15,"bold"),
                       bg="#003049",
                       fg="white").place(x=447,y=516)
        oil_txt=Entry(F3,
                       font=("Arial Black",15,"bold"),
                       textvariable=self.oil,
                       bg="light yellow").place(x=625,y=519,width=150,height=30)  
        

        F6=LabelFrame(self.root,
                      bg="red").place(x=835,y=180,width=400,height=385)
        
        ################## Menu Frame #####################
        F4 = Frame(self.root, bd=12, relief=GROOVE)
        F4.place(x=870, y=180, width=400, height=385)

        bill_title = Label(F4,
                        text="Bill Area",
                        font=("Arial Black",15,"bold"),
                        bd=7,
                        relief=GROOVE)
        bill_title.pack(fill=X)

        scrol_y = Scrollbar(F4, orient=VERTICAL)
        self.txtarea = Text(F4, yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT, fill=Y)
        self.txtarea.pack(fill=BOTH, expand=1)

        scrol_y.config(command=self.txtarea.yview)


        F7=LabelFrame(self.root,
                      text="Bill Menu",
                      font=("Arial Black",15,"bold"),
                      bg="#003049",
                      fg="white",
                      bd=12,
                      relief=GROOVE).place(x=0,y=565,width=1300,height=210)
        
        m1_lbl=Label(F7,
                 text="Total Cosmetic Price:",
                 font=("Arial Black",12,"bold"),
                 bg="#003049",
                 fg="white").place(x=19,y=600)
        m1_txt=Entry(F7,
                 font=("Arial Black",12,"bold"),
                 textvariable=self.cosmetic_price,
                        bg="light yellow",
                        bd=7,
                        relief=SUNKEN).place(x=220,y=600,width=150,height=30)   
        
        m2_lbl=Label(F7,
                 text="Total Grocery Price:",
                 font=("Arial Black",12,"bold"),
                 bg="#003049",
                 fg="white").place(x=19,y=650)
        m2_txt=Entry(F7,
                 font=("Arial Black",12,"bold"),
                 textvariable=self.grocery_price,
                        bg="light yellow",
                        bd=7,
                        relief=SUNKEN).place(x=220,y=650,width=150,height=30) 
     
        
        c1_lbl=Label(F7,
                 text="Cosmetic Tax:",
                 font=("Arial Black",12,"bold"),
                 bg="#003049",
                 fg="white").place(x=419,y=600)
        c1_txt=Entry(F7,
                 font=("Arial Black",12,"bold"),
                 textvariable=self.cosmetic_tax,
                        bg="light yellow",
                        bd=7,
                        relief=SUNKEN).place(x=570,y=600,width=150,height=30)   
        
        c2_lbl=Label(F7,
                 text="Grocery Tax:",
                 font=("Arial Black",12,"bold"),
                 bg="#003049",
                 fg="white").place(x=419,y=650)
        c2_txt=Entry(F7,
                 font=("Arial Black",12,"bold"),
                 textvariable=self.grocery_tax,
                        bg="light yellow",
                        bd=7,
                        relief=SUNKEN).place(x=570,y=650,width=150,height=30) 
        
        btn_F=Frame(F7,bd=7,relief=GROOVE,bg="yellow")
        btn_F.place(x=730,y=590,width=530,height=100)

        total_btn=Button(btn_F,
                         text="Total",
                         font=("Arial Black",12,"bold"),
                         bg="light blue",
                         fg="black",cursor="hand2",
                         command=self.total).place(x=10,y=3,width=100,height=80)
        GBill_btn=Button(btn_F,
                         text="Generate Bill",
                         font=("Arial Black",12,"bold"),
                         command=self.bill_area, 
                         bg="light blue",
                         fg="black",cursor="hand2").place(x=130,y=3,width=150,height=80)
        Clear_btn=Button(btn_F,
                         text="Clear",
                         font=("Arial Black",12,"bold"),
                            bg="light blue",
                            fg="black",cursor="hand2",
                            command=self.clear_data).place(x=300,y=3,width=100,height=80)
        Exit_btn=Button(btn_F,
                         text="Exit",
                         font=("Arial Black",12,"bold"),
                         bg="light blue",
                         fg="black",cursor="hand2",
                         command=self.exit_app).place(x=410,y=3,width=100,height=80)
        self.welcome_bill()
        
    def total(self):
        self.total_cosmetic_price=float(
                                                 (self.soap.get()*40)+
            (self.colgate.get()*60)+
            (self.cream.get()*120)+
            (self.vaseline.get()*150)+  
            (self.bodylotion.get()*200)+
            (self.surfexcel.get()*70)+
            (self.lipstick.get()*250))
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.total_grocery_price=float(
            (self.rice.get()*80)+
            (self.chips.get()*30)+
            (self.coke.get()*50)+
            (self.choclate.get()*60)+  
            (self.biscuits.get()*40)+
            (self.flour.get()*90)+
            (self.oil.get()*120))
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.cosmetic_tax.set("Rs. "+str(round(self.total_cosmetic_price*0.05,2)))
        self.grocery_tax.set("Rs. "+str(round(self.total_grocery_price*0.05,2)))
        self.total_bill=float(self.total_cosmetic_price+self.total_grocery_price+float(self.cosmetic_tax.get().replace("Rs. ",""))+float(self.grocery_tax.get().replace("Rs. ","")))
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\n\t    Super Low Supermarket\n")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
            return
        self.welcome_bill()
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\nMysore Sandal\t\t{self.soap.get()}\t\t{self.soap.get()*40}")
        if self.colgate.get()!=0:
            self.txtarea.insert(END,f"\nColgate\t\t{self.colgate.get()}\t\t{self.colgate.get()*60}")
        if self.cream.get()!=0:
            self.txtarea.insert(END,f"\nPond's Cream\t\t{self.cream.get()}\t\t{self.cream.get()*120}")
        if self.vaseline.get()!=0:
            self.txtarea.insert(END,f"\nVaseline\t\t{self.vaseline.get()}\t\t{self.vaseline.get()*150}")
        if self.bodylotion.get()!=0:
            self.txtarea.insert(END,f"\nBody Lotion\t\t{self.bodylotion.get()}\t\t{self.bodylotion.get()*200}")
        if self.surfexcel.get()!=0:
            self.txtarea.insert(END,f"\nSurf Excel\t\t{self.surfexcel.get()}\t\t{self.surfexcel.get()*70}")
        if self.lipstick.get()!=0:
            self.txtarea.insert(END,f"\nLipstick\t\t{self.lipstick.get()}\t\t{self.lipstick.get()*250}")
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.rice.get()*80}")
        if self.chips.get()!=0:
            self.txtarea.insert(END,f"\nChips\t\t{self.chips.get()}\t\t{self.chips.get()*30}")
        if self.coke.get()!=0:
            self.txtarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t\t{self.coke.get()*50}")
        if self.choclate.get()!=0:
            self.txtarea.insert(END,f"\nChoclate\t\t{self.choclate.get()}\t\t{self.choclate.get()*60}")
        if self.biscuits.get()!=0:
            self.txtarea.insert(END,f"\nBiscuits\t\t{self.biscuits.get()}\t\t{self.biscuits.get()*40}")
        if self.flour.get()!=0:
            self.txtarea.insert(END,f"\nFlour\t\t{self.flour.get()}\t\t{self.flour.get()*90}")
        if self.oil.get()!=0:
            self.txtarea.insert(END,f"\nOil\t\t{self.oil.get()}\t\t{self.oil.get()*120}")
        self.txtarea.insert(END,f"\n-------------------------------------")
        if self.cosmetic_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
        if self.grocery_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.txtarea.insert(END,f"\nTotal Bill : {self.total_cosmetic_price+self.total_grocery_price+float(self.cosmetic_tax.get().replace('Rs. ',''))+float(self.grocery_tax.get().replace('Rs. ',''))}")  
        self.txtarea.insert(END,f"\n-------------------------------------")
        self.save_bill()
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op:
            if not os.path.exists("bills"):
                os.makedirs("bills")
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. : {self.bill_no.get()} saved successfully!")
        else:
            messagebox.showinfo("Not Saved", "Bill not saved.")
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear Data?")
        if op==True:
            # ======cosmetic=======
            self.soap.set(0)
            self.colgate.set(0)
            self.cream.set(0)
            self.vaseline.set(0)
            self.bodylotion.set(0)
            self.surfexcel.set(0)
            self.lipstick.set(0)
            # ======grocery=======
            self.rice.set(0)
            self.chips.set(0)
            self.coke.set(0)
            self.choclate.set(0)
            self.biscuits.set(0)
            self.flour.set(0)
            self.oil.set(0)
            # ======total & tax=======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            # ======customer=======
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
        else:
            return
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op==True:
            self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()