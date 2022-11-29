Use MUSEUM;
-- ENSF 300 Final Project 
-- Query Retrieval File

-- 1) Show all tables and explain how they are related to one another(keys,triggers, etc).
select *
from information_schema.table_constraints
where constraint_schema = "museum";

-- 2) A basic retrieval query.
/*
Displaying all the art objects stored in the museum database that includes Id num, year created and title.
*/
select Id_no,Year_created, Title
from ART_OBJECT;

/*
Displaying the contact person, address and phone that is borrowed.
Order them by the art objects Id number. 
*/
select Id_no, Contact_person, Address, Phone
from ART_OBJECT as AOB, COLLECTION as C
where AOB.Borrowed_collection = C.Name
group by Id_no;

-- 3) A retrirval query with ordered results.
/*
Displaying all the art objects based on the date that are only available, when it was created from oldest to newest works.
Displaying the Id number, title, artists' first and last name and year.
*/
select Id_no, Title, Artist_FName, Artist_LName, Year_created
from ART_OBJECT
where Year_created is not null
order by Year_created Asc;

-- 4) A nested retrieval query.
/*
Display all art objects' Id number, the artist first and last name,art object description and year created for the artists that 
are from the United Kingdom.
*/
select  distinct Id_no, Artist_FName, Artist_LName, Artobj_descrip, Year_created
from ARTIST, ART_OBJECT 
where Year_created in
(
select Year_created
from ARTIST, ART_OBJECT 
where Artist_FName = FName and Artist_LName = LName and Country_of_origin = "United Kingdom"
);

-- 5) A retrieval query using joined tables.
/*
Joining the tables for ART_OBJECT and IN_PERMANENT_COLLECTION to retrieval all the Id number, title, artists'
first and last name, the year created and the art type. That are in the permanent collection that is on storage. 
*/
select ART_OBJECT.Id_no, Title, Artist_FName, Artist_LName, Year_created,Art_type
from ART_OBJECT join IN_PERMANENT_COLLECTION on IN_PERMANENT_COLLECTION.Id_no = ART_OBJECT.Id_no
where Status = "stored";

-- 6) An update operation with any necessary triggers.
/*

*/

-- 7) A deletion operation with any necessary triggers.
/*

*/