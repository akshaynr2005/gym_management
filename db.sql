create database gym_db;
use gym_db;
create table member(id int auto_increment primary key,
name varchar(100),
place varchar(100),
plan enum("1 month","2 months","3 months","6 months","8 months","1 year"),
mobile varchar(100) unique,
fee int,
joining_date date);
select * from member;
