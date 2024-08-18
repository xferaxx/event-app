from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import mysql.connector

from Events import Events
from System import add_user, add_event, users, myDB, show_events, max_reports, edit_event, delete_event, events, \
    approve_event, show_approved_user, DicOfEventUser, adds, userApproves, eventsApproved, show_reported_events, \
    show_report2, max_revenue, type_count, check_add10, add_comment, show_comments, edit_comment, \
    delete_comment, create_database

from Users import *

create_database()


# MYSQL Connection
def connectionSQL():
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database='db'
                                         )
    return connection


# to Load the Users into list and send them to make them Objects
def load_users():
    try:
        connection = connectionSQL()

        sql_select_Query = "select * from users"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        for row in records:
            usr = User(row[0], row[1], row[2], row[3])
            users.append(usr)

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


# -----------------------------------------------------------------------------------------------------------------

# to Load the Events into list and send them to make them Objects
def load_events():
    try:
        connection = connectionSQL()

        sql_select_Query = "select * from eventu"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        for row in records:
            adds(row[0], row[5], DicOfEventUser)
            evnt = Events(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            events.append(evnt)

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


# -----------------------------------------------------------------------------------------------------------------

# to Load the approves into Dict to use in Functions
def load_approves():
    try:
        connection = connectionSQL()

        sql_select_Query = "select * from approves"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        for row in records:
            adds(row[0], row[1], userApproves)
            adds(row[1], row[0], eventsApproved)

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


# -----------------------------------------------------------------------------------------------------------------

load_users()
load_events()
check_add10()
load_approves()

# -----------------------------------------------------------------------------------------------------------------

root = Tk()
root.title("User Registration")
root.attributes('-fullscreen', True)

root.configure(bg='grey')

global u1
global u2
global u3

# Creating the labels for user section
Label(root, text="User ID").place(x=10, y=10)
Label(root, text="Full Name").place(x=10, y=40)
Label(root, text="Email").place(x=10, y=70)

# the Input of User Section
u1 = Entry(root)
u1.place(x=140, y=10)

u2 = Entry(root)
u2.place(x=140, y=40)

u3 = Entry(root)
u3.place(x=140, y=70)


def add_user_gui():
    user_id = u1.get()
    Full_Name = u2.get()
    Email = u3.get()
    mysqldb = connectionSQL()

    try:

        add_user(int(user_id), Full_Name, Email)
        messagebox.showinfo("information", "Record inserted successfully...")
        u1.delete(0, END)
        u2.delete(0, END)
        u3.delete(0, END)
        u1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# -----------------------------------------------------------------------------------------------------------------

def add_event_gui():
    event_id = ev1.get()
    typo = ev2.get()
    desc = ev3.get()
    address = ev4.get()
    dang_level = ev5.get()
    user_event_id = ev6.get()

    mysqldb = connectionSQL()

    try:
        add_event(int(event_id), typo, desc, address, dang_level, user_event_id)

        messagebox.showinfo("information", "Record inserted successfully...")
        ev1.delete(0, END)
        ev2.delete(0, END)
        ev3.delete(0, END)
        ev4.delete(0, END)
        ev5.delete(0, END)
        ev6.delete(0, END)

        ev1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# -----------------------------------------------------------------------------------------------------------------

def edit_event_gui():
    if ev6.get() == "":

        event_id = ev1.get()
        typo = ev2.get()
        desc = ev3.get()
        address = ev4.get()
        dang_level = ev5.get()

        mysqldb = connectionSQL()

        try:
            edit_event(int(event_id), typo, desc, address, dang_level)

            messagebox.showinfo("information", "Record inserted successfully...")
            ev1.delete(0, END)
            ev2.delete(0, END)
            ev3.delete(0, END)
            ev4.delete(0, END)
            ev5.delete(0, END)

            ev1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showerror("error", "try again without adding USER ID")
        messagebox.showinfo("my message", "you cant UPDATE user_id\n;)")
        messagebox.showwarning("warning", "Reason(changing foreign key FORBIDDEN)")


# -----------------------------------------------------------------------------------------------------------------

def delete_event_gui():
    event_id = ev1.get()

    mysqldb = connectionSQL()

    try:
        delete_event(int(event_id))

        messagebox.showinfo("information", "Record inserted successfully...")
        ev1.delete(0, END)
        ev2.delete(0, END)
        ev3.delete(0, END)
        ev4.delete(0, END)
        ev5.delete(0, END)
        ev6.delete(0, END)

        ev1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# -----------------------------------------------------------------------------------------------------------------

def approve_event_gui():
    event_id = ev1.get()
    user_id = ev6.get()

    mysqldb = connectionSQL()

    try:

        k = approve_event(int(event_id), int(user_id))
        if k == -2:
            messagebox.showinfo("error", "You Already Approve this event")
            messagebox.showinfo("information", "Choose another Event")
        elif k == -1:
            messagebox.showinfo("error", "you cant Approve your own event")
        else:
            messagebox.showinfo("information", "Record inserted successfully...")
            ev1.delete(0, END)
            ev2.delete(0, END)
            ev3.delete(0, END)
            ev4.delete(0, END)
            ev5.delete(0, END)
            ev6.delete(0, END)
            ev1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


# -----------------------------------------------------------------------------------------------------------------

def show_approved_user_gui():
    event_id = ev1.get()

    mysqldb = connectionSQL()

    try:
        STR = show_approved_user(int(event_id))
        w = Label(root, text=STR)
        w.pack()
        messagebox.showinfo("information", STR)
        ev1.delete(0, END)
        ev2.delete(0, END)
        ev3.delete(0, END)
        ev4.delete(0, END)
        ev5.delete(0, END)
        ev6.delete(0, END)

        ev1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

    def remove_text():
        w.destroy()

    Button(root, text="Delete Labels", bg='yellow', fg='green', command=remove_text, height=4, width=10).place(x=870,
                                                                                                               y=570)


# -----------------------------------------------------------------------------------------------------------------


def show_reported_event_gui():
    user_id = ev6.get()

    mysqldb = connectionSQL()

    try:
        STR = show_reported_events(int(user_id))
        w = Label(root, text=STR)
        w.pack()
        messagebox.showinfo("information", STR)
        ev1.delete(0, END)
        ev2.delete(0, END)
        ev3.delete(0, END)
        ev4.delete(0, END)
        ev5.delete(0, END)
        ev6.delete(0, END)

        ev6.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

    def remove_text():
        w.destroy()

    Button(root, text="Delete Labels", bg='yellow', fg='green', command=remove_text, height=4, width=10).place(x=870,
                                                                                                               y=570)


# -----------------------------------------------------------------------------------------------------------------

def show_report2_gui():
    mysqldb = connectionSQL()

    try:
        STRr, STRr2, STRr3 = type_count()
        w = Label(root, text=STRr)
        b = Label(root, text=STRr2)
        s = Label(root, text=STRr3)

        w.pack()
        b.pack()
        s.pack()

        ev1.delete(0, END)
        ev2.delete(0, END)
        ev3.delete(0, END)
        ev4.delete(0, END)
        ev5.delete(0, END)
        ev6.delete(0, END)

        ev1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

    def remove_text():
        w.destroy()
        b.destroy()
        s.destroy()

    Button(root, text="Delete Labels", bg='yellow', fg='green', command=remove_text, height=4, width=10).place(x=870,
                                                                                                               y=570)


# -----------------------------------------------------------------------------------------------------------------

def type_count_gui():
    user_id = ev6.get()
    mysqldb = connectionSQL()
    try:
        STR1, STR2, STR3 = show_report2(int(user_id))
        s = Label(root, text=STR1)
        t = Label(root, text=STR2)
        z = Label(root, text=STR3)

        s.pack()
        t.pack()
        z.pack()

        ev6.delete(0, END)

        ev6.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

    def remove_text1():
        s.destroy()
        t.destroy()
        z.destroy()

    Button(root, text="Delete Labels", bg='yellow', fg='green', command=remove_text1, height=4, width=10).place(x=870,
                                                                                                                y=570)


# -----------------------------------------------------------------------------------------------------------------

# this is for event
global ev1
global ev2
global ev3
global ev4
global ev5
global ev6

# creating the labels for event section
Label(root, text="Event ID                         #").place(x=10, y=505)
Label(root, text="Type").place(x=10, y=535)
Label(root, text="Description").place(x=10, y=565)
Label(root, text="Address").place(x=10, y=595)
Label(root, text="Dangerous level").place(x=10, y=625)
Label(root, text="your userID                   #").place(x=10, y=655)

# THE INPUT FOR EVENT SECTION
ev1 = Entry(root)
ev1.place(x=150, y=505)

ev2 = Entry(root)
ev2.place(x=150, y=535)

ev3 = Entry(root)
ev3.place(x=150, y=565)

ev4 = Entry(root)
ev4.place(x=150, y=595)

ev5 = Entry(root)
ev5.place(x=150, y=625)

ev6 = Entry(root)
ev6.place(x=150, y=655)
# ---------------------------------------------- BUTTONS --------------------------------------------------------
Button(root, text="ADD USER", bg='yellow', fg='green', command=add_user_gui, height=4, width=13).place(x=10, y=120)

Button(root, text="ADD EVENT", bg='yellow', fg='green', command=add_event_gui, height=4, width=13).place(x=10, y=688)

Button(root, text="UPDATE EVENT", bg='yellow', fg='green', command=edit_event_gui, height=4, width=13).place(x=120,
                                                                                                             y=688)

Button(root, text="DELETE EVENT", bg='yellow', fg='green', command=delete_event_gui, height=4, width=13).place(x=230,
                                                                                                               y=688)

Button(root, text="Approve Event\n(#Enter EventID)\n(#Enter UserID)", bg='yellow', fg='green',
       command=approve_event_gui, height=4,
       width=13).place(x=340, y=688)

Button(root, text="Show \nApproved user\n(#Enter eventID)", bg='yellow', fg='green', command=show_approved_user_gui,
       height=4,
       width=13).place(x=450, y=688)

Button(root, text="Show \nReported events\n(#Enter userID)", bg='yellow', fg='green', command=show_reported_event_gui,
       height=4,
       width=13).place(x=560, y=688)

Button(root, text="Show \nType count", bg='yellow', fg='green', command=show_report2_gui, height=4, width=13).place(
    x=670, y=688)

Button(root, text="Show Report & \nShow Report2\n(#Enter UserID)", bg='yellow', fg='green', command=type_count_gui,
       height=4,
       width=13).place(x=780, y=688)


# -----------------------------------------------------------------------------------------------------------------

# Gui to show users on Tree
def view_users():
    cur1 = myDB.cursor()
    cur1.execute("SELECT * FROM users")
    rows = cur1.fetchall()

    for row in rows:
        print(row)
        tree.insert("", END, values=row)

    cur1.close()


tree = Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=10)
tree.column("#1", anchor=CENTER)
tree.heading("#1", text="ID")
tree.column("#2", anchor=CENTER)
tree.heading("#2", text="Name")
tree.column("#3", anchor=CENTER)
tree.heading("#3", text="Email")
tree.column("#4", anchor=CENTER)
tree.heading("#4", text="Credit")
tree.pack()


# to clear user Tree
def clear_users():
    for item in tree.get_children():
        tree.delete(item)


# to clear event Tree
def clear_events():
    for item in tree2.get_children():
        tree2.delete(item)


# ------------------------BUTTONS-------------------------
button1 = Button(text="Display data", bg='yellow', fg='green', command=view_users)
button1.pack(pady=10)

Button(root, text="Clear Users", bg='yellow', fg='green', command=clear_users).place(x=1090, y=200)

Button(root, text="Clear Events", bg='yellow', fg='green', command=clear_events).place(x=1090, y=515)


# -----------------------------------------------------------------------------------------------------------------

def view_events():
    rows1 = show_events()
    for row in rows1:
        print(row)
        tree2.insert("", END, values=row)


tree2 = Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings', height=10)
tree2.column("#1", anchor=S)
tree2.heading("#1", text="event ID")
tree2.column("#2", anchor=S)
tree2.heading("#2", text="type")
tree2.column("#3", anchor=S)
tree2.heading("#3", text="description")
tree2.column("#4", anchor=S)
tree2.heading("#4", text="Address")
tree2.column("#5", anchor=S)
tree2.heading("#5", text="dangerous level")
tree2.column("#6", anchor=S)
tree2.heading("#6", text="User that reported the event")
tree2.column("#7", anchor=S)
tree2.heading("#7", text="Approves")
tree2.pack()

# ------------------------BUTTONS-------------------------


button2 = Button(text="Display data", bg='yellow', fg='green', command=view_events)
button2.pack(pady=20)

exit_button = Button(root, text="Exit", bg='red', fg='black', height=2, width=14, command=root.destroy).place(x=1250,
                                                                                                              y=10)


# -----------------------------------------------------------------------------------------------------------------

def show_report2_gui():
    # Level object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Level widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("1100x300")

    # A Label widget to show in toplevel
    Label(newWindow, text="MAX REPORTED USER").pack()

    tree3 = Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    tree3.column("#1", anchor=S)
    tree3.heading("#1", text="ID")
    tree3.column("#2", anchor=S)
    tree3.heading("#2", text="NAME")
    tree3.column("#3", anchor=S)
    tree3.heading("#3", text="Email")
    tree3.column("#4", anchor=S)
    tree3.heading("#4", text="Credit")
    tree3.column("#5", anchor=S)
    tree3.heading("#5", text="number of reports")

    tree3.pack()

    def view_max_report():
        rows1 = max_reports()
        for row in rows1:
            print(row)
            tree3.insert("", END, values=row)

    view_max_report()


# ------------------------BUTTON SHOW MAX REPORTED USER-------------------------
max_report = Button(root, text="SHOW MAX\nReported user", command=show_report2_gui, bg='yellow', fg='green', height=2,
                    width=16).place(x=1090, y=140)


# -----------------------------------------------------------------------------------------------------------------

def max_revenue_gui():
    # Level object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Level widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("1000x300")

    # A Label widget to show in toplevel
    Label(newWindow, text="MAX REVENUE USER").pack()

    tree4 = Treeview(newWindow, column=("c1", "c2", "c3", "c4"), show='headings')
    tree4.column("#1", anchor=S)
    tree4.heading("#1", text="ID")
    tree4.column("#2", anchor=S)
    tree4.heading("#2", text="NAME")
    tree4.column("#3", anchor=S)
    tree4.heading("#3", text="Email")
    tree4.column("#4", anchor=S)
    tree4.heading("#4", text="Credit")

    tree4.pack()

    def view_max_revenue():
        STR = max_revenue()
        for row in STR:
            print(row)
            tree4.insert("", END, values=row)

    view_max_revenue()


# ------------------------BUTTON SHOW MAX REVENUE-------------------------
max_report = Button(root, text="SHOW MAX\n USER REVENUE", command=max_revenue_gui, bg='yellow', fg='green', height=2,
                    width=16).place(x=1090, y=95)

# ---------------------------------------------Comment Section------------------------------------------------------

# this for comments
global c1
global c2
global c3


def comment_window():
    # Level object which will
    # be treated as a new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Level widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("1000x600")

    # A Label widget to show in toplevel
    Label(newWindow, text="COMMENTS").pack()

    Label(newWindow, text="Enter EventID").place(x=200, y=300)
    Label(newWindow, text="Enter your UserID").place(x=200, y=335)
    Label(newWindow, text="Enter your Comment").place(x=200, y=370)

    c1 = Entry(newWindow)
    c1.place(x=350, y=300)

    c2 = Entry(newWindow)
    c2.place(x=350, y=335)

    c3 = Entry(newWindow)
    c3.place(x=350, y=370, height=50, width=400)

    tree5 = Treeview(newWindow, column=("c1", "c2", "c3"), show='headings')
    tree5.column("#1", anchor=S)
    tree5.heading("#1", text="EVENT ID")
    tree5.column("#2", anchor=S)
    tree5.heading("#2", text="USER ID")
    tree5.column("#3", anchor=S)
    tree5.heading("#3", text="COMMENTS")

    tree5.pack()

    # to Clear screen
    def clear_comments():
        for item in tree5.get_children():
            tree5.delete(item)

    # to Display the Comments
    def display_c():
        rows1 = show_comments()
        for row in rows1:
            print(row)
            tree5.insert("", END, values=row)

    # to ADD a Comment on event
    def add_c():

        event_id = c1.get()
        user_id = c2.get()
        comment = c3.get()
        mysqldb = connectionSQL()

        try:
            add_comment(int(event_id), int(user_id), comment)
            messagebox.showinfo("information", "HI User " + str(user_id) + " \nyour Comment on Event " + str(
                event_id) + "\nWAS CREATED (added)")
            c1.delete(0, END)
            c2.delete(0, END)
            c3.delete(0, END)

            c1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    # to Edit a Comment on event
    def edit_c():

        event_id = c1.get()
        user_id = c2.get()
        comment = c3.get()
        mysqldb = connectionSQL()

        try:
            edit_comment(int(event_id), int(user_id), comment)
            messagebox.showinfo("information", "HI User " + str(user_id) + " \nyour Comment on Event " + str(
                event_id) + "\nWAS UPDATED")
            c1.delete(0, END)
            c2.delete(0, END)
            c3.delete(0, END)

            c1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    # to delete comment from event
    def remove_c():

        event_id = c1.get()
        user_id = c2.get()
        mysqldb = connectionSQL()

        try:
            delete_comment(int(event_id), int(user_id))
            messagebox.showinfo("information", "HI User " + str(user_id) + " \nyour Comment on Event " + str(
                event_id) + "\nWas REMOVED")

            c1.delete(0, END)
            c2.delete(0, END)
            c3.delete(0, END)

            c1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    # ------------------------ BUTTONS for comment section -------------------------
    Button(newWindow, text="Add\nComment", command=add_c, bg='yellow', fg='green', height=2, width=16).place(x=370,
                                                                                                             y=500)

    Button(newWindow, text="Display\nComments", command=display_c, bg='yellow', fg='green', height=2, width=13).place(
        x=530, y=250)

    Button(newWindow, text="Clear\nComments", command=clear_comments, bg='yellow', fg='green', height=2,
           width=13).place(
        x=650, y=250)

    Button(newWindow, text="Edit\nComment", command=edit_c, bg='yellow', fg='green', height=2,
           width=13).place(x=500, y=500)

    Button(newWindow, text="Remove\nComment", command=remove_c, bg='yellow', fg='green', height=2,
           width=13).place(x=610, y=500)


Button(root, text="GO TO COMMENTS", command=comment_window, bg='green', fg='black', height=2, width=16).place(x=900,
                                                                                                              y=715)

print(eventsApproved)
print(DicOfEventUser)
print(userApproves)

root.mainloop()
