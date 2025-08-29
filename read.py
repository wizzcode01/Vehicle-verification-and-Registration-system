import sqlite3
#connect to database

connection = sqlite3.connect("vehicle_plate_num.db")
cursor = connection.cursor()
#create table if not exit
command = "CREATE TABLE IF NOT EXISTS plate_number(id INTEGER PRIMARY KEY,plate_number TEXT,car_name TEXT,owner_name TEXT)"
cursor.execute(command)