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
(2, "One New Work: Ron Moppett", "2020-02-08", "2020-11-29"),
(3, "Wolves: The Art of Dempsey Bob", "2022-09-10", "2022-11-20");


DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	FName				VARCHAR(20) NOT NULL,
    LName				VARCHAR(20) NOT NULL,
    Main_style			VARCHAR(20),
    Artist_descrip		VARCHAR(250),
    Date_born			DATE,
    Date_died			DATE,
    Epoch				VARCHAR(20),
	Country_of_origin	VARCHAR(30),
	PRIMARY KEY (FName, LName)
);

DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION (
    Name                VARCHAR(25) NOT NULL,
    Contact_person      VARCHAR(20),
    Type                VARCHAR(20),
    C_descrip           VARCHAR(250),
    Address             VARCHAR(30),
    Phone               CHAR(11),
    PRIMARY KEY (Name)    
);

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
    Id_no               INT NOT NULL,
    Artist_FName        VARCHAR(20), 
    Artist_LName        VARCHAR(20),
    Year_created        INTEGER,
    Title               VARCHAR(30),
    Origin              VARCHAR(30),
    ArtObj_descrip      VARCHAR(250),
    Art_type            VARCHAR(10) NOT NULL DEFAULT 'OTHER',
    Epoch               VARCHAR(20),
    Borrowed_collection VARCHAR(25),
    Date_borrowed       DATE,
    Date_returned       DATE,
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Artist_FName, Artist_LName) REFERENCES ARTIST(FName, LName),
    FOREIGN KEY (Borrowed_collection) REFERENCES COLLECTION(Name)
);

DROP TABLE IF EXISTS ON_DISPLAY;
CREATE TABLE ON_DISPLAY (
    E_id                INT NOT NULL,
    A_id                INT NOT NULL,
    PRIMARY KEY (E_id, A_id),
    FOREIGN KEY (E_id) REFERENCES EXHIBITION(E_id),
    FOREIGN KEY (A_id) REFERENCES ART_OBJECT(Id_no)
);

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Drawn_on            VARCHAR(20),
    Paint_type          VARCHAR(20),
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
    Id_no               INT NOT NULL,
    Style               VARCHAR(20),
    Material            VARCHAR(20),
    Height              FLOAT,
    Weight              FLOAT,
    PRIMARY KEY (Id_no),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);