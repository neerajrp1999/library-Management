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

def ClearList(Bookid,Bookname,I_R,DateIssue,StudentID):
    Bookid.delete(0, tkinter.END)
    Bookname.delete(0, tkinter.END)
    I_R.delete(0, tkinter.END)
    DateIssue.delete(0, tkinter.END)
    StudentID.delete(0, tkinter.END)
def Page(r):
    r.destroy()
    root=Tk()
    root.title("Issues Book History")
    root.geometry("650x550")
    Label(root, text="Issues Book History",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    ra = PanedWindow()
    var = IntVar()
    R1 = Radiobutton(ra, text="Book ID", variable=var, value=1)
    R2 = Radiobutton(ra, text="Student ID", variable=var, value=2)
    R3 = Radiobutton(ra, text="Book Name", variable=var, value=3)
    search_entry = Entry(ra)
    b1=Button(ra, text="Search", height=1,command=lambda:Search_query(var,search_entry))
    b2=Button(ra, text="Refresh", height=1,command=lambda:AllData())
    b3=Button(ra, text="GO Back", height=1,command=lambda:GoBack(root))
    
    ra.add(R1)
    ra.add(R2)
    ra.add(R3)
    ra.add(search_entry)
    ra.add(b1)
    ra.add(b2)
    ra.add(b3)
    ra.pack()
    var.set(1)
    head = PanedWindow()
    l1=Label(head,text="Book ID  \t\t ",fg='blue')
    l2=Label(head,text="Student ID\t",fg='blue')
    l3=Label(head,text="   Book Name  \t",fg='blue')
    l4=Label(head,text="       Issue\Return\t",fg='blue')
    l5=Label(head,text="\tDate \t\t",fg='blue')
    head.add(l1)
    head.add(l2)
    head.add(l3)
    head.add(l4)
    head.add(l5)
    head.pack()
    m1 = PanedWindow()
    scrollbar = Scrollbar(root) 
    Bookid = Listbox(m1)
    Bookname = Listbox(m1)
    I_R = Listbox(m1)
    StudentID = Listbox(m1)
    DateIssue = Listbox(m1)
    def AllData():
        ClearList(Bookid,Bookname,I_R,DateIssue,StudentID)
        cursor.execute('SELECT * FROM Issue_Book_History ORDER BY DateIssue ASC')
        for row in cursor:
            Bookid.insert(0, row[0])
            Bookname.insert(0, str(row[1]).strip())
            I_R.insert(0, str(row[2]).strip())
            StudentID.insert(0, row[3])
            DateIssue.insert(0, row[4])
    def yview(*args):
        Bookid.yview(*args)
        Bookname.yview(*args)
        I_R.yview(*args)
        StudentID.yview(*args)
        DateIssue.yview(*args)
    try:
        AllData()
    except:
            print("Database connection problem!!!")
    Bookid.config(yscrollcommand = scrollbar.set)
    Bookname.config(yscrollcommand = scrollbar.set)
    I_R.config(yscrollcommand = scrollbar.set)
    StudentID.config(yscrollcommand = scrollbar.set)
    DateIssue.config(yscrollcommand = scrollbar.set)
    m1.add(Bookid)
    m1.add(StudentID)
    m1.add(Bookname)
    m1.add(I_R)
    
    m1.add(DateIssue)
    
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
            ClearList(Bookid,Bookname,I_R,DateIssue,StudentID)
            cursor.execute("SELECT * FROM Issue_Book_History WHERE BookID= ? ORDER BY DateIssue ASC",(toSearch))
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                I_R.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                DateIssue.insert(0, row[4])
        if(varNo==2):
            try:
                toSearch=int(search_entry.get())
            except:
                messagebox.showerror("Error", "Enter number only")
                return
            ClearList(Bookid,Bookname,I_R,DateIssue,StudentID)
            cursor.execute("SELECT * FROM Issue_Book_History WHERE StudentID = ? ORDER BY DateIssue ASC",(toSearch))
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                I_R.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                DateIssue.insert(0, row[4])
        if(varNo==3):
            toSearch='%'+search_entry.get()+'%'
            ClearList(Bookid,Bookname,I_R,DateIssue,StudentID)
            cursor.execute("SELECT * FROM Issue_Book_History WHERE BookName LIKE '%s' ORDER BY DateIssue ASC"%toSearch)
            for row in cursor:
                Bookid.insert(0, row[0])
                Bookname.insert(0, str(row[1]).strip())
                I_R.insert(0, str(row[2]).strip())
                StudentID.insert(0, row[3])
                DateIssue.insert(0, row[4])
    root.mainloop()
def GoBack(root):
    HomePage.Page(root)
