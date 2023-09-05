from tkinter import *
from tkinter import ttk , messagebox
#from PIL import Image , ImageTk
import sqlite3
import datetime

class repClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sanskar Mobile Repairing Shop")
        self.root.config(bg='white')
        self.root.focus_force()
        
         #========Variable Declaration===================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.cust_id = StringVar()
        self.cust_contact = StringVar()
        self.cust_name = StringVar()
        self.cust_model = StringVar()
        self.cust_aadhar = StringVar()
        self.cust_fault = StringVar()
        self.cust_charge = StringVar()
        self.cust_advnc = StringVar()
        self.cust_balance = StringVar()
        #====SearchFrame========
        searchFrame = LabelFrame(self.root,text='Search by' ,font=('goudy old style' , 12,'bold'), bg='white')
        searchFrame.place(x=250,y=20,width=600,height=70)
        
        #======ComboBox=========
        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','Aadhar','Cid','Contact'),state='readonly',justify=CENTER,font=('goudy old style' , 15,'bold'))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search = Entry(searchFrame,textvariable=self.var_searchtxt,font=('goudy old style' , 15),bg='lightyellow')
        txt_search.place(x=200,y=10)
        btn_search = Button(searchFrame,text='Search',command=self.search,font=('goudy old style' , 15),bg='#4caf50',fg='white')
        btn_search.place(x=410,y=10,width=150,height=30)
        
        #===title===============
        title=Label(self.root,text='Customer Repairing Details',font=('goudy old style' , 15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)
        
        #======1st Row Content===========
        lbl_cust_id = Label(self.root,text='Cust. Id',font=('goudy old style' , 15),bg='white')
        lbl_cust_id.place(x=50,y=150)
        lbl_name = Label(self.root,text='Name',font=('goudy old style' , 15),bg='white')
        lbl_name.place(x=380,y=150)
        lbl_contact = Label(self.root,text='Contact',font=('goudy old style' , 15),bg='white')
        lbl_contact.place(x=750,y=150)
        
        txt_cust_id = Entry(self.root , textvariable=self.cust_id,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_cust_id.place(x=150,y=150,width=180)
        txt_name = Entry(self.root , textvariable=self.cust_name,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_name.place(x=500,y=150,width=180)
        txt_contact = Entry(self.root , textvariable=self.cust_contact,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_contact.place(x=850,y=150,width=180)
        
        #=========2nd Row Content===========
        lbl_model = Label(self.root,text='Model',font=('goudy old style' , 15),bg='white')
        lbl_model.place(x=50,y=190)
        lbl_aadhar = Label(self.root,text='Aadhaar No',font=('goudy old style' , 15),bg='white')
        lbl_aadhar.place(x=380,y=190)
        lbl_fault = Label(self.root,text='Fault',font=('goudy old style' , 15),bg='white')
        lbl_fault.place(x=750,y=190)
        
        txt_model = Entry(self.root , textvariable=self.cust_model,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_model.place(x=150,y=190,width=180)
        txt_aadhar = Entry(self.root , textvariable=self.cust_aadhar,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_aadhar.place(x=500,y=190,width=180)
        txt_fault = Entry(self.root , textvariable=self.cust_fault,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_fault.place(x=850,y=190,width=180)
        
        #=========3rd Row Content===========
        lbl_charge = Label(self.root,text='Charges',font=('goudy old style' , 15),bg='white')
        lbl_charge.place(x=50,y=230)
        lbl_advance = Label(self.root,text='Advance',font=('goudy old style' , 15),bg='white')
        lbl_advance.place(x=380,y=230)
        lbl_balance = Label(self.root,text='Balance',font=('goudy old style' , 15),bg='white')
        lbl_balance.place(x=750,y=230)
        
        
        txt_charge = Entry(self.root , textvariable=self.cust_charge,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_charge.place(x=150,y=230,width=180)
        txt_advance = Entry(self.root , textvariable=self.cust_advnc,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_advance.place(x=500,y=230,width=180)
        txt_balance = Entry(self.root , textvariable=self.cust_balance,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_balance.place(x=850,y=230,width=180)
        
        
        
        #=========Buttons===================
        self.btn_repair = Button(self.root,text='Repair',command=self.repairBtn,font=('goudy old style' , 15),bg='#2196f3',fg='white',state=DISABLED)
        self.btn_repair.place(x=400,y=305,width=110,height=28)
        self.btn_clear = Button(self.root,text='Clear',command=self.clear,font=('goudy old style' , 15),bg='#607d8b',fg='white',state=DISABLED)
        self.btn_clear.place(x=530,y=305,width=110,height=28)
        
        
        
    #===============Search Button========================================================
    def search(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        #current_date = datetime.date.today()
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error' , 'Select Search by option from drop down',parent=self.root)
            elif self.var_searchtxt.get()=='':
                messagebox.showerror('Error' , 'Input required!',parent=self.root)
            else:
                #cur.execute('select * from customer where'+self.var_searchby.get()+" LIKE %"+self.var_searchtxt.get()+"%")
                cur.execute('SELECT * FROM customer WHERE ' + self.var_searchby.get() + ' LIKE ?',('%' + self.var_searchtxt.get() + '%',))
                row = cur.fetchone()
                self.cust_id.set(row[0]),
                self.cust_name.set(row[2]),
                self.cust_model.set(row[4]),
                self.cust_contact.set(row[5]),
                self.cust_aadhar.set(row[7]),
                self.cust_fault.set(row[8]),
                self.cust_charge.set(row[9]),
                self.cust_advnc.set(row[10]),
                
                if self.cust_charge.get()=='':
                    self.cust_balance.set('Charges not Mentioned')
                elif self.cust_advnc.get()=='':
                    self.cust_balance.set(row[9])
                else:    
                    x = str(int(row[9]) - int(row[10]))
                    self.cust_balance.set(x)
                self.btn_repair.config(state=NORMAL)
                self.btn_clear.config(state=NORMAL)
                
                #if len(rows)!=0:
                    #self.CustomerTable.delete(*self.CustomerTable.get_children())
                    #for row in rows:
                        #self.CustomerTable.insert('',END,values=row)
                #else:
                    #messagebox.showerror('Error','No records Found!',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
            
    #==============Repair Button========================================
    def repairBtn(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        current_date = datetime.date.today()
        #rep_status = 'Repaired'
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error' , 'Select Search by option from drop down',parent=self.root)
            elif self.var_searchtxt.get()=='':
                messagebox.showerror('Error' , 'Input required!',parent=self.root)
            else:
                #cur.execute('select * from customer where'+self.var_searchby.get()+" LIKE %"+self.var_searchtxt.get()+"%")
                cur.execute('SELECT * FROM repair WHERE cid=?' , (self.cust_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error' , 'Record already exist',parent=self.root)
                else:
                    clrbalance_value = 'Yes' if self.cust_balance.get() == '0' else 'No'
                    cur.execute('Insert into repair (date,cid,contact,aadhar,fault,balance,status,clearbalanced,setwithdraw,clearbalancedwithdraw) values(?,?,?,?,?,?,?,?,?,?)',(
                            current_date,
                            self.cust_id.get(),
                            self.cust_contact.get(),
                            self.cust_aadhar.get(),
                            self.cust_fault.get(),
                            self.cust_balance.get(),
                            'Repaired',
                            clrbalance_value,
                            'No',
                            'No'
                        ))
                    con.commit()
                    messagebox.showinfo('Success','Repaired Info added successfully',parent=self.root)
                    self.clear()
                
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
        
            
    #==============Clear Button==========================================
    def clear(self):
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')
        self.cust_id.set('')
        self.cust_name.set(''),
        self.cust_model.set(''),
        self.cust_contact.set(''),
        self.cust_aadhar.set(''),
        self.cust_fault.set(''),
        self.cust_charge.set(''),
        self.cust_advnc.set('')
        self.cust_balance.set('')
        self.btn_repair.config(state=DISABLED)
        self.btn_clear.config(state=DISABLED)        
        
if __name__ == "__main__":
    root = Tk()
    obj = repClass(root)
    root.mainloop()