import pyodbc
from tkinter import *
from tkinter import messagebox
import HomePage

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=.\;"
                      "Database=tester;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

def Page(r):
    r.destroy()
    root=Tk()
    root.title("Login")
    root.geometry("550x550")
    Label(root, text="Login Page",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    username = StringVar()
    password = StringVar()

    Label(root, text="Enter User Name",fg='red', font=("Helvetica", 16)).pack()    
    Username = Entry(root,font=("Helvetica", 16),fg='red',textvariable=username)
    Username.pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Label(root, text="Enter Password",fg='red', font=("Helvetica", 16)).pack()
    Password = Entry(root,font=("Helvetica", 16),fg='red',textvariable=password,show="*")
    Password.pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Button(root, text="Login", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:CheckLogin(root,Username,Password)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()
    
    root.mainloop()

def CheckLogin(root,Username,Password):
    user=Username.get().strip()
    pwd=Password.get().strip()
    if(len(user)==0 or len(pwd)==0):
        messagebox.showerror("Error", "Fill All Details")
        return
    try:
        cursor.execute('SELECT * FROM loginD WHERE username= ?',user)
        isl=0
        for row in cursor:
            if(row[1].strip()==pwd):
                isl=1
                Succes(root)
            else:
                messagebox.showerror("Error", "Incorrect password")
        if(isl==1):
            messagebox.showerror("Error", "Incorrect User Name")
        
    except:
        messagebox.showerror("Error","Database connection problem!!!")

def Succes(r):
    HomePage.Page(r)
    
t=Tk()
Page(t)
t.mainloop()
