import pyodbc
from tkinter import *
from tkinter import messagebox
import BookDetails,RegisterNewBook,ActiveBook,IssueHistory,Issue_Return

def Page(r):
    r.destroy()
    root=Tk()
    root.title("Home Page")
    root.geometry("550x550")
    Label(root, text="Home Page",fg='red', font=("Helvetica", 16)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Button(root, text="Issue/Return Book", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:Issue_Return.Page(root)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()
    
    Button(root, text="Register New Book", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:RegisterNewBook.Page(root)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()
    
    Button(root, text="Show All Book Details", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:BookDetails.Page(root)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Button(root, text="Book Issues History", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:IssueHistory.Page(root)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()

    Button(root, text="Active Book Issue", height=1,fg='red', font=("Helvetica", 16),
           command=lambda:ActiveBook.Page(root)).pack()
    Label(root, text="",fg='red', font=("Helvetica", 16)).pack()
    
    root.mainloop()
