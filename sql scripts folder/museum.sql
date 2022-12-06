DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM; 
USE MUSEUM;

DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION (
	E_id				INT NOT NULL,
    Name				VARCHAR(50) NOT NULL,
    Start_date			DATE,
    End_date			DATE,
    PRIMARY KEY (E_id)
);

INSERT INTO EXHIBITION (E_id, Name, Start_date, End_date)
VALUES
(1, "Vivian Maier", "2020-02-08", "2020-05-24"),
(2, "Wolves: The Art of Dempsey Bob", "2022-09-10", "2022-11-20");

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	FName				VARCHAR(20) NOT NULL,
    LName				VARCHAR(20) NOT NULL,
    Main_style			VARCHAR(20),
    Artist_descrip		VARCHAR(300),
    Date_born			DATE,
    Date_died			DATE,
    Epoch				VARCHAR(20),
	Country_of_origin	VARCHAR(30),
	PRIMARY KEY (FName, LName)
);

INSERT INTO ARTIST(FName, LName, Main_style, Artist_descrip, Date_born, Date_died, Epoch, Country_of_origin)
VALUES
("Vivian", "Maier", "Black & White", 
"Vivian Dorothy Maier was an American street photographer whose work was discovered and 
    recognized after her death. She worked for about 40 years as a nanny, mostly 
    in Chicago's North Shore, while pursuing photography.", "1926-02-01", "2009-04-21", "Modern", "United States"),
("Dempsey", "Bob", "Traditional", 
"Dempsey Bob, OC D.Litt is a Northwest Coast woodcarver and sculptor from British Columbia, 
    Canada, who is of Tahltan and Tlingit First Nations descent. He was born in the Tahltan 
    village of Telegraph Creek on the Stikine River in northwestern B.C., and is of the Wolf clan. ",
"1948-01-01", null, "Contemporary", "Canada"),
("Lai Cheuk", "Wah", "Realistic", 
"Sarah Lai Cheuk Wah is best known for her paintings of common objects and urban landscapes, 
    which she renders realistically in great detail. Her visual language is derived from the 
    ordinary, the mundane and the everyday.", "1983-01-01", null, "Contemporary", "Hong Kong"),
("Anish", "Kapoor", "Installation art", 
"Sir Anish Mikhail Kapoor CBE, RA is a British-Indian sculptor specializing in installation 
    art and conceptual art.", "1954-03-12", null, "Contemporary", "United Kingdom");


DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION (
    Name                VARCHAR(25) NOT NULL,
    Contact_person      VARCHAR(20),
    Type                VARCHAR(20),
    C_descrip           VARCHAR(300),
    Address             VARCHAR(40),
    Phone               CHAR(11),
    PRIMARY KEY (Name)    
);

INSERT INTO COLLECTION(Name, Contact_person, Type, C_descrip, Address, Phone)
VALUES
("Glenbow Collection", "Melanie Kjorlien", "Museum", "Glenbow\'s incredible collection of art and objects can provide us with a sense of 
    belonging, an understanding of what it means to live here in Alberta, and an appreciation for the 
    legacy of the remarkable people and events that have shaped our communities.", "130 9 Ave SE, Calgary, AB",
"14032684100"),
("Met Collection", "Tiarra Brown", "Museum", 
"The Metropolitan Museum of Art is one of the world's largest and finest art museums. Its collections include 
    more than two million works of art spanning 5,000 years of world culture, from prehistory to the present 
    and from every part of the globe.", "1000 Fifth Avenue, New York, NY", "12125357710");

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
    Id_no               INT NOT NULL,
    Artist_FName        VARCHAR(20), 
    Artist_LName        VARCHAR(20),
    Year_created        INTEGER,
    Title               VARCHAR(50),
    Origin              VARCHAR(30),
    ArtObj_descrip      VARCHAR(300),
    Art_type            VARCHAR(20) NOT NULL DEFAULT 'OTHER',
    Epoch               VARCHAR(20),
    Borrowed_collection VARCHAR(25),
    Date_borrowed       DATE,
    Date_returned       DATE,
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Artist_FName, Artist_LName) REFERENCES ARTIST(FName, LName) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (Borrowed_collection) REFERENCES COLLECTION(Name) ON UPDATE CASCADE ON DELETE SET NULL
);

-- trigger that requires Date_borrowed and Date_returned to be dates in the past or today's date
delimiter //
CREATE TRIGGER DATE_VIOLATION
BEFORE UPDATE ON ART_OBJECT
FOR EACH ROW
BEGIN
    IF new.Date_borrowed > CURDATE() THEN
        SET new.Date_borrowed = null;
    END IF;
    IF new.Date_returned > CURDATE() THEN
        SET new.Date_returned = null;
    END IF;
END; //

delimiter ;

INSERT INTO ART_OBJECT(Id_no, Artist_FName, Artist_LName, Year_created, Title, Origin, 
ArtObj_descrip, Art_type, Epoch, Borrowed_collection, Date_borrowed, Date_returned)
VALUES
(1, "Vivian", "Maier", 1953, null, "American", "From Street Photography 1", "OTHER", "Modern", "Glenbow Collection", "2020-01-02", "2020-06-15"),
(2, "Dempsey", "Bob", null, "Traders of the Sea", "Tahltan-Tlingit", "5' x 10' Wood panel", "OTHER", "Contemporary", null, null, null),
(3, "Lai Cheuk", "Wah", 2013, "Spotting the Light onto a Light", "Hong Konger", null, "PAINTING", "Contemporary", "Met Collection", "2022-05-06", null),
(4, "Lai Cheuk", "Wah", 2013, "Sugar Rock", "Hong Konger", null, "PAINTING", "Contemporary", "Met Collection", "2022-05-06", null),
(5, "Lai Cheuk", "Wah", 2009, "Sea (night series)", "Hong Konger", null, "OTHER", "Contemporary", null, null, null),
(6, "Lai Cheuk", "Wah", 2001, "A Drowsy Car", "Hong Konger", null, "PAINTING", "Contemporary", null, null, null),
(7, "Anish", "Kapoor", 2006, "Cloud Gate", "British-Indian", "Cloud Gate is a public sculpture.", "STATUE", "Contemporary", "Met Collection",
"2022-02-06", "2022-11-10"),
(8, null, null, 1680, "Marsyas", "German", "The satyr Marsyas screams in the midst of his torture.", "SCULPTURE", "Italian baroque", "Met Collection", "2021-12-12", null),
(9, null, null, 1861, "Woman from the French Colonies", "French", "The idea of the universality of beauty.", "STATUE", "Baroque", null, null, null),
(10, null, null, 1925, "Statue of Balto", "American", "Balto led a team of sled dogs to transport diphtheria antitoxin.", "STATUE", "Modern", null, null, null);

DROP TABLE IF EXISTS ON_DISPLAY;
CREATE TABLE ON_DISPLAY (
    E_id                INT NOT NULL,
    A_id                INT NOT NULL,
    PRIMARY KEY (E_id, A_id),
    FOREIGN KEY (E_id) REFERENCES EXHIBITION(E_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (A_id) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO ON_DISPLAY(E_id, A_id)
VALUES
(1, 1),
(2, 2);

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Drawn_on            VARCHAR(20),
    Paint_type          VARCHAR(20),
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO PAINTING(Id_no, Style, Drawn_on, Paint_type)
VALUES
(3, "Realism", "Canvas", "Oil"),
(4, "Realism", "Paper", "Oil"),
(6, "Realism", "Canvas", "Acrylic");

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Material            VARCHAR(20),
    Height_in_m         FLOAT,  -- in meters
    Weight_in_lb        FLOAT,  -- in lbs
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO SCULPTURE(Id_no, Style, Material, Height_in_m, Weight_in_lb)
VALUES
(7, "Installation art", "Stainless steel", 10, 220000),
(10, "Animalism", "Bronze", 1.3716, 1000);

DROP TABLE IF EXISTS STATUE;
CREATE TABLE STATUE (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Material            VARCHAR(20),
    Height_in_m         FLOAT,  -- in meters
    Weight_in_lb        FLOAT,  -- in lbs
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO STATUE(Id_no, Style, Material, Height_in_m, Weight_in_lb)
VALUES
(8, "Portraiture", "Marble", 0.6858, 133.8),
(9, "Bust", "Marble", 0.96885, 307.1);

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Type                VARCHAR(30),
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO OTHER(Id_no, Style, Type)
VALUES
(1, "Black & White", "Photo"),
(2, "Traditional", "Wood panel"),
(5, "Seascape", "Silverpoint on wood panel");

DROP TABLE IF EXISTS IN_PERMANENT_COLLECTION;
CREATE TABLE IN_PERMANENT_COLLECTION (
    Id_no               INT NOT NULL,
    Cost                DECIMAL(19,2),
    Date_acquired       DATE,
    Status              VARCHAR(10),
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO IN_PERMANENT_COLLECTION(Id_no, Cost, Date_acquired, Status)
VALUES
(2, 1000, "2019-08-15", "on display"),
(5, 2320.20, "2021-09-23", "stored"),
(6, 450, "2022-03-11", "on loan"),
(9, 780, "2020-06-19", "on loan"),
(10, 999.98, "2021-12-09", "stored");


DROP ROLE IF EXISTS db_admin@localhost, data_entry@localhost, read_access@localhost;
CREATE ROLE db_admin@localhost, data_entry@localhost, read_access@localhost;

GRANT ALL PRIVILEGES ON MUSEUM.* TO db_admin@localhost;
GRANT SELECT, INSERT, UPDATE, DELETE ON MUSEUM.* TO data_entry@localhost;
GRANT SELECT ON MUSEUM.* TO read_access@localhost;

DROP USER IF EXISTS ch@localhost, kt@localhost, guest@localhost;
CREATE USER ch@localhost IDENTIFIED WITH mysql_native_password BY 'password1';
CREATE USER kt@localhost IDENTIFIED WITH mysql_native_password BY 'password2';
CREATE USER guest@localhost;

GRANT db_admin@localhost TO ch@localhost;
GRANT data_entry@localhost TO kt@localhost;
GRANT read_access@localhost TO guest@localhost;

SET DEFAULT ROLE ALL TO ch@localhost;
SET DEFAULT ROLE ALL TO kt@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;