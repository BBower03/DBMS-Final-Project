import psycopg2
conn = psycopg2.connect(dbname = "gym", user = "postgres", password = "admin", host = "localhost", port = "5432")
cursor = conn.cursor()

def main() :
    
    while True:
        print("Register as a new member: 1")
        print("Member Login: 2")
        print("Trainer Login: 3")
        print("Administrator Login: 4")
        print("Exit: 0")
        request = input("Select desired action: \n")
        if request == "1":
            registerNewMember()
        elif request == "2":
            id = memberLogin()
            memberView(id)
        elif request == "3":
            id = trainerLogin()
            trainerDashboard(id)
        elif request == "4":
            id = adminLogin()
            adminDashboard(id)
        elif request == "0":
            exit()

def registerNewMember():
    print("registering as a new member:")
    fn = input("what is your first name?: ")
    ln = input("what is your last name?: ")
    phone = input("what is your phone number?: ")
    email = input("what is your email address?: ")
    ccNum = input("What is your credit card number?: ")
    print("we will now ask for some health information: ")
    height = input("How tall are you?: ")
    weight = input("How much do you weigh?: ")
    targetWeight = input("What is your weight loss goal?: ")
    numWorkouts = input("How many workouts would you like to complete per week?: ")
    numCals = input("How many calories would you like to burn per day?: ")
    username = input("enter your username: ")
    password = input("What would you like your password to be?: ")

    query = "INSERT INTO gym_user (user_type, username, user_password) VALUES (%s, %s, %s)"
    data = ("member", username, password)
    cursor.execute(query, data)
    conn.commit()
    
    query = "SELECT user_id FROM gym_user WHERE username = %s"
    data = (username,)
    cursor.execute(query, data)
    uid = cursor.fetchone()
    uid = uid[0]
    
    query = """INSERT INTO gym_member (
        user_id, first_name, last_name, phone, email, payment_info, subscription_type,
        subscription_start, subscription_end, member_weight, member_height, weight_goals,
        num_workouts_week, calorie_burn_goal, saved_routines
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    data = (uid, fn, ln, phone, email, ccNum, "member",
    None, None, weight, height, targetWeight,
    numWorkouts, numCals, None)
    
    cursor.execute(query, data)
    conn.commit()
    
    print("congratulations! you are now registered\n")



def trainerLogin():
    while True: 
        username = input("Username: ")
        password = input("Password: ")

        query = "SELECT user_id FROM gym_user WHERE username = %s AND user_password = %s"
        data = (username, password)
        cursor.execute(query, data)
        uid = cursor.fetchone()
        
        if uid:
            print("\nLogin succsessful!: ID: " + str(uid[0]))
            query = "SELECT trainer_id from gym_trainer WHERE user_id = %s"
            data = (uid,)
            cursor.execute(query, data)
            uid = cursor.fetchone()
            return uid
        else:
            print("Invalid username or password. Please try again\n")

def trainerDashboard(id):
    while True:
        print("trainer dashboard: ")
        print("1: lookup member")
        print("2: manage schedule")
        print("0: exit")
        request = input("Please make a selection: \n")
        if request == "0":
            return
        elif request == "1":
            memberLookup()
        elif request == "2":
            trainerschedule(id)
            
def memberLookup():
    while True:
        n = input("please enter members first name: (0 to exit)\n")
        if n == "0":
            return
        query = "SELECT * FROM gym_member WHERE first_name = %s"
        data = (n,)
        cursor.execute(query, data)
        members = cursor.fetchall()
        if members:
            for m in members:
                print("results: ", m[0], m[2], m[3], m[4])
        else:
            print("No members found\n")
            return
        
        
def trainerschedule(id):
    query = "SELECT * FROM gym_schedule WHERE trainer_id = %s"
    data = (id,)
    cursor.execute(query, data)
    sched = cursor.fetchall()
    if sched:
        print("your schedule: ")
        for e in sched:
            print(e[1], e[2], e[4])
    else:
        print("You have no events scheduled!\n")
        
    request = input("Would you like to add a new opening on your schedule?: (y/n) \n")
    if request == "y":
        updateTrainerSched(id)
    else:
        return

def updateTrainerSched(id):
    query = "INSERT INTO gym_schedule (available_time, booking_length, trainer_id, day_of_week) VALUES (%s, %s, %s, %s)"
    time = input("What time are you available at (hh:mm:ss): ")
    length = input("How long are you available for?: ")
    d = input("What day of the week will it be?: ")
    data = (time, length, id, d)
    cursor.execute(query, data)
    conn.commit()
    print("schedule updated!\n")
        
           
#admin functions           
 
def adminDashboard(id):
    while True:
        print("1: view rooms")
        print("2: set room availability")
        print("3: Check equipment maintenance logs")
        print("4: check customer payment confirmation")
        print("0: exit")
        request = input("Please select an option: \n")
        if request == "0":
            return
        elif request == "1":
            viewRooms()
        elif request == "2":
            setRoom()
        elif request == "3":
            viewLogs()
        elif request == "4":
            viewPayment()
            
def adminLogin():
     while True: 
        username = input("Username: ")
        password = input("Password: ")

        query = "SELECT user_id FROM gym_user WHERE username = %s AND user_password = %s"
        data = (username, password)
        cursor.execute(query, data)
        uid = cursor.fetchone()
        
        if uid:
            print("\nLogin succsessful!: ID: " + str(uid[0]))
            query = "SELECT admin_id from gym_admin WHERE user_id = %s"
            data = (uid,)
            cursor.execute(query, data)
            uid = cursor.fetchone()
            return uid
        else:
            print("Invalid username or password. Please try again\n")


def viewPayment():
    cursor.execute("SELECT * FROM bill")
    bills = cursor.fetchall()
    for b in bills:
        print("User:", b[0], "| Payed:", b[1])
            
            
def viewLogs():
    query = "SELECT * FROM gym_equipment"
    cursor.execute(query)
    logs = cursor.fetchall()
    for log in logs:
        print("id:", log[0], "name:", log[1], "last maintained:", log[2], "room id:", log[3], "\n")
            
def setRoom():
    r = input("Which room would you like to change availability of? \n")
    t = input("Would you like to set the room as available? (true/false)\n")
    if t == "true":
        query = "UPDATE gym_room SET room_availability = TRUE WHERE room_id = %s"
    else:
        query = "UPDATE gym_room SET room_availability = FALSE WHERE room_id = %s"
        
    data = (r,)
    cursor.execute(query, data)
    conn.commit()
    print('Room availability updated!')

        
def viewRooms():
    query = "SELECT * FROM gym_room"
    cursor.execute(query)
    rooms = cursor.fetchall()
    for room in rooms:
        print(room[0], room[1], room[2], room[3], room[4])
        print()
        
        
#member functions
def memberView(id):
    while True:
        print("Member View: " + id)
        print("Profile Management: 1")
        print("Dashboard: 2")
        print("View schedule: 3")
        print("Log Out: 0")
        request = input("Please select an option: \n")

        if request == "1":
            profileManagement(id)
        elif request == "0":
            return
        elif request == "2":
            displayDashboard(id)
        elif request == "3":
            schedule(id)
            
def memberLogin():
    while True: 
        username = input("Username: ")
        password = input("Password: ")

        query = "SELECT user_id FROM gym_user WHERE username = %s AND user_password = %s"
        data = (username, password)
        cursor.execute(query, data)
        uid = cursor.fetchone()
        
        if uid:
            print("\nLogin succsessful!: ID: " + str(uid[0]))
            return str(uid[0])
        else:
            print("Invalid username or password. Please try again\n")

def schedule(id):
    while True:
        query = "SELECT member_id FROM gym_member WHERE user_id = %s"
        data = (id,)
        cursor.execute(query, data)
        memberId = cursor.fetchone()
        memberId = memberId[0]
        query = """SELECT gc.class_id, gc.room_id, gc.trainer_id, gc.class_type, gc.category, gc.start_time, gc.end_time
            FROM gym_class gc
            JOIN booked_classes bc ON gc.class_id = bc.class_id
            WHERE bc.member_id = %s"""
        data = (memberId,)
        cursor.execute(query, data)
        classes = cursor.fetchall()
        if classes:
            print("Your booked classes: ")
            for gymClass in classes:
                query = "SELECT first_name FROM  gym_trainer WHERE trainer_id = %s"
                data = (gymClass[2],)
                cursor.execute(query, data)
                name = cursor.fetchone()
                name = name[0]
                print("Class Id:", gymClass[0], "|  Class Type:", gymClass[3], "|  Category:", gymClass[4], "|  Start Time:", gymClass[5], "|  End time:", gymClass[6], "|  Trainer:", name)
        else:
            print("you are not registered for any classes\n")
        
        request = input ("Would you like to view opened classes?: (y/n)\n")
        if request == 'y':
            availableClasses(memberId)
        else:
            return
        
def availableClasses(memberId):
    while True:
        cursor.execute("SELECT * FROM gym_class WHERE number_of_people < enrollment_limit")
        classes = cursor.fetchall()
        print("All classes with openings: \n")
        
        for gymClass in classes:
            query = "SELECT first_name FROM  gym_trainer WHERE trainer_id = %s"
            data = (gymClass[2],)
            cursor.execute(query, data)
            name = cursor.fetchone()
            name = name[0]
            print("Class Id:", gymClass[0], "|  Class Type:", gymClass[3], "|  Category:", gymClass[4], "|  Start Time:", gymClass[5], "|  End time:", gymClass[6], "|  Trainer:", name, "|  Number of people:", gymClass[7])

        print("Would you like to join a class?: y/n\n")
        request = input("Press 0 to exit: ")
        if request == "0":
            return
        elif request == "y":
            joinClass(memberId)
        
def joinClass(memberId):
    cn = input("Which class number would you like to join?: ")
    query = "INSERT INTO booked_classes (member_id, class_id) VALUES (%s, %s)"
    data = (memberId, cn)
    cursor.execute(query, data)
    conn.commit()
    
    query = "UPDATE gym_class SET number_of_people = number_of_people + 1 WHERE class_id = %s"
    data = (cn,)
    cursor.execute(query, data)
    conn.commit()


def displayDashboard(id):
    while True:
        query = "SELECT * FROM gym_member WHERE user_id = %s"
        data = (id,)
        cursor.execute(query, data)
        info = cursor.fetchone()
        print("health stats: ")
        print("Height: ", info[11])
        print("Weight: ", info[10])
        print("target weight: ", info[12])
        print("desired number of workouts", info[13])
        print("Calories per day burn goal: ", info[14])
        print("Saved routines: ", info[15])
        print("\nOption:\n0: exit")
        print("1: edit saved workout routines")
        
        request = input("please select an option by number: \n")
        
        if request == "0":
            return
        if request == "1":
            editRoutines(id)

def editRoutines(id):
    r = input("please type out your new routine: ")
    query = "UPDATE gym_member SET saved_routines = %s WHERE user_id = %s"
    data = (r, id)
    cursor.execute(query, data)
    conn.commit()
    print("\nroutines updates successfully\n")

def profileManagement(id):
    while True: 
        query = "SELECT * FROM gym_member WHERE user_id = %s"
        data = (id,)
        cursor.execute(query, data)
        info = cursor.fetchone()
        print("1: First Name: ", info[2])
        print("2: Last Name: ", info[3])
        print("3: phone number: ", info[4])
        print("4: Email Address: ", info[5])
        print("5: Payment Method", info[6])
        print("6: Height: ", info[11])
        print("7: Weight: ", info[10])
        print("8: target weight: ", info[12])
        print("9: desired number of workouts", info[13])
        print("10: Calories per day burn goal: ", info[14])
        query = "SELECT username, user_password FROM gym_user WHERE user_id = %s"
        data = (id,)
        cursor.execute(query, data)
        username, password = cursor.fetchone()
        print("11: Username: ", username)
        print("12: Password: ", password)
        print("0: back")
        request = input("What would you like to edit: \n")

        if request == "1":
            changeFirstName(id)
        elif request == "0":
            return
        elif request == "2":
            changeLastName(id)
        elif request == "3":
            changePhoneNumber(id)
        elif request == "4":
            changeEmail(id)
        elif request == "5":
            changePayment(id)
        elif request == "6":
            changeHeight(id)
        elif request == "7":
            changeWeight(id)
        elif request == "8":
            changeTargetWeight(id)
        elif request == "9":
            changeNumWorkouts(id)
        elif request == "10":
            changeCal(id)
        elif request == "12":
            changePass(id)
        elif request == "11":
            changeUser(id)
            
        
        

def changeFirstName(id):
    fn = input("Editing First name: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET first_name = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("First name changed")
    else: 
        print("Cancelling")
        return

def changeLastName(id):
    fn = input("Editing last name: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET last_name = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Last name changed")
    else: 
        print("Cancelling")
        return
    
def changePhoneNumber(id):
    fn = input("Editing phone number: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET phone = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("phone number changed")
    else: 
        print("Cancelling")
        return
    
def changeEmail(id):
    fn = input("Editing Email address: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET email = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Email address changed")
    else: 
        print("Cancelling")
        return
    
def changePayment(id):
    fn = input("Editing Credit Card Number: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET payment_info = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Payment info changed")
    else: 
        print("Cancelling")
        return
    
def changeHeight(id):
    fn = input("Editing Height: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET member_height = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Height changed")
    else: 
        print("Cancelling")
        return

def changeWeight(id):
    fn = input("Editing Weight: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET member_weight = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Weight changed")
    else: 
        print("Cancelling")
        return
    
def changeTargetWeight(id):
    fn = input("Editing Weight goal: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET weight_goals = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("weight goal changed")
    else: 
        print("Cancelling")
        return
    
def changeNumWorkouts(id):
    fn = input("Editing number of weekly workouts: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET num_workouts_week = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("number of workouts changed")
    else: 
        print("Cancelling")
        return
    
def changeCal(id):
    fn = input("Editing daily calorie burn goal: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_member SET calorie_burn_goal = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Calorie goal changed")
    else: 
        print("Cancelling")
        return
    
def changeUser(id):
    fn = input("Editing Username: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_user SET username = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Username changed")
    else: 
        print("Cancelling")
        return

def changePass(id):
    fn = input("Editing Password: ")
    if input("Are you sure (y/n)?: ") == "y":
        query = "UPDATE gym_user SET user_password = %s WHERE user_id = %s"
        data = (fn, id)
        cursor.execute(query, data)
        conn.commit()
        print("Password changed")
    else: 
        print("Cancelling")
        return
    
main()
