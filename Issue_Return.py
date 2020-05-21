import pyodbc
from tkinter import *
import tkinter
from tkinter import messagebox
import datetime
import HomePage

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=.\;"
                      "Database=tester;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

def Page(r1):
    r1.destroy()
    root=Tk()
    root.title("Issue\Return Book")
    root.geometry("650x550")
    Label(root, text="Issue\Return Book",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Label(root, text="Enter Book ID:").pack()
    Entry_BID=Entry(root,textvariable="username")
    Entry_BID.pack()
    Label(root, text="").pack()

    Label(root, text="Enter Student ID:").pack()
    Entry_SI=Entry(root)
    Entry_SI.pack()
    Label(root, text="").pack()

    ra = PanedWindow()
    var = IntVar()
    R1 = Radiobutton(ra, text="Issue", variable=var, value=1)
    R2 = Radiobutton(ra, text="Return", variable=var, value=2)
    ra.add(R1)
    ra.add(R2)
    ra.pack()
    var.set(1)

    Label(root, text="").pack()
    b1=Button(root, text="Issue\Return", height=1,command=lambda:query(var,Entry_BID,Entry_SI)).pack()
    Label(root, text="").pack()
    b2=Button(root, text="GO Back", height=1,command=lambda:GoBack(root)).pack()

def query(var,Entry_BID,Entry_SI):
    BID=Entry_BID.get()
    SI=Entry_SI.get()
    if(len(BID)==0 or len(SI)==0):
        messagebox.showerror("Error", "Fill All Details")
        return
    try:
        int(BID)
        int(SI)
    except:
        messagebox.showerror("Error", "Fill Number Only")
        return
    if(checkBookID(BID)==0):
        messagebox.showerror("Error", "Invalid Book ID")
        return
    if(var.get()==1):
        if(checkUserNotIssueBook(SI)==1):
            if(BookAvilableNot(BID)==0):
                AvilableBookNo=GetBookDetails(BID,1)
                NewAvilableBookNo=AvilableBookNo-1;
                Update(NewAvilableBookNo,BID,SI,"Issue")
            else:
               messagebox.showerror("Error", "Book Not avilable.")
               return
        else:
            messagebox.showerror("Error", "This Student Already Issued 1 Book.")
            return
    if(var.get()==2):
        if(BookID_And_SID_are_same_issue(BID,SI)):
            AvilableBookNo=GetBookDetails(BID,1)
            NewAvilableBookNo=AvilableBookNo+1;
            Update(NewAvilableBookNo,BID,SI,"Return")
        else:
            messagebox.showerror("Error", "This Book is not issue for this student")
            return
    
def GoBack(root):
    HomePage.Page(root)

def checkBookID(ID):
    cursor.execute("SELECT * FROM BookDetail WHERE BookId= ? ",(ID))
    for row in cursor:
        return 1
    return 0

def checkUserNotIssueBook(ID):
    cursor.execute("SELECT * FROM Active_Book_Detail WHERE StudentID= ? ",(ID))
    for row in cursor:
        return 0
    return 1
def BookAvilableNot(ID):
    cursor.execute("SELECT NoAvilableBook FROM BookDetail WHERE BookId= ? ",(ID))
    for row in cursor:
        if(row[0]==0):
            return 1
    return 0
def GetBookDetails(ID,no):
    cursor.execute("SELECT * FROM BookDetail WHERE BookId= ? ",(ID))
    for row in cursor:
        if(no==1):#NoAvilableBook
            return row[3]
        if(no==2):#BookName
            return row[1]
        if(no==3):#AutherName
            return row[4]
        
def Update(No,BID,SI,isType):
    datenow = datetime.datetime.now()
    cursor.execute("UPDATE BookDetail SET NoAvilableBook =? WHERE BookId= ? ",(No,BID))
    cursor.commit()
    cursor.execute("INSERT INTO Active_Book_Detail VALUES(?,?,?,?,?)",(BID,GetBookDetails(BID,2),GetBookDetails(BID,3),SI,datenow))
    cursor.commit()
    cursor.execute("INSERT INTO Issue_Book_History VALUES(?,?,?,?,?)",(BID,GetBookDetails(BID,2), isType ,SI,datenow))
    cursor.commit()
    messagebox.showinfo("Done","Done")
