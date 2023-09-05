from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image , ImageTk
import time 
from customer import customerClass
from repairs import repClass
from statuss import statusClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Sanskar Mobile Repairing Shop")
        self.root.config(bg='white')
    

        heading = Label(self.root,text ='Mobile Repairing Management System',font=('Verdana' , 30 , 'bold'),bg='#010c48' , fg='white',anchor='w').place(x=0,y=0,relwidth=1,height=70)
        
        #btn logout
        btn_logout = Button(self.root , text='Log Out' , font=('Verdana' , 15 , 'bold'),bg='yellow',cursor='hand2').place(x=1200,y=18,width=110,height=40)
        
        #lbl_clock_date_time
        self.lbl_clock = Label(self.root,text ='Welcome to Sanskar Mobile Shop\t\t\t Date : dd-mm-yyyy\t\t\t Time : HH:MM:SS',font=('Verdana' , 15 ),bg='#4d636d' , fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #left Menu Frame
        self.MenuLogo = Image.open('image/mobilephone.jpg')
        self.MenuLogo = self.MenuLogo.resize((200,200) , Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        leftMenu = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        leftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menu = Label(leftMenu , image=self.MenuLogo)
        lbl_menu.pack(side=TOP , fill=X)
        
        self.icon = Image.open('image/bulletsicon.png')
        self.icon = self.icon.resize((30 , 30) , Image.Resampling.LANCZOS)
        self.icon = ImageTk.PhotoImage(self.icon)
        
        lbl_menu = Label(leftMenu , text='Menu' , font=('Verdana' , 15),bg='#009688').pack(side=TOP , fill=X)
        btn_cust = Button(leftMenu , text='Customer' , command=self.customers,image=self.icon,compound=LEFT,padx=15,anchor='w',font=('Verdana' , 15),bg='white',bd=3,cursor='hand2').pack(side=TOP , fill=X)
        btn_repair = Button(leftMenu , text='Repair' , command=self.repair,image=self.icon,compound=LEFT,padx=15,anchor='w',font=('Verdana' , 15),bg='white',bd=3,cursor='hand2').pack(side=TOP , fill=X)
        btn_status = Button(leftMenu , text='Status' , command=self.status,image=self.icon,compound=LEFT,padx=15,anchor='w',font=('Verdana' , 15),bg='white',bd=3,cursor='hand2').pack(side=TOP , fill=X)
        btn_bill = Button(leftMenu , text='Bill' , image=self.icon,compound=LEFT,padx=15,anchor='w',font=('Verdana' , 15),bg='white',bd=3,cursor='hand2').pack(side=TOP , fill=X)
        # Add your content elements here...
        #======fotter=========
        self.lbl_footer = Label(self.root,text ='RMS - Repairing Mobile System | Developed by Ankit Jain \n For any Technical Issue Contact Us : 799XXXXX29',font=('Verdana' , 10 ),bg='#4d636d' , fg='white').pack(side=BOTTOM,fill=X)
        self.update_date_time()
        
    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S %p")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text = f'Welcome to Sanskar Mobile Shop\t\t\t Date : {str(date_)}\t\t\t Time : {str(time_)}')
        self.lbl_clock.after(200,self.update_date_time)
        # Close button to close the window
        #self.close_button = ttk.Button(root, text="Close", command=self.close_window)
        #self.close_button.pack(pady=10)
        
    
        
    #========Customer Method=======================
   
    def customers(self):
        self.new_win = Toplevel(self.root)
        #self.new_win.grab_set()
        #self.root.withdraw()
        self.cust_obj = customerClass(self.new_win)
    
     
    #=========Repair Module=========================
    def repair(self):
        self.new_win = Toplevel(self.root)
        self.cust_obj = repClass(self.new_win)
        
    #=========Status Module=========================
    def status(self):
        self.new_win = Toplevel(self.root)
        self.cust_obj = statusClass(self.new_win)
        
        
    #def close_window(self):
        #self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
