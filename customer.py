from tkinter import *
from tkinter import ttk , messagebox
from PIL import Image , ImageTk
import sqlite3
import datetime

class customerClass:
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
        self.cust_gender = StringVar()
        self.cust_contact = StringVar()
        self.cust_name = StringVar()
        self.cust_model = StringVar()
        self.cust_aadhar = StringVar()
        self.cust_mail = StringVar()
        self.cust_fault = StringVar()
        self.cust_charge = StringVar()
        #self.cust_address = StringVar()
        self.cust_advnc = StringVar()
        self.cust_rep = StringVar()
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
        title=Label(self.root,text='Customer Details',font=('goudy old style' , 15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)
        
        #======1st Row Content===========
        lbl_cust_id = Label(self.root,text='Cust. Id',font=('goudy old style' , 15),bg='white')
        lbl_cust_id.place(x=50,y=150)
        lbl_gender = Label(self.root,text='Gender',font=('goudy old style' , 15),bg='white')
        lbl_gender.place(x=380,y=150)
        lbl_contact = Label(self.root,text='Contact',font=('goudy old style' , 15),bg='white')
        lbl_contact.place(x=750,y=150)
        
        txt_cust_id = Entry(self.root , textvariable=self.cust_id,font=('goudy old style' , 15),bg='lightyellow',state=DISABLED)
        txt_cust_id.place(x=150,y=150,width=180)
        cmb_gender = ttk.Combobox(self.root , textvariable=self.cust_gender,values=('Select','Male','Female','Other'),state='readonly',justify=CENTER,font=('goudy old style' , 15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        
        txt_contact = Entry(self.root , textvariable=self.cust_contact,font=('goudy old style' , 15),bg='lightyellow')
        txt_contact.place(x=850,y=150,width=180)
        
        #=========2nd Row Content===========
        lbl_name = Label(self.root,text='Name',font=('goudy old style' , 15),bg='white')
        lbl_name.place(x=50,y=190)
        lbl_model = Label(self.root,text='Model Name',font=('goudy old style' , 15),bg='white')
        lbl_model.place(x=380,y=190)
        lbl_aadhar = Label(self.root,text='Aadhaar No',font=('goudy old style' , 15),bg='white')
        lbl_aadhar.place(x=750,y=190)
        
        txt_name = Entry(self.root , textvariable=self.cust_name,font=('goudy old style' , 15),bg='lightyellow')
        txt_name.place(x=150,y=190,width=180)
        txt_model = Entry(self.root , textvariable=self.cust_model,font=('goudy old style' , 15),bg='lightyellow')
        txt_model.place(x=500,y=190,width=180)
        txt_aadhar = Entry(self.root , textvariable=self.cust_aadhar,font=('goudy old style' , 15),bg='lightyellow')
        txt_aadhar.place(x=850,y=190,width=180)
        
        #=========3rd Row Content===========
        lbl_mail = Label(self.root,text='E-mail ID',font=('goudy old style' , 15),bg='white')
        lbl_mail.place(x=50,y=230)
        lbl_fault = Label(self.root,text='Fault',font=('goudy old style' , 15),bg='white')
        lbl_fault.place(x=380,y=230)
        lbl_charge = Label(self.root,text='Charges',font=('goudy old style' , 15),bg='white')
        lbl_charge.place(x=750,y=230)
        
        txt_mail = Entry(self.root , textvariable=self.cust_mail,font=('goudy old style' , 15),bg='lightyellow')
        txt_mail.place(x=150,y=230,width=180)
        txt_fault = Entry(self.root , textvariable=self.cust_fault,font=('goudy old style' , 15),bg='lightyellow')
        txt_fault.place(x=500,y=230,width=180)
        txt_charge = Entry(self.root , textvariable=self.cust_charge,font=('goudy old style' , 15),bg='lightyellow')
        txt_charge.place(x=850,y=230,width=180)
        
        #=========4th Row Content===========
        lbl_address = Label(self.root,text='Address',font=('goudy old style' , 15),bg='white')
        lbl_address.place(x=50,y=270)
        lbl_advance = Label(self.root,text='Advance',font=('goudy old style' , 15),bg='white')
        lbl_advance.place(x=380,y=270)
        lbl_duration = Label(self.root,text='Time Req.',font=('goudy old style' , 15),bg='white')
        lbl_duration.place(x=750,y=270)
        
        self.txt_address = Text(self.root,font=('goudy old style' , 15),bg='lightyellow')
        self.txt_address.place(x=150,y=270,width=180,height=60)
        txt_advance = Entry(self.root , textvariable=self.cust_advnc,font=('goudy old style' , 15),bg='lightyellow')
        txt_advance.place(x=500,y=270,width=180)
        txt_duration = Entry(self.root , textvariable=self.cust_rep,font=('goudy old style' , 15),bg='lightyellow')
        txt_duration.place(x=850,y=270,width=180)
        
        #=========Buttons===================
        btn_add = Button(self.root,text='Save',command=self.add,font=('goudy old style' , 15),bg='#2196f3',fg='white').place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text='Update',command=self.update,font=('goudy old style' , 15),bg='#4caf50',fg='white').place(x=620,y=305,width=110,height=28)
        btn_delete = Button(self.root,text='Delete',command=self.delete,font=('goudy old style' , 15),bg='#f44336',fg='white').place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text='Clear',command=self.clear,font=('goudy old style' , 15),bg='#607d8b',fg='white').place(x=860,y=305,width=110,height=28)
        
        #========Customer Details==========
        cust_frame = Frame(self.root,bd=3,relief=RIDGE)
        cust_frame.place(x=0,y=350,relwidth=1,height=150)
        
        scrolly = Scrollbar(cust_frame , orient=VERTICAL)
        scrollx = Scrollbar(cust_frame , orient=HORIZONTAL)
        
        self.CustomerTable = ttk.Treeview(cust_frame , columns=('cid','date','name','gender','device','contact','email','aadhar','problem','charges','advance','address','days_to_repair'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #======To make Work Scroll bar need to configure
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        
        
        self.CustomerTable.heading('cid',text='Customer ID')
        self.CustomerTable.heading('date',text='Order Date')
        self.CustomerTable.heading('name',text='Name')
        
        self.CustomerTable.heading('gender',text='Gender')
        self.CustomerTable.heading('device',text='Model Name')
        self.CustomerTable.heading('contact',text='Contact')
        
        self.CustomerTable.heading('email',text='Email ID')
        self.CustomerTable.heading('aadhar',text='Aadhar No.')
        self.CustomerTable.heading('problem',text='Fault')
        
        self.CustomerTable.heading('charges',text='Total Repairing Cost')
        self.CustomerTable.heading('advance',text='Advance Payment')
        self.CustomerTable.heading('address',text='Address')
        self.CustomerTable.heading('days_to_repair',text='Duration')
        
        self.CustomerTable['show'] = 'headings'
        self.CustomerTable.pack(fill=BOTH , expand=1)
        self.CustomerTable.bind('<ButtonRelease-1>',self.get_data)
        
        #=========Calling show() function================
        self.show()
        
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
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('',END,values=row)
                else:
                    messagebox.showerror('Error','No records Found!',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
        
    
    #=================CRUD Operations====================================================
    #=================Save Command=======================================================
    def add(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        current_date = datetime.date.today()
        try:
            
            if self.cust_contact=='':
                messagebox.showerror('Error' , 'Customer Contact Number must be required',parent=self.root)
            else:
                cur.execute('Insert into customer (date,name,gender,device,contact,email,aadhar,problem,charges,advance,address,days_to_repair) values(?,?,?,?,?,?,?,?,?,?,?,?)',(
                    current_date,
                    self.cust_name.get(),
                    self.cust_gender.get(),
                    self.cust_model.get(),
                    self.cust_contact.get(),
                    self.cust_mail.get(),
                    self.cust_aadhar.get(),
                    self.cust_fault.get(),
                    self.cust_charge.get(),
                    self.cust_advnc.get(),
                    self.txt_address.get('1.0' , END),
                    self.cust_rep.get()
                ))
                con.commit()
                # Fetch the last inserted cust_id
                last_inserted_id = cur.lastrowid

                # Show a messagebox with the last inserted cust_id
                messagebox.showinfo('Success', f'Customer Details added successfully\nCustomer ID: {last_inserted_id}', parent=self.root)

                self.show()
                #messagebox.showinfo('Success','Customer Details added successfully',parent=self.root)
                #self.show()
                
                
    
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
            
    #==============Update Command==========================================
    def update(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        current_date = datetime.date.today()
        try:
            
            if self.cust_id=='':
                messagebox.showerror('Error' , 'Customer ID must be required',parent=self.root)
            else:
                cur.execute('select * from customer where cid=?',(self.cust_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error' , 'Invalid Customer ID',parent=self.root)
                else:
                    cur.execute('Update customer set name=?,gender=?,device=?,contact=?,email=?,aadhar=?,problem=?,charges=?,advance=?,address=?,days_to_repair=? where cid=?',(
                    #current_date,
                    self.cust_name.get(),
                    self.cust_gender.get(),
                    self.cust_model.get(),
                    self.cust_contact.get(),
                    self.cust_mail.get(),
                    self.cust_aadhar.get(),
                    self.cust_fault.get(),
                    self.cust_charge.get(),
                    self.cust_advnc.get(),
                    self.txt_address.get('1.0' , END),
                    self.cust_rep.get(),
                    self.cust_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Customer Details Updated successfully',parent=self.root)
                    self.show()
                
                
    
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
            
    #=======================btn_Delete Customer Record===========================
    def delete(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        current_date = datetime.date.today()
        try:
            
            if self.cust_id=='':
                messagebox.showerror('Error' , 'Customer ID must be required',parent=self.root)
            else:
                cur.execute('select * from customer where cid=?',(self.cust_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error' , 'Invalid Customer ID',parent=self.root)
                else:
                    op = messagebox.askyesno('Confirmation' , 'Do you really want to delete record?',parent=self.root)
                    if op==True:
                        cur.execute('delete from customer where cid=?',(self.cust_id.get(),))
                        con.commit()
                        messagebox.showinfo('Success','Customer Deleted successfully',parent=self.root)
                        self.clear()
                    
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
    #=======================btn_Clear Form Fields=================================
    def clear(self):
        self.cust_id.set('')
        self.cust_name.set(''),
        self.cust_gender.set('Select'),
        self.cust_model.set(''),
        self.cust_contact.set(''),
        self.cust_mail.set(''),
        self.cust_aadhar.set(''),
        self.cust_fault.set(''),
        self.cust_charge.set(''),
        self.cust_advnc.set(''),
        self.txt_address.delete('1.0' , END),
        #self.txt_address.insert(END,row[11]),
        self.cust_rep.set('')
        self.show()
        
            
    
    
    
    
    #==============Display Record In Tree View Window========================
    def show(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        #current_date = datetime.date.today()
        try:
            cur.execute('select * from customer')
            rows = cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error' , f'Error due to : {str(ex)}',parent=self.root)
            
    #===============getData When selected from Treeview======================
    def get_data(self,ev):
        f = self.CustomerTable.focus()
        content=(self.CustomerTable.item(f))
        row=content['values']
        #print(row)
        self.cust_id.set(row[0])
        self.cust_name.set(row[2]),
        self.cust_gender.set(row[3]),
        self.cust_model.set(row[4]),
        self.cust_contact.set(row[5]),
        self.cust_mail.set(row[6]),
        self.cust_aadhar.set(row[7]),
        self.cust_fault.set(row[8]),
        self.cust_charge.set(row[9]),
        self.cust_advnc.set(row[10]),
        self.txt_address.delete('1.0' , END),
        self.txt_address.insert(END,row[11]),
        self.cust_rep.set(row[12])
        
    


if __name__ == "__main__":
    root = Tk()
    obj = customerClass(root)
    root.mainloop()
