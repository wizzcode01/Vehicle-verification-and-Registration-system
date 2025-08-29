
filename = 'database.csv'
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Plate Number', 'Car Name', 'User name'])
   with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(updated_rows)
                for row in reader:
                    if check in row[0]:
                        print(f'found plate number: {row[0]} Car name: {row[1]} User name: {row[2]}')
                        found = True
                        break  # exit the loop once the plate number is found
                if not found:
                    print('Invalid plate number, kindly visit 2.to register plate number using this format: ABC-123DE')
  #read all rows from the file
    try:

             current_entries = [row for row in reader]
            # show current entries for clarity
             print("current entries:")
             for row in current_entries:
                print(row)

            #filter out the row with the specified plate number
             updated_rows= [row for row in current_entries if len(row) > 0 and row[0] != delete_plate]
            #check if deletion was successful
             if len(updated_rows) == len(current_entries):
                 print(f'Plate number {delete_plate} not found.')
                 return
             else:
                 print(f'Plate number {delete_plate} has been deleted.')

                #write updated row back to file

                     #add new registration
                 add_new = input("Add new entry? (yes/no): ")
                 if add_new == 'yes':
                     while True:
                        pattern = re.compile(r'^[A-Z]{3}-\d{3}[A-Z]{2}$')
                        plateNo = input('Enter plate number: ')
                        if pattern.match(plateNo):
                           break
                 username = input('Enter Username: ')
                 carName = input('Enter Car name: ')

print('New entry registered successfully.')


    except FileNotFoundError:
                      print('File not found.')
    except Exception as e:
        print(f"An error occurred: {e}")
print(f"plate number validated: {result[1]}")
            print(f"car_name: {result[2]}")
            print(f"user_name: {result[3]}")