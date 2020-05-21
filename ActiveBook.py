import pyodbc
from tkinter import *
import tkinter
from tkinter import messagebox
import HomePage
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=.\;"
                      "Database=tester;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

def ClearList(Bookid,Bookname,Authername,IssueDate,StudentID):
    Bookid.delete(0, tkinter.END)
    Bookname.delete(0, tkinter.END)
    Authername.delete(0, tkinter.END)
    IssueDate.delete(0, tkinter.END)
    StudentID.delete(0, tkinter.END)
def Page(r):
    r.destroy()
    root=Tk()
    root.title("Active Issues Book Details")
    root.geometry("650x550")
    Label(root, text="Active Issues Book Details",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    ra = PanedWindow()
    var = IntVar()
    R1 = Radiobutton(ra, text="Book ID", variable=var, value=1)
    R2 = Radiobutton(ra, text="Student ID", variable=var, value=2)
    R3 = Radiobutton(ra, text="Book Name", variable=var, value=3)
    R4 = Radiobutton(ra, text="Auther Name", variable=var, value=4)
    search_entry = Entry(ra)
    b1=Button(ra, text="Search", height=1,command=lambda:Search_query(var,search_entry))
    b2=Button(ra, text="Refresh", height=1,command=lambda:AllData())
    b3=Button(ra, text="GO Back", height=1,command=lambda:GoBack(root))
    
    ra.add(R1)
    ra.add(R2)
    ra.add(R3)
    ra.add(R4)
    ra.add(search_entry)
    ra.add(b1)
    ra.add(b2)
    ra.add(b3)
    ra.pack()
    var.set(1)
    head = PanedWindow()
    l1=Label(head,text="Book ID  \t\t ",fg='blue')
    l2=Label(head,text="   Book Name  \t",fg='blue')
    l3=Label(head,text="       Auther Name\t",fg='blue')
    l4=Label(head,text="Student ID\t",fg='blue')
    l5=Label(head,text="\tDate of Issue book",fg='blue')
    head.add(l1)
    head.add(l4)
    head.add(l2)
    head.add(l3)
    
    head.add(l5)
    head.pack()
    m1 = PanedWindow()
    scrollbar = Scrollbar(root) 
    Bookid = Listbox(m1)
    Bookname = Listbox(m1)
    Authername = Listbox(m1)
    StudentID = Listbox(m1)
    IssueDate = Listbox(m1)
    def AllData():
        ClearList(Bookid,Bookname,Authername,IssueDate,StudentID)
        cursor.execute('SELECT * FROM Active_Book_Detail ORDER BY IssueDate DESC')
        for row in cursor:
            Bookid.insert(0, row[0])
            Bookname.insert(0, str(row[1]).strip())
            Authername.insert(0, str(row[2]).strip())
            StudentID.insert(0, row[3])
            IssueDate.insert(0, row[4])
    def yview(*args):
        Bookid.yview(*args)
        Bookname.yview(*args)
        Authername.yview(*args)
        StudentID.yview(*args)
        IssueDate.yview(*args)
    try:
        AllData()
    except:
            print("Database connection problem!!!")
    Bookid.config(yscrollcommand = scrollbar.set)
    Bookname.config(yscrollcommand = scrollbar.set)
    Authername.config(yscrollcommand = scrollbar.set)
    StudentID.config(yscrollcommand = scrollbar.set)
    IssueDate.config(yscrollcommand = scrollbar.set)
    m1.add(Bookid)
    m1.add(StudentID)
    m1.add(Bookname)
    m1.add(Authername)
    
    m1.add(IssueDate)
    
    scrollbar.config(command =yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    m1.pack(side=LEFT, fill=Y)

    def Search_query(var,search_entry):
        varNo=var.get()
        if(len(search_entry.get())==0):
            messagebox.showerror("Error", "Enter something first")
            return
        if(varNo==1):
            try:
                toSearch=int(search_entry.get())
            except:
                messagebox.showerror("Error", "Enter number only")
                return
            ClearList(Bookid,Bookname,Authername,IssueDate,StudentID)
            cursor.execute("SELECT * FROM Active_Book_Detail WHERE BookID= ? ORDER BY IssueDate DESC",(toSearch))
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                Authername.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                IssueDate.insert(0, row[4])
        if(varNo==2):
            try:
                toSearch=int(search_entry.get())
            except:
                messagebox.showerror("Error", "Enter number only")
                return
            ClearList(Bookid,Bookname,Authername,IssueDate,StudentID)
            cursor.execute("SELECT * FROM Active_Book_Detail WHERE StudentID = ? ORDER BY IssueDate DESC",(toSearch))
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                Authername.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                IssueDate.insert(0, row[4])
        if(varNo==3):
            toSearch='%'+search_entry.get()+'%'
            ClearList(Bookid,Bookname,Authername,IssueDate,StudentID)
            cursor.execute("SELECT * FROM Active_Book_Detail WHERE BookName LIKE '%s' ORDER BY IssueDate DESC"%toSearch)
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                Authername.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                IssueDate.insert(0, row[4])
        if(varNo==4):
            toSearch='%'+search_entry.get()+'%'
            ClearList(Bookid,Bookname,Authername,IssueDate,StudentID)
            cursor.execute("SELECT * FROM Active_Book_Detail WHERE AuthorName LIKE '%s' ORDER BY IssueDate DESC"%toSearch)
            print(toSearch)
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                Authername.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                IssueDate.insert(0, row[4])
    root.mainloop()
def GoBack(root):
    HomePage.Page(root)
