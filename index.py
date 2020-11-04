from tkinter import *
from tkinter.messagebox import *
import dash

dash.create()
dash.create_admin()

def index():
    index_ui = Tk()
    index_ui.geometry("900x600+300+100")
    index_ui.resizable(0,0)
    bg = '#000000'
    Label(index_ui).grid(row=0, column=0, rowspan=20, columnspan=20)

    Label(index_ui, text='Welcome', font='Helvetica 18 ', fg='white', bg='#34383C').place(x=50, y=230)
    Label(index_ui, text='FIR Management System', font='Helvetica 12 ', fg='white', bg='#34383C').place(x=50, y=260)
    Label(index_ui, text='Add / Remove / update and view the records using this interactive application', font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=290)
    

    logo = PhotoImage(file="images/logo.gif")
    Label(index_ui, image=logo,borderwidth=0).place(x=695,y=120)


    username_logo = PhotoImage(file="images/username_logo.gif")
    Label(index_ui, image=username_logo).place(x=600, y=260)
    username = Entry(index_ui, font=(14),fg='#0B8FCC')
    username.place(x=635, y=260)

    pass_logo = PhotoImage(file="images/password_logo.gif")
    Label(index_ui, image=pass_logo).place(x=600, y=290)
    password = Entry(index_ui, font=(14), show='*',fg='#0B8FCC')
    password.place(x=635, y=290)

    login_button = Button(index_ui, borderwidth=0,bg='#1A2E39',command=lambda:dash.sign_in(index_ui,username.get(), password.get()))
    login_button_bg = PhotoImage(file="images/login_button.GIF")
    login_button.config(image=login_button_bg)
    login_button.place(x=640 , y=350)

    help_button = Button(index_ui, borderwidth=0, command=show_help,bg='#00BC90')
    help_bg = PhotoImage(file="images/help.gif")
    help_button.config(image=help_bg)
    help_button.place(x=870, y=570)

    index_ui.mainloop()

def show_help():
    help_win = Toplevel()
    help_win.geometry("900x600+300+100")

    help_win_bg = PhotoImage(file="images/other_bg.gif")
    Label(help_win, image=help_win_bg).place(x=0, y=0)

    Label(help_win , text="Credits:", font="Helvetica 15 bold", fg='grey', bg='#34383C').place(x=400, y=60)
    Label(help_win , text='Kshitij Kumar Sinha', font = 'Helvetica 16 bold',bg='black', fg='#028CCA' ).place(x=280, y=250)
    Label(help_win , text='Shrey Sunil Ratna   ', font = 'Helvetica 16 bold',bg='black', fg='#028CCA' ).place(x=280, y=280)
    Label(help_win , text='Ankit Kumar             ', font = 'Helvetica 16 bold',bg='black', fg='#028CCA' ).place(x=280, y=310)
    help_win.mainloop()
    
root=Tk()
root.geometry("450x600+510+130")
root.resizable(0,0)
root.overrideredirect(1)
splash_image = PhotoImage(file="images/splash.gif")

def to_index():
    root.destroy()
    index()
    
Label(root, image = splash_image).place(x=0,y=0)
root.after(3000,to_index)
root.mainloop()