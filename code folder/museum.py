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
        print("\nWhat category of art objects would you like to search?")
        print("1. Painting")
        print("2. Statue")
        print("3. Sculpture")
        print("4. Other art types")
        print("5. General art objects")
        table_choice = input("Enter a choice from 1-5: ")

        if table_choice != "5":
            arttype_dict = {"1":"painting", "2":"statue", "3":"sculpture", "4":"other"}
            table = arttype_dict.get(table_choice)
            instr = "select * from " + table
            searchkey = input("\nEnter the Id number of the " + table + " you are looking for (press Enter to show all): ") or None
            if (searchkey != None):
                instr += " where Id_no=%s"
                searchkey = searchkey.split("\n")
                searchkey = tuple(searchkey)

            try:
                cur.execute(instr, searchkey)
            except mysql.connector.Error as err:
                print("\nSomething went wrong:", err)
                return
            
            col_names=cur.column_names
            search_result=cur.fetchall()

            print("Search found",len(search_result),"entries:\n")
            header_size=len(col_names)
            for i in range(header_size):
                print("{:<22s}".format(col_names[i]),end='')
            print()
            print(22*header_size*'-')
            for row in search_result:
                for j in range(header_size):
                    print("{:<22s}".format(str(row[j])),end='')                
                print()


        elif table_choice == "5":
            instr = "select * from art_object"
            searchkey = input("\nEnter the Id number of the art_object you are looking for (press Enter to show all): ") or None
            if (searchkey != None):
                instr += " where Id_no=%s"
                searchkey = searchkey.split("\n")
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
            searchkey = searchkey.split("\n")
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
                print("{:<22s}".format(col_names[i]),end='')
        print()
        print(20*(header_size)*'-')
        for row in search_result:
            for j in range(header_size-1):
                if j == 3:
                    print("{:<35s}".format(str(row[j+1])),end='')   
                elif j > 3:
                    print("{:<20s}".format(str(row[j+1])),end='')
                else:
                    print("{:<22s}".format(str(row[j])),end='')                
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

    table_dict = {"1":"art_object", "2":"artist", "3":"exhibition", "4":"collection"}

    cur.execute("SELECT * FROM " + table_dict.get(table))
    col_names = cur.column_names

    num_params = len(col_names)
    params = num_params * "%s,"
    params = params[:-1]    #remove extra comma at end
    insert_str = ("insert into " + table_dict.get(table) + " values (" + params + ")")

    for i in range(num_insertions):
    
        if table == "1" or table == "3":
            select_str = ("select " + col_names[0] + " from " + table_dict.get(table) + " order by " +  col_names[0] + " desc limit 1")
            cur.execute(select_str)
            last_id = (cur.fetchone())
            
            data = [last_id[0]+1]
            
        else:
            data = []

        data = data + input_list[i].split(",")
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
        data = tuple(data)

        try:
            cur.execute(insert_str, data)
            cnx.commit()
            print("\nData successfully entered into database.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return

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

def table_menu(action):
    table_dict = {"1":"art_object","2":"artist","3":"exhibition","4":"collection",
            "5":"in_permanent_collection","6":"on_display","10":"other","7":"painting",
            "8":"sculpture","9":"statue"}
    while(True):
        print("\nWhich table would you like to", action, "from ? Choose from the following list:")
        print("1. General Art objects")
        print("2. Artist")
        print("3. Exhibition")
        print("4. Collection")
        print("5. Permanent Collection objects")
        print("6. On Display Objects")
        print("7. PAINTING Type Art Objects")
        print("8. SCULPTURE Type Art Objects")
        print("9. STATUE Type Art Objects")
        print("10. OTHER Type Art Ojbects")

        table = input("Enter your choice (1 - 10) here: ")
        
        if table in table_dict:
            break
        print("Invalid input.")
    return table_dict.get(table)


def update_delete_menu(action_num):
    if action_num:
        action = "update"
    else:
        action = "delete"
    table = table_menu(action)

    cur.execute("select * from " + table)
    col_names=cur.column_names
    search_result=cur.fetchall()
    print("\nThere are" , len(search_result),"entries in that table:\n")

    header_size = len(col_names)

    if table == "art_object":
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
        
        a_id = input("\nPlease enter the Id_no of the art object you would like to " + action + ": ")
        if action == "update":
            print("\nWhich attribute would you like to update?")
            for i in range(header_size):
                print(str(i+1) + ". " + str(col_names[i]))
            index = int(input("Enter your choice here (1 - " + str(header_size) + "): "))
            attribute = col_names[index-1]
            
            new_val = input("\nEnter a new value for " + attribute + " here (press Enter for None):") or None
            if new_val != None:
                new_val = tuple(new_val.split('\n'))
            else:
                new_val = (new_val,)
            update_str = "update " + table + " set " + attribute + "=%s where Id_no=" + a_id
        else:
            delete_str = "delete from art_object where Id_no =" + a_id

    elif table == "artist":
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

        fname = input("\nPlease enter the First name of the artist you would like to " + action + ": ")
        fname = "\"" + fname + "\""
        lname = input("Please enter the Last name of the artist you would like to " + action + ": ")
        lname = "\"" + lname + "\""
        if action == "update":
            print("\nWhich attribute would you like to update?")
            for i in range(header_size):
                print(str(i+1) + ". " + str(col_names[i]))
            index = int(input("Enter your choice here (1 - " + str(header_size) + "): "))
            attribute = col_names[index-1]
            
            new_val = input("\nEnter a new value for " + attribute + " here (press Enter for None):") or None
            if new_val != None:
                new_val = tuple(new_val.split('\n'))
            else:
                new_val = (new_val,)
            update_str = "update " + table + " set " + attribute + "=%s where fname=" + fname + " and lname=" + lname
        else:
            delete_str = "delete from artist where fname =" + fname + " and lname=" + lname 

    elif table == "exhibition":
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

        e_id = input("\nPlease enter the E_id of the exhibition you would like to " + action + ": ")
        if action == "update":
            print("\nWhich attribute would you like to update?")
            for i in range(header_size):
                print(str(i+1) + ". " + str(col_names[i]))
            index = int(input("Enter your choice here (1 - " + str(header_size) + "): "))
            attribute = col_names[index-1]
            
            new_val = input("\nEnter a new value for " + attribute + " here (press Enter for None):") or None
            if new_val != None:
                new_val = tuple(new_val.split('\n'))
            else:
                new_val = (new_val,)
            update_str = "update " + table + " set " + attribute + "=%s where E_id=" + e_id
        else:
            delete_str = "delete from exhibition where E_id =" + e_id
    
    elif table == "collection":
        # print all attributes except collection description
        for i in range(header_size-1):
            if i == 3:
                print("{:<35s}".format(col_names[i+1]),end='')
            elif i > 3:
                print("{:<20s}".format(col_names[i+1]),end='')
            else:
                print("{:<22s}".format(col_names[i]),end='')
        print()
        print(20*(header_size)*'-')
        for row in search_result:
            for j in range(header_size-1):
                if j == 3:
                    print("{:<35s}".format(str(row[j+1])),end='')   
                elif j > 3:
                    print("{:<20s}".format(str(row[j+1])),end='')
                else:
                    print("{:<22s}".format(str(row[j])),end='')                
            print()   
        
        # print collection description
        print()
        print("{:s}".format(col_names[3]),end='')
        print()

        print(15*8*'-')
        for row in search_result:
            print("{:s}".format(str(row[3])),end='')  
            print() 

        name = input("\nPlease enter the Name of the collection you would like to " + action + ": ")
        name = "\"" + name + "\""
        if action == "update":
            print("\nWhich attribute would you like to update?")
            for i in range(header_size):
                print(str(i+1) + ". " + str(col_names[i]))
            index = int(input("Enter your choice here (1 - " + str(header_size) + "): "))
            attribute = col_names[index-1]
            
            new_val = input("\nEnter a new value for " + attribute + " here (press Enter for None):") or None
            if new_val != None:
                new_val = tuple(new_val.split('\n'))
            else:
                new_val = (new_val,)
            update_str = "update " + table + " set " + attribute + "=%s where name=" + name
        else:
            delete_str = "delete from collection where name=" + name 

    else:
        for i in range(header_size):
            print("{:<22s}".format(col_names[i]),end='')
        print()
        print(22*(header_size)*'-')
        for row in search_result:
            for j in range(header_size):
                print("{:<22s}".format(str(row[j])),end='')                
            print()   
        
        pk = input("\nPlease enter the " + col_names[0] + " of the object you would like to " + action + ": ")
        pk = "\"" + pk + "\""
        if action == "update":
            print("\nWhich attribute would you like to update?")
            for i in range(header_size):
                print(str(i+1) + ". " + str(col_names[i]))
            index = int(input("Enter your choice here (1 - " + str(header_size) + "): "))
            attribute = col_names[index-1]
            
            new_val = input("\nEnter a new value for " + attribute + " here (press Enter for None):") or None
            if new_val != None:
                new_val = tuple(new_val.split('\n'))
            else:
                new_val = (new_val,)
            update_str = "update " + table + " set " + attribute + "=%s where " + col_names[0] + "=" + pk
        else:
            delete_str = "delete from " + table + " where " + col_names[0] + "=" + pk       

    if action == "update":
        try:
            cur.execute(update_str, new_val)
            cnx.commit()
            if (cur.rowcount < 1):
                raise Exception("The object you entered does not exist.")
            print("\nData successfully updated.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return
        except Exception as e:
            print("\nUnsuccessful update:", e)
    else:
        try:
            cur.execute(delete_str)
            cnx.commit()
            if (cur.rowcount < 1):
                raise Exception("The object you entered does not exist.")
            print("\nData successfully deleted.")
        except mysql.connector.Error as err:
            print("\nSomething went wrong:", err)
            return   
        except Exception as e:
            print("\nUnsuccessful deletion:", e)

def admin_access():
    choice = menu(0);
    if choice == "0":
        selection_menu()
    elif choice == "1":
        insertion_menu()
    elif choice == "2":
        update_delete_menu(0)
    elif choice == "3":
        update_delete_menu(1)
    elif choice == "4":
        create_new_table_menu()
    elif choice == "5":
        create_view_menu()
    elif choice == "6":
        alter_tb_menu()
    elif choice == "7":
        basic_query_menu()
    elif choice == "10":
        return
    else: 
        print("Sorry that is an invalid action. Please re-enter your choice.")
    admin_access()

def create_new_table_menu():
    while (True):
        print("\n New Table Creation")
        print(20*"-")
        print("Please select the method in which you would like to create your new table:")
        print("\n1: Typing in your MySQL command")
        print("2: Insert a SQL script file path directory")
        print("3: Back to MENU")
        chosen = input("Enter chosen method (1-2): ")

        if chosen == "1":  
            type_sql()
        elif chosen == "2":         
            read_sql()
        elif chosen == "3":
            break
        else:
            print("\nSorry that is not a valid entry. Please re-enter your chosen method: ")

        break 

    return
        



## Functions for reading and typing sql scripts and files (Create table, view, alter table)

def type_sql():
    print("\nChosen Method: Typing in your MySQL command")
    command = input("\nPlease type in your MySQL command: ")
    cur.execute("use museum")
    cur.execute(command)
    print("\nYour command has been executed sucessfully!")

def read_sql():
    print("\nChosen Method: Reading SQL file")
    path = input("\nPlease enter your sql script file path directory: ")

    cur.execute("use museum")
    with open (path, 'r') as f:
        with cnx.cursor() as cursor:
            cursor.execute(f.read(), multi=True)
        print("\nRead file and executed sucessfully!")


def create_view_menu():
    while (True):
        print("\n View Creation")
        print(15*"-")
        print("Please select the method in which you would like to create view:")
        print("\n1: Typing in your MySQL command")
        print("2: Insert a SQL script file")
        print("3: Back to MENU")
        chosen = input("Enter chosen method (1-2): ")

        if chosen == "1":
            type_sql()
        elif chosen == "2":                 
            read_sql()
            print_query()   
        elif chosen == "3":
            break
        else:
            print("\nSorry that is not a valid entry. Please re-enter your chosen method: ")
        break

    return

def alter_tb_menu():
    while(True):
        print("\n Altering Existing Table")
        print(25*"-") 
        print("Please select the method in which you would like to alter an existing table:")
        print("\n1: Typing in your MySQL command")
        print("2: Insert a SQL script file")
        print("3: Back to MENU")
        chosen = input("Enter chosen method (1-3): ")

        if chosen == "1":
            type_sql()
        elif chosen == "2":
            read_sql()
        elif chosen == "3":
            break
        else:
            print("\nSorry that is not a valid entry. Please re-enter your chosen method: ")
        
        break
    
    return 


def basic_query_menu():
    while (True):
        print("\n Chosen Basic Query Retrieval")
        print(30*"-")
        print("\n1: Typing in your MySQL command")
        print("2: Insert a SQL script file")
        print("3: Back to MENU")
        chosen = input("Please select the method in which you would like to create view:")

        if chosen == "1":
            query_type()
        elif chosen == "2":
            read_sql()
        elif chosen == "3":
            break
        else:
            print("\nSorry that is not a valid entry. Please re-enter your chosen method: ")

        break
    
    return


#functions for query display below for both methods (reading and typing)

def query_type():
    print("\nTyping in your SQL command")
    print(25*"-")
    command = input("\nPlease enter your SQL query: ")
    cur.execute("use museum")
    cur.execute(command)
    print_query()

def print_query():
    col_names = cur.column_names
    attribute_size = len(col_names)
    print()
    print(50*"-")
    print("Attribute list names: ")
    for i in range(attribute_size):
        print(col_names[i], end= '\t')
    print()

    rows = cur.fetchall()
    size = len(rows)
    print("\nTable Content (respective from attribute name list): \n")
    for i in range(size):
        for j in range(len(rows[i])):
            print(rows[i][j], end= "\t")
            print()
        print()
    return

def data_entry_access():
    choice = menu(1);
    if choice == "0":
        selection_menu()
    elif choice == "1":
        insertion_menu()
    elif choice == "2":
        update_delete_menu(0)
    elif choice == "3":
        update_delete_menu(1)
    elif choice == "10":
        return
    else:
        print("That is not a valid input.")
    data_entry_access()

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
        admin_access()
    elif (role == "`data_entry`@`localhost`"):
        print("\nYou have Data Entry privileges.")
        data_entry_access()
    else:
        print("\nYou have Read-Access privileges.")
        guest_access()

    print("\nThanks for using the program! See you next time.")

    cnx.close()


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

if __name__ == "__main__":
    main()