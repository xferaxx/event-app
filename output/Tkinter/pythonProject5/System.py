import mysql.connector
from Events import Events
from Users import User

users = []

myDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db'
)


# Only for DataBase and Table Creation
def create_database():
    myCursor = myDB.cursor()

    query1 = """ CREATE DATABASE IF NOT EXISTS db;"""
    myCursor.execute(query1)
    myDB.commit()

    query2 = """ use db; """
    myCursor.execute(query2)
    myDB.commit()

    query3 = """ create table if not exists users(
                    user_id INT NOT NULL,
                    Full_Name VARCHAR(30) NOT NULL,
                    Email VARCHAR(30) NOT NULL,
                    Credit INT NOT NULL DEFAULT 0,
                    PRIMARY KEY ( user_id )
                    );
              """
    myCursor.execute(query3)
    myDB.commit()

    query4 = """ create table if not exists eventu(
                    event_id INT NOT NULL ,
                    typu VARCHAR(30) NOT NULL,
                    description VARCHAR(30) NOT NULL,
                    address VARCHAR(30) NOT NULL,
                    dangerous_level VARCHAR(30) NOT NULL,
                    user_id INT NOT NULL,
                    approves int NOT NULL DEFAULT 0,
                    PRIMARY KEY ( event_id ),
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                    );
             """
    myCursor.execute(query4)
    myDB.commit()

    query5 = """ create table if not exists approves(
                    event_id INT NOT NULL,
                    user_id INT NOT NULL,
                    PRIMARY KEY (event_id, user_id),
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (event_id) REFERENCES eventu(event_id)
                    );
               """
    myCursor.execute(query5)
    myDB.commit()

    query6 = """ create table if not exists comments(
                   event_id INT NOT NULL,
                   user_id INT NOT NULL,
                   comments VARCHAR(50) NOT NULL,
                   FOREIGN KEY (event_id) REFERENCES eventu(event_id),
                   FOREIGN KEY (user_id) REFERENCES users(user_id)
                   ); 
                """
    myCursor.execute(query6)
    myDB.commit()

    query7 = """                   
                  INSERT IGNORE INTO users 
                    (user_id, Full_Name, Email) 
                  VALUES 
                    (1, "Julian Tech", "julian@gmail.com");
                """
    myCursor.execute(query7)
    myDB.commit()

    query8 = """                                                                                     
                  INSERT IGNORE INTO users                  
                    (user_id, Full_Name, Email)             
                  VALUES                                    
                    (2, "Mahdi", "Mahdi@gmail.com");                                                             
                """
    myCursor.execute(query8)
    myDB.commit()

    query9 = """                                    
                  INSERT IGNORE INTO users          
                    (user_id, Full_Name, Email)     
                  VALUES                            
                    (3, "Malik", "Malik@gmail.com");
                """
    myCursor.execute(query9)
    myDB.commit()

    query10 = """                                    
                  INSERT IGNORE INTO users          
                    (user_id, Full_Name, Email)     
                  VALUES                            
                    (4, "Zahi", "Zahi@gmail.com");
                """
    myCursor.execute(query10)
    myDB.commit()

    query11 = """                                 
                  INSERT IGNORE INTO eventu       
                    (event_id, typu, description, address, dangerous_level, user_id)   
                  VALUES                          
                    (1, "environmental", "gas leaked", "haifa", "Hard", 1);
                """
    myCursor.execute(query11)
    myDB.commit()

    query12 = """                                 
                      INSERT IGNORE INTO eventu       
                        (event_id, typu, description, address, dangerous_level, user_id)   
                      VALUES                          
                        (2, "environmental", "Tornado", "Tel AViv", "Medium", 1);
                    """
    myCursor.execute(query12)
    myDB.commit()

    query13 = """                                 
                      INSERT IGNORE INTO eventu       
                        (event_id, typu, description, address, dangerous_level, user_id)   
                      VALUES                          
                        (3, "health", "corona", "haifa", "low", 2);
                    """
    myCursor.execute(query13)
    myDB.commit()

    query10 = """                                 
                      INSERT IGNORE INTO eventu       
                        (event_id, typu, description, address, dangerous_level, user_id)   
                      VALUES                          
                        (1, "health", "viruses", "Plaza Hotel", "Hard", 3);
                    """
    myCursor.execute(query10)
    myDB.commit()

    print("DataBase ( db ) was created successfully")


# ------------------------------------------------------------------------------------------------------------

# Method to add user
def add_user(u_id, name, mail):
    print("Adding user to users table")
    usr = User(u_id, name, mail)
    if usr.user_id < 0:
        print("please", u_id, "can not be used (Enter Positive ID)")
        return

    if usr in users:
        print("This User ID", u_id, "is Already Exist")
        return
    else:
        print("User", u_id, "is Successfully Added")
        myCursor = myDB.cursor()
        query = """INSERT INTO users (user_id,Full_Name,Email)
                    VALUES (%s, %s, %s) """

        record = (u_id, name, mail)
        myCursor.execute(query, record)
        myDB.commit()
        print("Record inserted successfully into Laptop table")
        return


# ------------------------------------------------------------------------------------

# Method to print users
def show_users():
    print("--------------------USERS--------------------")
    for us in users:
        print(us)


print("\n")

# ********************************************************************************************************************
# *********************************** Events Function start here ***********************************

events = []

# Users who report an event(UserID is Key , and EventID is list of Value)
DicOfEventUser = {}


# this Method was Created to Create some Types of Dict
def adds(ev, U, dicOfEV):
    if U in dicOfEV:
        dicOfEV[U].append(ev)
    else:
        dicOfEV[U] = [ev]
    return


# Method to add events
def add_event(event_id, type, description, address, dangerous_level, user_id):
    event = Events(event_id, type, description, address, dangerous_level, user_id)

    if event.event_id < 0:
        print("please", event_id, "can not be used (Enter Positive ID)")
        return
    if event in events:
        print("This Event ID", event_id, "is Already Exist")
        return

    events.append(event)
    print("Event", event_id, "Successfully Created")
    adds(event_id, user_id, DicOfEventUser)

    myCursor = myDB.cursor()
    query = """INSERT INTO eventu(event_id,typu,description,address,dangerous_level,user_id) 
               VALUES (%s, %s, %s, %s, %s, %s) """
    record = (event_id, type, description, address, dangerous_level, user_id)
    myCursor.execute(query, record)
    myDB.commit()
    print("Record inserted successfully into Laptop table")
    return


# this Dict for Users that Approved Event(EventID is the Key)
eventsApproved = {}
# this dict for users that Approved Event(UserID is the KEY)
userApproves = {}


# Method to approve an event
def approve_event(ap_event_id, ap_user_id):
    if ap_event_id in eventsApproved:
        if ap_user_id in eventsApproved[ap_event_id]:
            return -2
    if ap_user_id not in DicOfEventUser.keys():
        users_still_not_reported(ap_user_id, ap_event_id)
        return
    listOfUEvents = DicOfEventUser[ap_user_id]
    if ap_event_id in listOfUEvents:
        print("you cant Approve your own Event Reason(Because user", ap_user_id, "Added event number", ap_event_id)
        return -1
    for ev in events:
        if ev.event_id == ap_event_id:
            ev._approves = ev.approves + 1
            print(ev.approves)
            give_3credit(ap_user_id)
            adds(ap_user_id, ap_event_id, eventsApproved)
            adds(ap_event_id, ap_user_id, userApproves)

            myCursor = myDB.cursor()

            query = """Update eventu set approves = %s where event_id = %s"""
            record1 = (ev.approves, ap_event_id)
            myCursor.execute(query, record1)
            myDB.commit()

            query2 = """INSERT INTO approves(event_id,user_id)                     
                       VALUES (%s, %s)"""
            record2 = (ap_event_id, ap_user_id)
            myCursor.execute(query2, record2)
            myDB.commit()
            return


# Method to to get out from Bad Situation(like plan b)
def users_still_not_reported(user_id, event_id):
    adds(event_id, user_id, userApproves)
    adds(event_id, user_id, eventsApproved)
    for ev in events:
        if ev.event_id == event_id:
            ev._approves = ev.approves + 1
            give_3credit(user_id)
            myCursor = myDB.cursor()
            query = """Update eventu set approves = %s where event_id = %s"""
            record1 = (ev.approves, event_id)
            myCursor.execute(query, record1)
            myDB.commit()

            query2 = """INSERT INTO approves(event_id,user_id) 
                       VALUES (%s, %s)"""
            record2 = (event_id, user_id)
            myCursor.execute(query2, record2)
            myDB.commit()

    return


# Method to give 3 Credit for who approve to an event
def give_3credit(usr_id):
    for U in users:
        if U.user_id == usr_id:
            U.credit = U.credit + 3
            print("Event was Approved, (3) Credits was Successfully added for user ID", usr_id, "Total Credit =",
                  U.credit)

            myCursor = myDB.cursor()
            query = """                                                      
                       UPDATE users                                         
                       SET                                                   
                           Credit = %s                                                                    
                       WHERE                                                 
                           users.user_id = %s;                             
                           """

            record1 = (U.credit, usr_id)
            myCursor.execute(query, record1)
            myDB.commit()


# this method check if User exist (*this was made before data base was used to check lists)
def check(us_id):
    for U in users:
        if U.user_id == us_id:
            return True


# Method to delete a event
def delete_event(event_id):
    c = myDB.cursor()

    query = "DELETE FROM eventu WHERE eventu.event_id = %s;"
    valu = (int(event_id))
    c.execute(query, (valu,))

    myDB.commit()


# Method to Update a event
def edit_event(event_id, typu, description, address, dangerous_level):
    print("Event Number", event_id, "was Updated")
    myCursor = myDB.cursor()
    query = """ 
               UPDATE eventu 
               SET 
                   typu = %s,
                   description = %s,
                   address = %s,
                   dangerous_level = %s
               WHERE
                   eventu.event_id = %s;
                   """

    record1 = (typu, description, address, dangerous_level, event_id)
    myCursor.execute(query, record1)
    myDB.commit()
    myCursor.close()


# Method to Print event
def show_events():
    print("--------------------EVENTS--------------------")
    cur2 = myDB.cursor()
    cur2.execute("SELECT * FROM eventu")
    rows1 = cur2.fetchall()
    for e in events:
        print(e)
    return rows1


# Method to show approved user on specific event
def show_approved_user(event_id):
    String = "Users that Approved on event " + str(event_id) + " are users " + str(eventsApproved[event_id])
    return String


# Method to show Reported events on specific user
def show_reported_events(user_id):
    String = "Events that was Reported by User " + str(user_id) + " are  " + str(DicOfEventUser[user_id])
    return String


# this show user activity
def user_activity(user_id):
    if user_id in userApproves and user_id in DicOfEventUser:
        Reports = len(DicOfEventUser[user_id])
        Approves = len(userApproves[user_id])
        total = Reports + Approves
        s = "UserID =", str(user_id), "has", str(total), "Activities\n" " the User reported", str(
            Reports), "event(s)", "and Approved", str(Approves), "other Event(s)"
        return Reports, Approves, s

    if user_id not in userApproves and user_id not in DicOfEventUser:
        s = "no Activity yet"
        e = ""
        t = ""
        return s, e, t

    if user_id not in userApproves:
        Approves = 0
        Reports = len(DicOfEventUser[user_id])
        total = Reports + Approves
        s = "UserID =", str(user_id), "has", str(total), "Activities\n", " the User reported", str(
            Reports), "event(s)", "and Approved", str(Approves), "other Event(s)"
        return Reports, Approves, s

    if user_id not in DicOfEventUser:
        Reports = 0
        Approves = len(userApproves[user_id])
        total = Reports + Approves
        s = "UserID =", str(user_id), "has", str(total), "Activities\n", " the User reported", str(
            Reports), "event(s)", "and Approved", str(Approves), "other Event(s)"
        return Reports, Approves, s


# Method to show user Report
def show_report2(usr_id):
    cnt = d.count(usr_id)
    x, y, z = user_activity(usr_id)
    for U, S in eventsApproved.items():
        if usr_id in S and len(S) >= 5:
            s = str(cnt * 10) + " Credit of event Report"
            t = str(y * 3) + " Credits of Events Approving"
            return s, t, z

        elif usr_id in S and len(S) <= 5:
            str11 = " No Own Events was Approved"
            t = y * 3
            str22 = str(t) + " Credits of Events Approving"
            return z, str11, str22


# Method to show Max User Report
def max_reports():
    print("The max Reports users is")
    myCursor = myDB.cursor()
    query = """ 
            SELECT distinct u.*, 
            COUNT(e.user_id) AS num_of_reports
            FROM users u LEFT JOIN eventu e
            ON u.user_id = e.user_id
            GROUP BY u.user_id
            HAVING num_of_reports >= ALL(SELECT count(user_id) FROM eventu GROUP BY user_id);"""

    myCursor.execute(query)
    rows = myCursor.fetchall()
    myDB.commit()
    return rows


# Method to show Max revenue of a user
def max_revenue():
    myCursor = myDB.cursor()
    query = """                                                                                 
             select * from users                             
             inner join (select max(credit) as Credit from   
                         users) as maxima                    
             on maxima.credit = users.credit                                                             
             """

    myCursor.execute(query)
    rows = myCursor.fetchall()
    myDB.commit()
    return rows


# Method to show and count  the type of events
def type_count():
    Cnt = 0
    Cnt1 = 0
    Cnt2 = 0
    for event in events:
        if event.dangerous_level == "Hard":
            Cnt = Cnt + 1
        elif event.dangerous_level == "Medium":
            Cnt1 = Cnt1 + 1
        else:
            Cnt2 = Cnt2 + 1
    strr = "there is " + str(Cnt) + " of HARD Report(s)-->(Dangerous level = Hard)"
    str2 = "there is " + str(Cnt1) + " of MEDIUM Report(s)-->(Dangerous level = Medium)"
    str3 = "there is " + str(Cnt2) + " of LOW Report(s)-->(Dangerous level = Low)"
    return strr, str2, str3


# Method to add a comment to an event
def add_comment(e_id, u_id, com):
    myCursor = myDB.cursor()
    query = """INSERT INTO comments(event_id,user_id,comments)               
               VALUES (%s, %s, %s)"""
    record = (e_id, u_id, com)
    myCursor.execute(query, record)
    myDB.commit()
    return


# Method to Update Comment of event
def edit_comment(e_id, u_id, com):
    myCursor = myDB.cursor()
    query = """ UPDATE comments SET comments = %s WHERE event_id = %s AND user_id = %s"""

    record = (com, e_id, u_id)
    myCursor.execute(query, record)
    myDB.commit()
    return


def delete_comment(event_id, user_id):
    c = myDB.cursor()

    query = "DELETE FROM comments WHERE event_id = %s AND user_id = %s"
    valu = (int(event_id), int(user_id))
    c.execute(query, valu)

    myDB.commit()


# Method to show ALL Comments
def show_comments():
    print("--------------------COMMENTS--------------------")
    cur2 = myDB.cursor()
    cur2.execute("SELECT * FROM comments")
    rows1 = cur2.fetchall()
    for e in events:
        print(e)
    return rows1


# to see if the event entered the 5 approves +
d = []


# Method if event got more than 5 approves the User Reporter of the event get 10 Credits
def give_10credit(user_id, Approves):
    for U in users:
        if U.user_id == user_id:
            chek = U.credit
            new = Approves * 2
            if chek == new:
                return
            U.credit = new
            x = U.credit
            print(new, "Credits Successfully added for user ID", user_id, "Total Credit =", U.credit)

            myCursor = myDB.cursor()
            query = """Update users set Credit = %s where user_id = %s"""

            record1 = (int(x), user_id)
            myCursor.execute(query, record1)
            myDB.commit()
            myCursor.close()
            return


# Method to check if event really get +5 Approves and after checking send to give _10Credit
def check_add10():
    for e in events:
        if e.approves >= 5:
            EVE = e.event_id
            for u, s in DicOfEventUser.items():
                if EVE in s:
                    give_10credit(u, e.approves)
                    d.append(u)
