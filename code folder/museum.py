# Python application that interfaces the museum database
# Chantae Ho 30141743
# Katherine Tubang

import mysql.connector

def main():
    print("Welcome to the Olympic Archery Database!")

    # 1- Ask for login credentials to connect to the localhost and database
    _user = input("Please enter user name: ")
    _password = input("Please enter your password: ")

    # connect to server
    cnx = mysql.connector.connect(user=_user, password=_password)
    cnx.close()

    menu()


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
