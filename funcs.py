import re

import sqlite3

from read import connection

#connect to database

connection = sqlite3.connect("vehicle_plateNumber.db")
cursor = connection.cursor()
#create table if not exit
cursor.execute( "CREATE TABLE IF NOT EXISTS plate_numbers"
                "(id INTEGER PRIMARY KEY,plate_no TEXT UNIQUE,car_name TEXT,user_name TEXT,is_deleted INTEGER DEFAULT 0)")
#cursor.execute("ALTER TABLE plate_numbers ADD COLUMN is_deleted INTEGER DEFAULT 0")
connection.commit()
        # Define the regex pattern for the plate numbers
pattern = re.compile(r'^[A-Z]{3}-\d{3}[A-Z]{2}$')
def display_registered_vehicle():
    cursor.execute('SELECT * FROM plate_numbers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'plate_no: {row[1]}')
        print(f'car_name: {row[2]}')
        print(f'user_name: {row[3]}')

def register():
    #Define the regex pattern for the plate number
    while True:

        #get user input
        pattern = re.compile(r'^[A-Z]{3}-\d{3}[A-Z]{2}$')
        plate_no = input('Enter Plate No: ')
        if pattern.match(plate_no):
            break #exit the loop
        else:
            print('Invalid Plate No. please kindly use the format: ABC-123DE')
    car_name = input('Enter Car name: ')
    user_name = input('Enter User name: ')

                #To check if plate number already exits or was deleted
    cursor.execute("SELECT * FROM plate_numbers WHERE plate_no = ?",(plate_no,))
    result = cursor.fetchone()
    if result:
        if result[4] == 1:
            print(f'plate number {plate_no} has been deleted.please visit the admin office to resolve this issue.')
        else:
            print('plate number already registered.')
        return
    #insert into database
    cursor.execute('INSERT INTO plate_numbers(plate_no, car_name, user_name)VALUES(?,?,?)',(plate_no,car_name,user_name))
    connection.commit()
    print("Registered successfully")
   # display_registered_vehicle() #call the new function

def validate():
    # Define the regex pattern for the plate numbers
        while True:
            pattern = re.compile(r'^[A-Z]{3}-\d{3}[A-Z]{2}$')
            #get user input
            plate_no = input('Enter Plate No in this format[ABC-123DE]: ')
            #validate the plate number with the pattern
            if pattern.match(plate_no):
               break
            else:
                print('Invalid Plate No. please kindly use the format: ABC-123DE')
    #check if plate number exists
        cursor.execute('SELECT * FROM plate_numbers WHERE plate_no = ?',(plate_no,))
        result = cursor.fetchone()
        if result:
            if result[4] == 1:
                print(f'plate number {plate_no} has been deleted.please visit the admin office to resolve this issue.')
            else:
                print(f"plate number is registered:{result[1]}" )
                print(f"car name:{result[2]}")
                print(f"user name:{result[3]}")
        else:
            print("plate number is not registered kindly visit number 1 to Register plate number")



def delete_plate():

#get vehicle plate number to delete
 plate_no = input('Enter Plate Number to delete: ')
#to check if plate number exits
 cursor.execute('SELECT * FROM plate_numbers WHERE plate_no = ?',(plate_no,))
 if cursor.fetchone():
    #update is_deleted flag
    cursor.execute('UPDATE plate_numbers SET is_deleted = 1 WHERE plate_no = ?',(plate_no,))
    connection.commit()
    print("Deletion successful.")
 else:
    print('plate number not found')



def help():
    print("To check if your plate number,car name,user name is validated Enter 1.")
    print("To register your plate number,car name,user name Enter 2.")
    print("If you need any help Enter 3.")
    print("To exit the program Enter 4. ")

def exit():
    print("Thank you for using \nREGISTRATION/PLATE NUMBER VERIFICATION SYSTEM ")
