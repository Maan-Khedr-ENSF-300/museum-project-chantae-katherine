-- Python Implementation
-- For Create View Function

-- User creates view, displaying Artist_Fname, Artist_Lname, Art_type, Year_created, ArtObj_descrip, Country_of_origin
-- For all art objects include other that are older than the year 2000.
drop view if exists MODERN_ART;

create view MODERN_ART
as select Artist_FName, Artist_LName, Art_type, Year_created, ArtObj_descrip, Country_of_origin 
from ART_OBJECT, ARTIST
where ART_OBJECT.Artist_FName = ARTIST.Fname and ART_OBJECT.Artist_LName = ARTIST.Lname and Year_created > 2000;