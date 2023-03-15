import sqlite3
import os

#check if database exists
if os.path.exists('education.db'):
    os.remove('education.db')

#connect to database education.db
conn = sqlite3.connect('education.db')

#create a cursor
c = conn.cursor()

#create table students
c.execute("""CREATE TABLE students (
	`studentID` 		int NULL,
	`collegeID` 		int NULL,	
	`firstName` 		varchar (20) NULL ,
	`lastName` 			varchar (20) NULL ,	
	`birthDate` 		date NULL ,	
	`email` 			varchar (30) NULL ,
	`city` 				varchar (15) NULL ,
	`region` 			varchar (15) NULL ,
	`country` 			varchar (15) NULL
)""")

#create table colleges
c.execute("""CREATE TABLE colleges (
    `collegeID` 		int NULL,
	`name` 				varchar (20) NULL,
	`students` 			int NULL,	
	`city` 				varchar (15) NULL ,
	`region` 			varchar (15) NULL ,	
	`country` 			varchar (15) NULL 
)""")

#verify tables creation
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(c.fetchall())

