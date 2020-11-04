from tkinter import *
import sqlite3
from tkinter.messagebox import *

con = sqlite3.Connection('DB.db')
cur = con.cursor()
def create():        
    cur.execute("create table if not exists login(username varchar(20) PRIMARY KEY, password varchar(20), name varchar(50))")
    
def create_admin():
    cur.execute("select * from login where username='admin'")
    status = cur.fetchall()
    if (len(status))==0:
        cur.execute("insert into login values ('admin', 'admin', 'Administrator')")
    else:
        flag=0

def sign_in(index_ui,username, password):
    try:
        cur.execute("select count(*) from login where username=? and password=?", (username, password))
    except:
        showerror('ERROR', 'SIGNIN FAILED')
        
        
    status = cur.fetchall()
    if status[0][0]==1:
        index_ui.destroy()
        dashboard(username)
    else:
        showerror('ERROR', 'SIGNING FAILED')

def details_ui(option):
    details_ui = Toplevel()
    details_ui.geometry("600x600+490+100")
    details_ui.resizable(0,0)
    bg = PhotoImage(file="images/windows_bg.gif")
    Label(details_ui, image=bg).place(x=0,y=0)
    cur.execute("create table if not exists complaint (fir_id varchar(10) PRIMARY KEY,  fname varchar(15), lname varchar(15),blood_group varchar(3), father_name varchar(30), gender varchar(6), age number(3), status varchar(10), address varchar(15), complaint varchar(15))") 

    Label(details_ui, text='FIR ID: ', font='Helvetica 11 bold',bg='#34383C',fg='white', borderwidth=0).place(x=140, y=80)
    fir_id = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    fir_id.place(x=320, y=80)

    Label(details_ui, text='First Name: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=140)
    fname = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    fname.place(x=320, y=140)
    
    Label(details_ui, text='Last Name: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=170)
    lname = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    lname.place(x=320, y=170)

    Label(details_ui, text='Blood Group: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=200)
    blood_group = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    blood_group.place(x=320, y=200)
    
    Label(details_ui, text="Father's Name: ", font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=230)
    father_name = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    father_name.place(x=320, y=230)

    Label(details_ui, text='Gender: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=260)
    gender = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    gender.place(x=320, y=260)

    Label(details_ui, text='Age: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=290)
    age = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    age.place(x=320, y=290)

    Label(details_ui, text='Status: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=320)
    status = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    status.place(x=320, y=320)

    Label(details_ui, text='Address: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=350)
    address = Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    address.place(x=320, y=350)

    Label(details_ui, text='Complaint: ', font='Helvetica 11 bold',bg='#34383C',fg='white').place(x=140, y=380)
    complaint= Entry(details_ui, font='Helvetica 11 bold', fg='#373E44')
    complaint.place(x=320, y=380)

   
    def insert_sql():
        try:
            cur.execute("insert into criminals values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (fid.get(),fname.get(), lname.get(), blood_group.get(), father_name.get(), gender.get(), age.get(), status.get(), address.get(), complaint.get()))
            showinfo('Inserted', 'Values are inserted')
        except:
            showerror('ERROR', 'Insertion failed')

    if(option=='insert'):
        Label(details_ui, text='Enter the Details ', borderwidth=0, bg='white',font=(12)).place(x=360, y=10)
        Button(details_ui, text='Insert', font='Helvetica 14 bold',bg='#373E44',fg='white',borderwidth=0, command=insert_sql).place(x=460, y=520)
    
    def update():
        try:        
            cur.execute("update criminals set lockup_id=?, fname=?, lname=?, blood_group=?, father_name=?, gender=?, age=?, status=?,crime=?,state=?, city=?, street_no=?, house_no=? where criminal_id=?",(lockup_id.get(), fname.get(), lname.get(), blood_group.get(), father_name.get(), gender.get(), age.get(), status.get(), crime.get(), state.get(), city.get(), street_no.get(), house_no.get(),criminal_id.get()))
            details_ui.destroy()
            showinfo('UPDATED', 'DATA UPDATED')
        except:
            showerror('ERROR', 'Failed to Update')
                      
    if(option=='update'):
        Label(details_ui, text='Enter Criminial ID to update', borderwidth=0, bg='white', font=(12)).place(x=324, y=10)
        Button(details_ui, text='Update', font='Helvetica 14 bold',bg='#373E44',fg='white',borderwidth=0, command=update).place(x=460, y=520)
    def view_sql(FIR_id):
        try:
            cur.execute("select * from criminals where criminal_id=?", [fir_id])
            details = cur.fetchall()[0]

            if(len(fname.get())!=0):
                fname.delete(0,END)
            fname.insert(0,details[2])
            if(len(lname.get())!=0):
                lname.delete(0,END)
            lname.insert(0,details[3])
            if(len(blood_group.get())!=0):
                blood_group.delete(0,END)
            blood_group.insert(0,details[4])
            if(len(father_name.get())!=0):
                father_name.delete(0,END)
            father_name.insert(0,details[5])
            if(len(gender.get())!=0):
                gender.delete(0,END)
            gender.insert(0,details[6])
            if(len(age.get())!=0):
                age.delete(0,END)
            age.insert(0,details[7])
            if(len(status.get())!=0):
                status.delete(0,END)
            status.insert(0,details[8])
            if(len(address.get())!=0):
                address.delete(0,END)
            address.insert(0,details[9])
            if(len(complaint.get())!=0):
                complaint.delete(0,END)
            complaint.insert(0,details[10])
            
                    
        except:
            showerror('ERROR', 'Complaint record is not available for this ID')
    if (option=='view'):
        Button(details_ui, text='VIEW', font='Helvetica 11 bold',bg='#373E44',fg='white',borderwidth=0, command=lambda:view_sql(fir_id.get())).place(x=460 , y=520)
        Label(details_ui, text='Enter Criminal id only', borderwidth=0, bg='white',font=(12)).place(x=360, y=10)
        
    details_ui.mainloop()

def create_acc():
    create_win = Toplevel()
    create_win.geometry("900x600+300+100")
    create_win.resizable(0,0)
    
    new_user_bg = PhotoImage(file="images/other_bg.gif")
    Label(create_win, image=new_user_bg).place(x=0, y=0)
    Label(create_win, text="CREATE AN ACCOUNT", font="Helvetica 15 bold", fg='white', bg='#34383C').place(x=331, y=60)

    username = Entry(create_win, font=(13))
    Label(create_win, text='Username', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=160)
        
    password = Entry(create_win, font=(13))
    Label(create_win, text='Password', fg = '#34383C', bg='white',font='Helvetica 11 bold').place(x=300, y=260)
        
    name = Entry(create_win, font=(13))
    Label(create_win, text='Name', fg = '#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=360)

        
    username.place(x=300, y=200)
    password.place(x=300, y=300)
    name.place(x=300, y=400)
  

    Button(create_win, text=' '*20+' SUBMIT'+' '*22, bg='#00BC90', fg='#34383C',font='Helvetica 15' ,borderwidth=0, command=lambda:submit()).place(x=270, y=490)
    def submit():
        try:
            cur.execute("insert into login values(?,?,?)", (username.get(), password.get(), name.get()))
            showinfo("CREATED", "ACCOUNT CREATED, NOW YOU CAN LOG IN TO THE APPLICATION")
            con.commit()
        except:
            showerror("ERROR", "YOUR ACCOUNT IS PROBABLY ALREADY REGISTERED , TRY LOGGING IN AND IF THE PROBLEM PERSISTS SEE HELP MENU")

    create_win.mainloop()

def remove():
    remove_ui = Toplevel()
    remove_ui.geometry("900x600+300+100")
    remove_ui.resizable(0,0)
    bg = PhotoImage(file="images/other_bg.gif")
    Label(remove_ui, image=bg).place(x=0,y=0)

    Label(remove_ui, text='Remove a Complaint',font="times 15 bold", fg='white', bg='#34383C').place(x=356, y=60)
    Label(remove_ui, text='FIR ID', fg = '#34383C', bg='white', font='Helvetica 18').place(x=374, y=280)
    to_remove = Entry(remove_ui, font=(13))
    to_remove.place(x=338, y=330)
    def execute_remove(to_remove):
        cur.execute("DELETE from complaint where fir_id = ?",[to_remove.get()])
    Button(remove_ui, text=' '*20 + 'REMOVE' + ' '*20,bg='#F85661', fg='#34383C', font='Helvetica 15',command=lambda:execute_remove(to_remove)).place(x=270, y=490)
    con.commit()
    remove_ui.mainloop()
    
def dashboard(username):
    dash_ui = Tk()
    dash_ui.geometry("900x600+300+100")
    dash_ui.resizable(0,0)
    bg = PhotoImage(file="images/background.gif")
    Label(dash_ui, relief="flat",image=bg).grid(row=0, column=0, rowspan=20, columnspan=20)

    user_bg = PhotoImage(file="images/user.gif")
    Label(dash_ui, image=user_bg,borderwidth=0).place(x=800 , y=6.5)
    
    logout = Button(dash_ui,bg='#16202C', borderwidth=0, command=lambda:dash_ui.destroy())
    logout_bg = PhotoImage(file="images/logout.gif")
    logout.config(image=logout_bg)
    logout.place(x=850, y=4)
    Label(dash_ui, text='DASHBOARD',fg='white',bg='#34383C', font='Helvetica 18 bold').place(x=420, y=10)
    Label(dash_ui, text='WELCOME '+username.upper() , bg='#34383C', fg='#0B8FCC', font = 'Helvetica 10 bold').place(x=45, y=50)
    
    add_bg = PhotoImage(file="images/plus.gif")
    Label(dash_ui, bg='#16202C', borderwidth=0, image=add_bg).place(x=10, y=105)
    Button(dash_ui, text='ADD', bg='#34383C', fg='#0B8FCC', font='4', borderwidth=0, command=lambda:details_ui('insert')).place(x=80, y=105)

    minus_bg = PhotoImage(file="images/minus.gif")
    Label(dash_ui, bg='#16202C', borderwidth=0,image=minus_bg).place(x=8.4,y=155)
    Button(dash_ui, text='REMOVE', bg='#34383C', fg='#0B8FCC', font='4', borderwidth=0, command=lambda:remove()).place(x=60, y=156)

    update_bg = PhotoImage(file="images/update.gif")
    Label(dash_ui, bg='#16202C', borderwidth=0,image=update_bg).place(x=8.4,y=205)
    Button(dash_ui, text='UPDATE', bg='#34383C', fg='#0B8FCC', font='4', borderwidth=0, command=lambda:details_ui('update')).place(x=60, y=207)

    view_bg = PhotoImage(file="images/view.gif")
    Label(dash_ui, bg='#16202C', borderwidth=0,image=view_bg).place(x=9.6,y=255)
    Button(dash_ui, text='VIEW', bg='#34383C', fg='#0B8FCC', font='4', borderwidth=0, command=lambda:details_ui('view')).place(x=72, y=258)
 
    add_user = Button(dash_ui,borderwidth=0,bg='#16202C', command=create_acc)
    add_user_bg = PhotoImage(file="images/add_user.gif")
    add_user.config(image=add_user_bg)
    add_user.place(x=20, y=480)

    graph = PhotoImage(file="images/splash.gif")
    Label(dash_ui, image=graph, borderwidth=0).place(x=205,y=76)
    dash_ui.mainloop()