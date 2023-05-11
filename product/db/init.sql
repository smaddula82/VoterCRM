create database votercrm;
use votercrm;
create table states(
state_code varchar(100) primary key,
state_name varchar(50),
country varchar(50)
);

insert into states values ("AP","Andhra Pradesh","India");
insert into states values ("TN","Tamilnadu","India");
