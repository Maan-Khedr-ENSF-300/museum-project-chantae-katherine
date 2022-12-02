# Python application that interfaces the museum database
# Chantae Ho 30141743
# Katherine Tubang

# Users:
#     Username: ch | Password: password1
#     Username: kt | Password: password2
#     Username: guest | No password

import mysql.connector

def login():
    print("Please select your role from the following list: ")
    print("1. Database Admin or Data Entry")
    print("2. Browse as guest")

    choice = input("Enter your role (1 or 2) here: ")

    if (choice == "1"):
        # Ask for login credentials to connect to the localhost and database
        _username = input("Please enter user name: ")
        _password = input("Please enter your password: ")
    elif (choice == "2"):
        _username = "guest"
        _password = None
    else:
        print("Invalid input.")
        exit(1)

    if _username == "root":
        print("Not a valid user.")
        exit(1)
    return _username, _password

def selection_menu():
    print("\nWhat would you like to lookup? Choose from the following list:")
    print("1. Art object")
    print("2. Artist")
    print("3. Exhibition")
    print("4. Collection")
    choice = input("Enter your choice (1 - 4) here: ")

    if choice == "1":
        # ask if user wants to see painting/statue/sculpture/other or art_object
        # print("\nWhat category of art objects would you like to search?")
        # print("1. Painting")
        # print("2. Statue")
        # print("3. Sculpture")
        # print("4. Other art types")
        # print("5. General art objects")
        # table_choice = input("Enter a choice from 1-5: ")
        table_choice = "5"
        if table_choice == "5":
            instr = "select * from art_object"
            searchkey = input("\nEnter the Id number of the art_object you are looking for (1 - 10, or press Enter to show all): ") or None
            if (searchkey != None):
                instr += " where Id_no=%s"
                searchkey = tuple(searchkey)

            cur.execute(instr, searchkey)
            col_names=cur.column_names
            search_result=cur.fetchall()


            print("Search found ",len(search_result)," Entries:\n")
            header_size=len(col_names)
            for i in range(6):
                if i == 4:
                    print("{:<35s}".format(col_names[i]),end='')
                else:
                    print("{:<16s}".format(col_names[i]),end='')
            print()
            print(15*8*'-')
            for row in search_result:
                i = 0
                for j in range(6):
                    if j == 4:
                        print("{:<35s}".format(str(row[j])),end='')
                    else:
                        print("{:<16s}".format(str(row[j])),end='')                
                print()

            print()

            for i in range(7, header_size):
                print("{:<20s}".format(col_names[i]),end='')
            print()
            print(15*8*'-')
            for row in search_result:
                i = 0
                for j in range(7, len(row)):
                    print("{:<20s}".format(str(row[j])),end='')                
                print()
            
            print()
            print("{:s}".format(col_names[6]),end='')
            print()

            print(15*8*'-')
            for row in search_result:
                print("{:s}".format(str(row[6])),end='')  
                print()



    # multi-level menu to help user reach selection, with option to go back to upper menu

def guest_access():
    selection_menu()
    # end user wanting to browse database
    # use descriptive user-friendly prompts to guide user
    

def main():
    print("Welcome to the Art Museum Database!")
    _username, _password = login()

    # connect to server
    cnx = mysql.connector.connect(user=_username, password=_password)
    global cur
    cur = cnx.cursor()
    
    cur.execute("Use museum")
    cur.execute("select current_role()")
    role = cur.fetchone()[0]
    if (role == "`db_admin`@`localhost`"):
        print("You have Database Admin privileges.")
        role_num = 0
    elif (role == "`data_entry`@`localhost`"):
        print("You have Data Entry privileges.")
        role_num = 1
    else:
        print("You have Read-Access privileges.")
        guest_access()

    cnx.close()



# 2- The application will ask the user for the kind of operation they would like to execute
def menu():
    print("\n-----------MENU-----------")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Create table")
    print("5. Create view")
    print("6. Alter")
    print("7. Query")

    choice = input("Which operation would you like to execute? Please enter your choice here: ")
    return choice;

# 3- Based on the previous selection, you will use a sequence of prompts to gather the information
# needed from the user to create a valid sql command
    # - For example if the user selects insert, present them with a prompt asking for which table
    # they want to insert data to. Make your prompts descriptive and user friendly. After that you
    # can ask the user for each attribute’s value one at a time with instructions on input
    # limitations to avoid wrongful/invalid sql statements, for example if an attribute is
    # mandatory tell them that it can not be left empty and if the attribute has a default value
    # show the default value and give the user means of selecting default value selection and so
    # on.

    # - Try to make each option broken down to as many atomic parts as possible. Another
    # example is for table creation, ask for the table name, then ask for the number of attributes
    # that table will have, followed by a loop to ask for each attribute name, data type, does it
    # have default value?, can it be null, and other constraints such primary key, foreign ket, etc..

# 4- Once all information needed is gathered, you will construct the appropriate SQL command and
# use the SQL connector to pass the SQL statement over to MySQL and get it executed, and finally
# fetching the output of the statement (if any)

# 5- Present the user with the results of the statement that was executed.

# 6- The program runs endlessly until on the main menu the user selects to quit the program

'''Information for this project:
o	python application user interfaces: you are required to do the guest 
interface which only allows for queries, you will only have to do one more 
of the two remaining interfaces - your choice which one to do -. If you do 
both remaining interfaces there is up to 8% project bonus to be awarded
o	access control using sql commands: this requires the creation of roles 
and users for the database from the sql scrip as shown in the video posted on 
D2L. the project requirement is to manage user access through the application, 
meaning that you can always log in as root and just show the interface 
corresponding to the prompt selections, which would not prevent a guest from 
dropping a table if they knew how to inject scripts. for the bonus the login 
will be using multiple credentials with different access levels as shown in 
the video recording which will prevent any undesired behaviour by the user. 
this is worth up to 3% project bonus
'''


if __name__ == "__main__":
    main()
