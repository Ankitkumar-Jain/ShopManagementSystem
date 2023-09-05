from tkinter import *
from tkinter import ttk , messagebox
#from PIL import Image , ImageTk
import sqlite3
import datetime

class statusClass:
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
        self.cust_fault = StringVar()
        self.cust_aadhar = StringVar()
        self.cust_status = StringVar()
        self.cust_balance = StringVar()
        self.clr_balance = StringVar()
        self.set_withdraw = StringVar()
        self.clrbalancewithdraw = StringVar()
        self.var_chk = StringVar()
        #====SearchFrame========
        searchFrame = LabelFrame(self.root,text='Search by' ,font=('goudy old style' , 12,'bold'), bg='white')
        searchFrame.place(x=250,y=20,width=600,height=70)
        
        #======ComboBox=========
        cmb_search = ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','Aadhar','Cid','Contact'),state='readonly',justify=CENTER,font=('goudy old style' , 15,'bold'))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search = Entry(searchFrame,textvariable=self.var_searchtxt,font=('goudy old style' , 15),bg='lightyellow')
        txt_search.place(x=200,y=10)
        btn_search = Button(searchFrame,text='Check Status',command=self.search,font=('goudy old style' , 15),bg='#4caf50',fg='white')
        btn_search.place(x=410,y=10,width=150,height=30)
        
        #===title===============
        title=Label(self.root,text='Customer Repairing Status',font=('goudy old style' , 15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)
        
        #======1st Row Content===========
        lbl_cust_id = Label(self.root,text='Cust. Id',font=('goudy old style' , 15),bg='white')
        lbl_cust_id.place(x=50,y=150)
        lbl_aadhar = Label(self.root,text='Aadhar No',font=('goudy old style' , 15),bg='white')
        lbl_aadhar.place(x=380,y=150)
        lbl_contact = Label(self.root,text='Contact',font=('goudy old style' , 15),bg='white')
        lbl_contact.place(x=750,y=150)
        
        txt_cust_id = Entry(self.root , textvariable=self.cust_id,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_cust_id.place(x=150,y=150,width=180)
        txt_aadhar = Entry(self.root , textvariable=self.cust_aadhar,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_aadhar.place(x=500,y=150,width=180)
        txt_contact = Entry(self.root , textvariable=self.cust_contact,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_contact.place(x=850,y=150,width=180)
        
        #=========2nd Row Content===========
        lbl_fault = Label(self.root,text='Issues',font=('goudy old style' , 15),bg='white')
        lbl_fault.place(x=50,y=190)
        lbl_status = Label(self.root,text='Status',font=('goudy old style' , 15),bg='white')
        lbl_status.place(x=380,y=190)
        lbl_balance = Label(self.root,text='Balance',font=('goudy old style' , 15),bg='white')
        lbl_balance.place(x=750,y=190)
        
        txt_fault = Entry(self.root , textvariable=self.cust_fault,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_fault.place(x=150,y=190,width=180)
        txt_status = Entry(self.root , textvariable=self.cust_status,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_status.place(x=500,y=190,width=180)
        txt_balance = Entry(self.root , textvariable=self.cust_balance,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_balance.place(x=850,y=190,width=180)
        
        #=========3rd Row Content===========
        lbl_clrbalance = Label(self.root,text='Bal. Cleared',font=('goudy old style' , 15),bg='white')
        lbl_clrbalance.place(x=50,y=230)
        lbl_setWithdraw = Label(self.root,text='Recieved',font=('goudy old style' , 15),bg='white')
        lbl_setWithdraw.place(x=380,y=230)
        #============New Row================
        lbl_clrbalancewithdraw = Label(self.root,text='Balance',font=('goudy old style' , 15),bg='white')
        lbl_clrbalancewithdraw.place(x=50,y=305)
        
        
        txt_clrbalance = Entry(self.root , textvariable=self.clr_balance,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_clrbalance.place(x=150,y=230,width=180)
        txt_setWithdraw = Entry(self.root , textvariable=self.set_withdraw,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_setWithdraw.place(x=500,y=230,width=180)
        txt_clrbalancewithdraw = Entry(self.root , textvariable=self.clrbalancewithdraw,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_clrbalancewithdraw.place(x=150,y=305,width=580)
        
        #=========Buttons===================
        #=========Checkboxes and Buttons===================
        #self.chk_balance_clear_set_received = Checkbutton(self.root, text='Balanced Clear and Set Received by Customer', font=('goudy old style', 12), bg='white',state=DISABLED, command=self.chk_balance_clear_set_received_click)
        self.chk_balance_clear_set_received = Checkbutton(self.root, text='Balanced Clear and Set Received by Customer',onvalue='Yes',offvalue='No',variable=self.var_chk, font=('goudy old style', 12), bg='white',state=DISABLED, command=self.chk_balance_clear_set_received_click)
        self.var_chk.set('No')
        self.chk_balance_clear_set_received.place(x=50, y=350)
        
        #self.chk_balance_not_clear_set_received = Checkbutton(self.root, text='Balanced Not Clear but Set Received by Customer', font=('goudy old style', 12), bg='white',state=DISABLED, command=self.chk_balance_not_clear_set_received_click)
        #self.chk_balance_not_clear_set_received.place(x=400, y=350)
        
        self.btn_paid = Button(self.root, text='Paid', command=self.paid,font=('goudy old style', 15), bg='#2196f3', fg='white', cursor='hand2',state=DISABLED)
        self.btn_paid.place(x=50, y=380, width=150, height=40)
        
        self.btn_unpaid = Button(self.root, text='Unpaid',command=self.unpaid, font=('goudy old style', 15), bg='#e74c3c', fg='white', cursor='hand2',state=DISABLED)
        self.btn_unpaid.place(x=220, y=380, width=150, height=40)
        
        self.btn_clear = Button(self.root, text='Clear', command=self.clear,font=('goudy old style', 15), bg='#607d8b', fg='white', cursor='hand2',state=DISABLED)
        self.btn_clear.place(x=390, y=380, width=150, height=40)
        
        #self.btn_clear = Button(self.root,text='Clear',command=self.clear,font=('goudy old style' , 15),bg='#607d8b',fg='white',state=DISABLED)
        #self.btn_clear.place(x=400,y=305,width=110,height=28)
        
        
        
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
                cur.execute('SELECT * FROM repair WHERE ' + self.var_searchby.get() + ' LIKE ?',('%' + self.var_searchtxt.get() + '%',))
                row = cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror('Error' , 'Not Repaired Yet',parent=self.root)
                else:
                    self.cust_id.set(row[0])
                    self.cust_contact.set(row[2])
                    self.cust_fault.set(row[4])
                    self.cust_aadhar.set(row[3])
                    self.cust_status.set(row[6])
                    self.cust_balance.set(row[5])
                    #balance,status,clearbalanced,setwithdraw,clearbalancedwithdraw
                    self.clr_balance.set(row[7])
                    self.set_withdraw.set(row[8])
                    self.clrbalancewithdraw.set(row[9])
                    self.chk_balance_clear_set_received.config(state=NORMAL)
                    #self.chk_balance_not_clear_set_received.config(state=NORMAL)
                    if self.clrbalancewithdraw.get()=='No':
                        self.btn_unpaid.config(state=NORMAL)
                    self.btn_clear.config(state=NORMAL)
                    #self.enable_paid_unpaid_buttons()
                    #pass
                
                
                #if len(rows)!=0:
                    #self.CustomerTable.delete(*self.CustomerTable.get_children())
                    #for row in rows:
                        #self.CustomerTable.insert('',END,values=row)
                #else:
                    #messagebox.showerror('Error','No records Found!',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
            
    #==============Checkbox Functionality======================================================
    
    def chk_balance_clear_set_received_click(self):
        if self.var_chk.get() == 'Yes':
            self.btn_paid.config(state=NORMAL) 
        else:
            self.btn_paid.config(state=DISABLED)

            
    
        
    #def chk_balance_clear_set_received_click(self):
        #if self.var_chk.get()=='Yes':
            #if (self.clrbalancewithdraw.get()=='No'):
                #self.btn_paid.config(state=NORMAL)
        #else:
            #self.btn_paid.config(state=DISABLED)
            
    #==============Paid Button Functionality======================================================
    def paid(self):
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
                cur.execute('SELECT * FROM repair WHERE cid=?' , (self.var_searchtxt.get(),))
                row = cur.fetchone()
                cur.execute("UPDATE repair SET balance='0', clearbalanced='yes', setwithdraw='yes', clearbalancedwithdraw='Payment done! Set received by customer on {}' WHERE {} LIKE ?".format(datetime.datetime.now(), self.var_searchby.get()), ('%' + self.var_searchtxt.get() + '%',))
                con.commit()
                
                messagebox.showinfo("Success", "Payment done! Data updated.")
                self.update_entry_boxes()  # Update entry boxes after payment
                self.var_chk.set('No')
                self.btn_paid.config(state=DISABLED)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)
            #cur.execute("UPDATE repair SET balance='0', clearbalanced='yes', setwithdraw='yes', clearbalancedwithdraw='Payment done! Set received by customer on {}' WHERE {} LIKE ?".format(datetime.datetime.now(), self.var_searchby.get()), ('%' + self.var_searchbyvalue.get() + '%',))
    
    #==============Unpaid Button Functionality======================================================
    def unpaid(self):
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
                #cur.execute('SELECT * FROM repair WHERE cid=?' , (self.var_searchtxt.get(),))
                #row = cur.fetchone()
                cur.execute("UPDATE repair SET setwithdraw='yes', clearbalancedwithdraw='Payment Not done! Set received by customer on {}' WHERE {} LIKE ?".format(datetime.datetime.now(), self.var_searchby.get()), ('%' + self.var_searchtxt.get() + '%',))
                con.commit()
                
                messagebox.showinfo("Success", "Data updated.")
                self.update_entry_boxes()  # Update entry boxes after unpaid
                self.btn_unpaid.config(state=DISABLED)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to : {str(ex)}', parent=self.root)
    
  
    #==============Clear Button==========================================
    def clear(self):
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')
        self.cust_id.set('')
        self.cust_contact.set('')
        self.cust_fault.set('')
        self.cust_aadhar.set('')
        self.cust_status.set('')
        self.cust_balance.set('')
        self.clr_balance.set('')
        self.set_withdraw.set('')
        self.clrbalancewithdraw.set('')
        self.var_chk.set('No')
        self.btn_clear.config(state=DISABLED)
        self.btn_unpaid.config(state=DISABLED)
        self.btn_paid.config(state=DISABLED)
        
    def update_entry_boxes(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM repair WHERE ' + self.var_searchby.get() + ' LIKE ?', ('%' + self.var_searchtxt.get() + '%',))
        row = cur.fetchone()
        if row:
            self.cust_id.set(row[0])
            self.cust_contact.set(row[2])
            self.cust_fault.set(row[4])
            self.cust_aadhar.set(row[3])
            self.cust_status.set(row[6])
            self.cust_balance.set(row[5])
            #balance,status,clearbalanced,setwithdraw,clearbalancedwithdraw
            self.clr_balance.set(row[7])
            self.set_withdraw.set(row[8])
            self.clrbalancewithdraw.set(row[9])
        con.close()
        
        
if __name__ == "__main__":
    root = Tk()
    obj = statusClass(root)
    root.mainloop()