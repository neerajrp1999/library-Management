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
    root.title("Register New Book")
    root.geometry("550x550")
    Label(root, text="Register New Book",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()
    
    Label(root, text="Enter Book ID:").pack()
    Entry_BID=Entry(root,textvariable="username")
    Entry_BID.pack()
    Label(root, text="").pack()

    Label(root, text="Enter Book Name:").pack()
    Entry_BN=Entry(root)
    Entry_BN.pack()
    Label(root, text="").pack()

    Label(root, text="Enter Book Author Name:").pack()
    Entry_BAN=Entry(root)
    Entry_BAN.pack()
    Label(root, text="").pack()

    Label(root, text="Enter Book Price:").pack()
    Entry_BP=Entry(root)
    Entry_BP.pack()
    Label(root, text="").pack()

    Label(root, text="Enter Number of Book:").pack()
    Entry_NB=Entry(root)
    Entry_NB.pack()
    Label(root, text="").pack()
    
    Button(root, text="Register", height=1,command=lambda:Register(Entry_BID,Entry_BN,Entry_BAN,Entry_BP,Entry_NB)).pack()
    Label(root, text="").pack()

    Button(root, text="GO BACK", height=1,command=lambda:GoBack(root)).pack()
    Label(root, text="").pack()
    root.mainloop()
def Register(Entry_BID,Entry_BN,Entry_BAN,Entry_BP,Entry_NB):
    if(len(Entry_BID.get())==0 and len(Entry_BN.get())==0 and len(Entry_BAN.get())==0
           and len(Entry_BP.get())==0 and len(Entry_NB.get())==0):
        messagebox.showerror("Error", "Enter All Field")
        return
    try:
        int(Entry_BID.get())
        int(Entry_NB.get())
        int(Entry_BP.get())
    except:
        messagebox.showerror("Error", "Enter Number only in Book ID and Number of Book")
    if(bookidExist(Entry_BID)==True):
        messagebox.showerror("Error", "This book id already exist")
        return
    cursor.execute("INSERT INTO BookDetail VALUES(?,?,?,?,?,?)",(Entry_BID.get(),Entry_BN.get(),Entry_NB.get(),Entry_NB.get(),Entry_BAN.get(),Entry_BP.get()))
    cursor.commit()
    messagebox.showinfo("Done", "Registation Done")
def bookidExist(Entry_BID):
    cursor.execute("SELECT * FROM BookDetail WHERE BookId= ? ",(Entry_BID.get()))
    s=0
    for i in cursor:
        s=1
    if(s==0):
        return False
    else:
        return True
def GoBack(root):
    HomePage.Page(root)
    
