import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def selection():
    gender = ""
    selected = int(radio.get())
    if selected == 1:
        gender = "Male"
    elif selected == 2:
        gender = "Female"
    elif selected == 3:
        gender = "Others"
    else:
        gender = "NULL"
    return gender


def check_fields():
    if nameField.get() == "":
        messagebox.showerror("Failed", "All Fields are Mandatory!")
    else:
        return


def details_page():
    top = Toplevel()
    top.title('Details')
    top.geometry("1200x1000")
    

    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute("select * from registration where name = (?)",
                  (login_name.get(),))
        val = c.fetchone()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close() 

    label_reg = Label(top, text="REGISTRATION  DETAILS:",fg="goldenrod", font=('Arial Black', 20))
    label_reg.place(relx=0.1, rely=0.1)
    
    label_name = Label(top, text="NAME:", font=('bold', 16))
    label_name.place(relx=0.2, rely=0.2)

    fetch_name = Label(top, text=f"{val[1]}", font=('bolf', 13))
    fetch_name.place(relx=0.3, rely=0.2)

    label_age = Label(top, text="AGE:",font=('bold', 16))
    label_age.place(relx=0.2, rely=0.3)

    fetch_age = Label(top, text=f"{val[2]}", font=('bolf', 13))
    fetch_age.place(relx=0.3, rely=0.3)
     
    label_dob = Label(top, text="DATE OF BIRTH:", font=('bold', 16))
    label_dob.place(relx=0.2, rely=0.4)

    fetch_dob = Label(top, text=f"{val[3]}", font=('bolf', 13))
    fetch_dob.place(relx=0.4, rely=0.4)
        
    label_pob = Label(top, text="PLACE OF BIRTH:", font=('bold',16))
    label_pob.place(relx=0.2, rely=0.5)

    fetch_pob = Label(top, text=f"{val[4]}", font=('bolf', 13))
    fetch_pob.place(relx=0.4, rely=0.5)

    label_gender = Label(top, text="GENDER:", font=('bold',16))
    label_gender.place(relx=0.2, rely=0.6)

    fetch_gender = Label(top, text=f"{val[5]}", font=('bolf', 13))
    fetch_gender.place(relx=0.3, rely=0.6)

    label_father = Label(top, text="FATHER:", font=('bold',16))
    label_father.place(relx=0.2, rely=0.7)

    fetch_father = Label(top, text=f"{val[6]}", font=('bolf', 13))
    fetch_father.place(relx=0.3, rely=0.7)

    label_mother = Label(top, text="MOTHER:", font=('bold',16))
    label_mother.place(relx=0.2, rely=0.8)

    fetch_mother = Label(top, text=f"{val[7]}", font=('bolf', 13))
    fetch_mother.place(relx=0.3, rely=0.8)

    label_address = Label(top, text="ADDRESS:", font=('bold',16))
    label_address.place(relx=0.2, rely=0.9)

    fetch_address = Label(top, text=f"{val[8]}", font=('bolf', 13))
    fetch_address.place(relx=0.3, rely=0.9)


def add_to_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute(
            "insert into registration (name, age, dob, pob, gender, fathername, mothername, address) values (?,?,?,?,?,?,?,?,?)", (
                nameField.get(),
                int(ageField.get()),
                dobField.get(),
                pobField.get(),
                selection(),
                fatherField.get(),
                motherField.get(),
                addrField.get(),
            
            ))
        c.execute("select * from registration")
        conn.commit()
        messagebox.showinfo(
            "Success", "Registration Complete"
        )
    except Exception as e:
        print(f"Error Has Occured Not able to connect to the Database :(\n{e}")
    finally:
        conn.close()


def login_db():
    try:
        conn = sqlite3.connect('db.sql')
        c = conn.cursor()
        c.execute("select * from registration where name = (?)",
                  (login_name.get(),))
        val = c.fetchone()
        if login_name.get() == val[1]:
            messagebox.showinfo("Success", "User Logged Successfully")
        conn.commit()
        details_page()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def login():
    login_db()


def register():
    print(selection())  # get the radio button value
    check_fields()
    add_to_db()


def existing_user():
    top = Toplevel()
    top.title('Login')
    top.geometry("900x450")
    canvas2=Canvas(top,width=1300,height=700)
    image2=ImageTk.PhotoImage(Image.open("C:\\Users\\DINESH\Desktop\\b.jpg"))
    canvas2.create_image(0,0,anchor=NW,image=image2)
    canvas2.pack()
    head = Label(top, text='LOGIN', font=('Arial Black', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    b_name = Label(top, text='NAME', font=('Arial Black', 14))
    b_name.place(relx=0.1, rely=0.4, anchor=W)
    global login_name
    login_name = Entry(top)
    login_name.place(relx=0.9, rely=0.4, anchor=E)
    login_name.config(width=30)

    b_auth = Label(top, text='PASSWORD', font=('Arial Black', 14))
    b_auth.place(relx=0.1, rely=0.6, anchor=W)
    global login_password
    login_password = Entry(top,show="*")
    login_password.place(relx=0.9, rely=0.6, anchor=E)
    login_password.config(width=30)

    bname = Button(top, text="SUBMIT", font=(
        "Arial Black", 10), bg="white",fg="green", command=login)
    bname.place(relx=0.2, rely=0.8, anchor=W)
    bname.config(height=1, width=10)

    bauth = Button(top, text="CANCEL", font=("Arial Black", 10),
                   bg="white",fg="red", command=top.destroy)
    bauth.place(relx=0.8, rely=0.8, anchor=E)
    bauth.config(height=1, width=10)
    top.mainloop()

def new_user():
    top = Toplevel()
    top.title('REGISTRATION')
    top.geometry("600x600")
    canvase3=Canvas(top,width=800,height=700)
    image3=ImageTk.PhotoImage(Image.open("C:\\Users\\DINESH\Desktop\\b.jpg"))
    canvase3.create_image(0,0,anchor=NW,image=image3)
    canvase3.pack()
    global radio
    radio = IntVar()

    frame1 = Frame(top,bg="skyblue")
    frame1.place(relx=0, rely=0, width=600, height=600)

    registerTitle = Label(frame1, text="REGISTRATION",
                          font=("Arial Black", 15), bg="skyblue",fg="black")
    registerTitle.place(relx=0.5, rely=0.03, anchor=CENTER)

    # Name Label and Field
    global nameField
    nameLabel = Label(frame1, text="Name:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black")
    nameLabel.place(x=20, y=70)
    nameField = Entry(frame1, font=("Helvetica", 13), bg="white")
    nameField.place(x=150, y=70, width=250)

    # Age Label and Age Field
    global ageField
    ageLabel = Label(frame1, text="Age:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black")
    ageLabel.place(x=20, y=110)
    ageField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    ageField.place(x=150, y=110, width=250)     # y + 40

    # DoB Label and Field
    global dobField
    dobLabel = Label(frame1, text="Date of Birth:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black")
    dobLabel.place(x=20, y=150)
    dobField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    dobField.place(x=150, y=150, width=250)

    # PoB Label and Field
    global pobField
    pobLabel = Label(frame1, text="Place of Birth:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black")
    pobLabel.place(x=20, y=190)
    pobField = Entry(frame1, font=("Helvetica", 13),
                     bg='white')
    pobField.place(x=150, y=190, width=250)

    # gender Label and Field
    genderLabel = Label(frame1, text="Gender:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black").place(x=20, y=230)
    maleField = Radiobutton(
        frame1, text="Male", variable=radio, value=1, command=selection, bg='white').place(x=150, y=230)
    femaleField = Radiobutton(
        frame1, text="Female", variable=radio, value=2, command=selection, bg='white').place(x=220, y=230)
    otherField = Radiobutton(
        frame1, text="Others", variable=radio, value=3, command=selection, bg='white').place(x=290, y=230)

    # Fathername Label and Field
    global fatherField
    fatherLabel = Label(frame1, text="Father's Name:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black").place(x=20, y=270)
    fatherField = Entry(frame1, font=("Helvetica", 13),
                        bg='white')
    fatherField.place(x=150, y=270, width=250)

    # mothername Label and Field
    global motherField
    motherLabel = Label(frame1, text="Mother's Name:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black").place(x=20, y=310)
    motherField = Entry(frame1, font=("Helvetica", 13),
                        bg='white')
    motherField.place(x=150, y=310, width=250)

    # address Label and Age Field
    global addrField
    addrLabel = Label(frame1, text="Address:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black").place(x=20, y=350)
    addrField = Entry(frame1, font=("Helvetica", 13),
                      bg='white')
    addrField.place(x=150, y=350, width=250)
    global passField
    passLabel = Label(frame1, text="Password:*", font=(
        "Helvetica", 13), bg="skyblue",fg="black")
    passLabel.place(x=20, y=390)
    passField = Entry(frame1, font=("Helvetica", 13), bg="white")
    passField.place(x=150, y=390, width=250)


    # T&C
    tandc = Checkbutton(
        frame1, text="I Agree to the Terms & Conditions", bg='skyblue', font=("Calibri", 13), onvalue=1, offvalue=0).place(x=20, y=450)

    # Register
    registerBtn = Button(frame1, text='Register', font=('Arial Black', 13),fg="green", padx=15, pady=5, cursor="hand2",
                         command=register).place(x=20, y=500)

    cancelBtn = Button(frame1, text='Cancel', font=('Arial Black', 13),fg="red", padx=15, pady=5, cursor="hand2",
                      command=top.destroy).place(x=200, y=500)
    top.mainloop()

def admin():
    messagebox.showinfo("ADMIN", " ADMIN PAGE ADDED")


def continue_window():
    top = Toplevel()
    top.title('PASSPORT AUTOMATION')
    top.geometry("900x450")
    canvase=Canvas(top,width=1300,height=700)
    image=ImageTk.PhotoImage(Image.open("C:\\Users\\DINESH\Desktop\\b.jpg"))
    canvase.create_image(0,0,anchor=NW,image=image)
    canvase.pack()
    head = Label(top, text='USER AUTH', font=('Arial Black', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    bname = Button(top, text="NEW USER", font=(
        "Arial Black", 10), bg="white", command=new_user, padx=15, pady=10)
    bname.place(relx=0.1, rely=0.4,)
    bname.config(height=1, width=10)

    bauth = Button(top, text="EXISTING USER", font=(
        "Arial Black", 10), bg="white", command=existing_user, padx=15, pady=10)
    bauth.place(relx=0.4, rely=0.4)
    bauth.config(height=1, width=10)

    adminBtn = Button(top, text="ADMIN", font=(
        "Arial Black", 10), bg="white", command=admin, padx=15, pady=10)
    adminBtn.place(relx=0.7, rely=0.4)
    top.mainloop()

# ================ Main ===================
root = Tk()
root.geometry("900x450")
root.title("PASSPORT AUTOMATION")
canvas=Canvas(root,width=1300,height=700)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\DINESH\Desktop\\b.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
#label=Label(Image=img)
#root.pack()
id = Label(root, text='WELCOME TO THE PASSPORT AUTOMATION SYSTEM',
           font=('Arial Black', 20))
id.place(relx=0.5, rely=0.2, anchor=CENTER)

a = Button(root, text="DO YOU WANT TO CONTINUE", font=(
    "Arial Black", 10), bg="green",fg="white", command=continue_window)
a.place(relx=0.5, rely=0.4, anchor=CENTER)
a.config(height=1, width=30)


b = Button(root, text="CANCEL", font=("Arial Black", 10),
           bg="red",fg="white", command=root.destroy)
b.place(relx=0.5, rely=0.6, anchor=CENTER)
b.config(height=1, width=10)


root.mainloop()
