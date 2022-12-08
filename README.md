[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9394829&assignment_repo_type=AssignmentRepo)
# ENSF 300 Final Project: Museum Project
Group 5 - 
Chantae Ho (30141743) chantae.ho@ucalgary.ca
Katherine Tubang (30121665) katherine.tubang@ucalgary.ca 

## Task Completion
- ERD diagram planning: Chantae, Katherine
- ERD diagram creation: Katherine
- Relational schema planning: Chantae
- Relational schema creation: Chantae
- SQL Database Creation & Initialization, Roles & Users (Access Control): Chantae
- SQL Queries: Chantae, Katherine
- Python guest access: Chantae
- Python data entry access: Chantae
- Python database admin access: Katherine
- Python testing and debugging: Chantae, Katherine
- Python reviewing: Chantae, Katherine

## Notes on how to use and run program:
1. Users:
- Username: ch | Password: password1
- Username: kt | Password: password2
- Username: guest | No password

2. In order to insert tuples from a file, the file must be in 'data folder'.
The attributes must be separated by commas without spaces, and entries must be line separated.
To insert from a file, enter the file name with the .txt extension, but without the path. For example, enter 'artist_data.txt', 'exhi_data.txt', etc.


3. In order to insert from an sql file in database admin access for options 4-7 (create table, create view, alter tables and queries), the user must enter the FULL PATH of the sql file from computer. 
- ex) inserting the file table_py.sql stored in desktop, user would need to enter //User/owner/Desktop/table_py.sql

4. When typing in SQL queries, the user does not need to include semicolons (;) at the end of commands

## Bonus Features:
- In .sql Query file:
  - Completed bonus queries 1), 6), and 7)
  - Implemented a full custom trigger (DATE_VIOLATION) for ART_OBJECT table
- In museum.sql file: Implemented access control using sql commands. Roles and users were created for database. 
- In the python application: Implemented the database admin, data entry, and guest accesses.
