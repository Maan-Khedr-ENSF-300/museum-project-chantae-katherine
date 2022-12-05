# Python application that interfaces the museum database
# Chantae Ho 30141743

# Users:
#     Username: ch | Password: password1
#     Username: kt | Password: password2
#     Username: guest | No password

import mysql.connector
import os

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
            
            # print art_object description separately
            print()
            print("{:s}".format(col_names[6]),end='')
            print()

            print(15*8*'-')
            for row in search_result:
                print("{:s}".format(str(row[6])),end='')  
                print()
    
    elif choice == "2":     # choice is artist
        instr = "select * from artist"
        searchkey = input("\nEnter the First name of the artist you are looking for (press Enter for all): ") or None
        if (searchkey != None):
            instr += " where Fname=%s"
            searchkey = searchkey.split("\n")
            searchkey = tuple(searchkey)

        cur.execute(instr, searchkey)
        col_names=cur.column_names
        search_result=cur.fetchall()

        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)

        for i in range(7):
            if i >= 3:
                print("{:<16s}".format(col_names[i+1]),end='')
            else:
                print("{:<17s}".format(col_names[i]),end='')
        print()
        print(17*7*'-')
        for row in search_result:
            j = 0
            for j in range(7):
                if j >= 3:
                    print("{:<16s}".format(str(row[j+1])),end='')   
                else:
                    print("{:<17s}".format(str(row[j])),end='')                
            print()
        
        # print artist description separately (it is v long)
        print()
        print("{:s}".format(col_names[3]),end='')
        print()

        print(15*8*'-')
        for row in search_result:
            print("{:s}".format(str(row[3])),end='')  
            print()
    
    elif choice == "3":     # choice is exhibition
        instr = "select * from exhibition"
        searchkey = input("\nEnter the Exhibition ID of the exhibition you are looking for (press Enter for all): ") or None
        if (searchkey != None):
            instr += " where E_id=%s"
            searchkey = tuple(searchkey)

        cur.execute(instr, searchkey)
        col_names=cur.column_names
        search_result=cur.fetchall()

        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)

        for i in range(header_size):
            if i == 1:
                print("{:<35s}".format(col_names[i]),end='')
            else:
                print("{:<15s}".format(col_names[i]),end='')
        print()
        print(20*header_size*'-')
        for row in search_result:
            for j in range(header_size):
                if j == 1:
                    print("{:<35s}".format(str(row[j])),end='')   
                else:
                    print("{:<15s}".format(str(row[j])),end='')                
            print()    
    
    elif choice == "4":     # choice is collection
        instr = "select * from collection"
        searchkey = input("\nEnter the name of the collection you are looking for (press Enter for all): ") or None
        if (searchkey != None):
            instr += " where Name=%s"
            searchkey = searchkey.split("\n")
            searchkey = tuple(searchkey)

        cur.execute(instr, searchkey)
        col_names=cur.column_names
        search_result=cur.fetchall()

        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)

        # print all attributes except collection description
        for i in range(header_size-1):
            if i == 3:
                print("{:<35s}".format(col_names[i+1]),end='')
            elif i > 3:
                print("{:<20s}".format(col_names[i+1]),end='')
            else:
                print("{:<20s}".format(col_names[i]),end='')
        print()
        print(20*(header_size)*'-')
        for row in search_result:
            for j in range(header_size-1):
                if j == 3:
                    print("{:<35s}".format(str(row[j+1])),end='')   
                elif j > 3:
                    print("{:<20s}".format(str(row[j+1])),end='')
                else:
                    print("{:<20s}".format(str(row[j])),end='')                
            print()   
        
        # print collection description
        print()
        print("{:s}".format(col_names[3]),end='')
        print()

        print(15*8*'-')
        for row in search_result:
            print("{:s}".format(str(row[3])),end='')  
            print() 

def insert_from_file(table):
    # Assuming file in in data folder!
    filename = input("\nEnter the filename here (include .txt extension): ")
    path = "C:\\Users\\chant\\Documents\\GitHub\\museum-project-team-5\\data folder\\" + filename
        
    input_list = []
    try:
        file_handler = open(path)
        for line in file_handler:
            input_list.append(line.rstrip())
    except IOError:
        exit("Error reading file")
    except Exception as error:
        exit("An error occurred")
    finally:
        file_handler.close()

    num_insertions = len(input_list)

    
    
    # i. Providing a file with information line separated, where each line represents an
    # entry that should be made to the table of choice

def insert_sequence(table):
    if table == "1":     # choice is art_object table
        # get column names and largest id number
        cur.execute("SELECT id_no FROM art_object ORDER BY id_no DESC LIMIT 1")
        last_id = (cur.fetchone())

        cur.execute("SELECT * FROM art_object where id_no=%s", last_id)
        col_names = cur.column_names

        data = [last_id[0]+1]

        for i in range(1, len(col_names)):
            info=""
            if i == 7:
                info = " (PAINTING/STATUE/SCULPTURE/OTHER)"
            elif (i == 10 or i == 11):
                info = " (yyyy-mm-dd format, including dashes)"
            prompt = "Enter a value for " + col_names[i] + info + ": "
            data.append(input(prompt) or None)

        data = tuple(data)
        insert_str = ("insert into art_object values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        try:
            cur.execute(insert_str, data)
            cnx.commit()
            print("\nData successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return

         #Based on art_type (PAINTING/STATUE/SCULPTURE/OTHER), get data for that also
        print("\nPlease enter some more information about your", data[7])
        cur.execute("SELECT * FROM " + data[7])
        col_names = cur.column_names

        num_params = len(col_names)
        params = num_params * "%s,"
        params = params[:-1]    #remove extra comma at end
        insert_arttype = ("insert into " + data[7] + " values (" + params + ")")

        arttype_data = [data[0]]

        for i in range(1, num_params):
            prompt = "Enter a value for " + col_names[i] + ": "
            arttype_data.append(input(prompt) or None)

        arttype_data = tuple(arttype_data)
        
        try:
            cur.execute(insert_arttype, arttype_data)
            cnx.commit()
            print("\nArt type successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return

        on_display = False

        #If borrowed_collection is None, then object is in permanent collection
        if data[9] == None:
            print("\nSince this art object is in the museum's permanent collection, we need some more information.")
            cur.execute("SELECT * FROM in_permanent_collection")
            col_names = cur.column_names

            num_params = len(col_names)
            params = num_params * "%s,"
            params = params[:-1]    #remove extra comma at end
            insert_pcoll = ("insert into in_permanent_collection values (" + params + ")")

            pcoll_data = [data[0]]

            for i in range(1, num_params):
                info = ""
                if i == 2:
                    info = " (yyyy-mm-dd)"
                elif i == 3:
                    info = " (stored/on loan/on display)"
                prompt = "Enter a value for " + col_names[i] + info + ": "
                pcoll_data.append(input(prompt) or None)

            pcoll_data = tuple(pcoll_data)
            
            try:
                cur.execute(insert_pcoll, pcoll_data)
                cnx.commit()
                print("\nData successfully entered into database.")
            except mysql.connector.Error as err:
                print("\nSomething went wrong:", err)
                return

            if pcoll_data[3] == "on display":
                on_display = True
        
        if (not on_display) and (data[9] != None):
            answer = input("\nIs the art object currently on display? Enter y or n: ")
            if answer == 'y':
                on_display = True
        
        if on_display:
            print("\nSince this art object is on display, we need some more information.")
            cur.execute("SELECT E_id, Name FROM exhibition")
            exhibitions = cur.fetchall()
            col_names = cur.column_names

            print("Here are the exhibitions to choose from: ")

            for i in range(len(col_names)):
                print("{:<20s}".format(col_names[i]),end='')
            print()
            print(30*len(col_names)*'-')
            for row in exhibitions:
                for i in range(len(col_names)):
                    print("{:<20s}".format(str(row[i])),end='')
                print()
            
            e_id = input("\nEnter the E_id of the exhibition this art object belongs to: ")
            to_insert = tuple(e_id)
            a_id = (data[0],)
            to_insert = to_insert + a_id

            try:
                cur.execute("insert into on_display values (%s, %s)", to_insert)
                cnx.commit()
                print("\nArt object display data successfully entered into database.")
            except mysql.connector.Error as err:
                print("\nSomething went wrong:", err)
                return

    elif table == "2":      # table choice is artist
        print("\nPlease enter the artist info below:")
        cur.execute("SELECT * FROM artist")
        col_names = cur.column_names

        num_params = len(col_names)
        params = num_params * "%s,"
        params = params[:-1]    #remove extra comma at end
        insert_artist = ("insert into artist values (" + params + ")")

        artist_data = []

        for i in range(0, num_params):
            info = ""
            if i == 4 or i == 5:
                info = " (yyyy-mm-dd)"
            prompt = "Enter a value for " + col_names[i] + info + ": "
            artist_data.append(input(prompt) or None)

        artist_data = tuple(artist_data)
        
        try:
            cur.execute(insert_artist, artist_data)
            cnx.commit()
            print("\nData successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return
    
    elif table == "3":      # table choice is exhibition
        print("\nPlease enter the exhibition info below:")
        cur.execute("SELECT * FROM exhibition")
        col_names = cur.column_names

        cur.execute("SELECT E_id FROM exhibition ORDER BY e_id DESC LIMIT 1")
        last_id = (cur.fetchone())

        num_params = len(col_names)
        params = num_params * "%s,"
        params = params[:-1]    #remove extra comma at end
        insert = ("insert into exhibition values (" + params + ")")

        data = [last_id[0]+1]

        for i in range(1, num_params):
            info = ""
            if i == 2 or i == 3:
                info = " (yyyy-mm-dd)"
            prompt = "Enter a value for " + col_names[i] + info + ": "
            data.append(input(prompt) or None)

        data = tuple(data)
        
        try:
            cur.execute(insert, data)
            cnx.commit()
            print("\nData successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return

    elif table == "4":      # table choice is collection
        print("\nPlease enter the collection info below:")
        cur.execute("SELECT * FROM collection")
        col_names = cur.column_names

        num_params = len(col_names)
        params = num_params * "%s,"
        params = params[:-1]    #remove extra comma at end
        insert = ("insert into collection values (" + params + ")")

        data = []

        for i in range(0, num_params):
            info = ""
            if i == 2:
                info = " (museum/personal/etc.)"
            elif i == 3:
                info = " (collection description)"
            prompt = "Enter a value for " + col_names[i] + info + ": "
            data.append(input(prompt) or None)

        data = tuple(data)
        
        try:
            cur.execute(insert, data)
            cnx.commit()
            print("\nData successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return

    else:
        print("That is not a valid choice.")
        return

def insertion_menu():
    while(True):
        print("\nWould you like to:")
        print("1. Provide a file with data to insert")
        print("2. Be guided through the data entry process")
        choice = input("Please enter your choice here: ")
        if (choice == "1" or choice == "2"):
            break;
        print("That is an invalid choice. Please choose again.")

    print("\nWhich table would you like to insert into? Choose from the following list:")
    print("1. Art object")
    print("2. Artist")
    print("3. Exhibition")
    print("4. Collection")
    table = input("Enter your choice (1 - 4) here: ")

    if (choice == "1"):
        insert_from_file(table)
    elif choice == "2":
        insert_sequence(table)

def guest_access():
    selection_menu()
    print()
    print(100*"=")
    choice = input("Would you like to continue searching? Enter y to continue or n to quit: ")
    if choice == 'y':
        guest_access()
    else:
        return

def update_menu():
    pass

def delete_menu():
    pass

def data_entry_access():
    choice = menu(1);
    if choice == "0":
        selection_menu()
    elif choice == "1":
        insertion_menu()
    elif choice == "2":
        update_menu()
    elif choice == "3":
        delete_menu()
    elif choice == "10":
        return
    else:
        print("That is not a valid input.")
    data_entry_access()
    
    # c. Update and delete tuples in the database by providing search field values. Make sure to
    # show appropriate messages for successful updates and deletions, and also descriptive
    # messages for failed attempts

def main():
    print("Welcome to the Art Museum Database!")
    _username, _password = login()

    # connect to server
    try:
        global cnx
        cnx = mysql.connector.connect(user=_username, password=_password)
    except mysql.connector.Error as err:
        print("\nSomething went wrong:", err)
        exit(1)
    global cur
    cur = cnx.cursor(buffered=True)
    
    cur.execute("Use museum")
    cur.execute("select current_role()")
    role = cur.fetchone()[0]
    if (role == "`db_admin`@`localhost`"):
        print("\nYou have Database Admin privileges.")
        role_num = 0
    elif (role == "`data_entry`@`localhost`"):
        print("\nYou have Data Entry privileges.")
        # data_entry_access()
        insert_from_file("3")
    else:
        print("\nYou have Read-Access privileges.")
        guest_access()

    print("\nThanks for using the program! See you next time.")


    cnx.close()



# 2- The application will ask the user for the kind of operation they would like to execute
def menu(role_num):
    print("\n-----------MENU-----------")
    print("0. Search database")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    if role_num == 0:
        print("4. Create table")
        print("5. Create view")
        print("6. Alter")
        print("7. Query")
    print("10. QUIT")

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
