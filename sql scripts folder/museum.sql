DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM; 
USE MUSEUM;

DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION (
	E_id				INT NOT NULL,
    Name				VARCHAR(30) NOT NULL,
    Start_date			DATE,
    End_date			DATE,
    PRIMARY KEY (E_id)
);

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	FName				VARCHAR(20) NOT NULL,
    LName				VARCHAR(20) NOT NULL,
    Main_style			VARCHAR(25),
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

-- 4. ART_OBJECT
-- 	• Id_no: INT NOT NULL
-- 	• Artist: can be null
-- 	• Year: can be null
-- 	• Title
-- 	• Origin
-- 	• ArtObj_descrip
-- 	• Art_type
-- 	• Epoch
-- 	• Artist_name
-- 	• Borrowed_collection
-- 	• Date_borrowed
-- Date_returned

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT (
    Id_no               INT NOT NULL,
    Artist_FName        VARCHAR(20), 
    Artist_LName        VARCHAR(20),
    Year                INTEGER,
);