-- Python Implementation
-- Create Table Function 

-- Admin creates a simple table for new art objects for art objects categorized as pottery
 drop table if exists POTTERY;

create table POTTERY
(
 Id_no         int not null,
 style         varchar(50),
 Material      varchar(20),
 Ceramic_type  varchar(20),
 primary key(Id_no)
);