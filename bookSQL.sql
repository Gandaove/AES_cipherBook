create database if not exists cipherBook;
create user bookuser@'%' identified with mysql_native_password by 'cipherbook';     ---use old verify
grant all privileges on cipherBook.* to 'bookuser'@'%';
use cipherBook;
drop table if exists BookList;
create table if not exists BookList(bookname varchar(255) not null primary key, question text, key_hash char(64) not null, content mediumtext not null) ENGINE=InnoDB DEFAULT CHARSET=utf8;
