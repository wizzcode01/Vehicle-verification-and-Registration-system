import funcs

while True:
    print('-' * 40)
    print('WELCOME TO REGISTRATION/PLATE NUMBER VERIFICATION SYSTEM ')
    print('-' * 40)

    print('1. Validate plate number')
    print('2. Register plate number')
    print('3. Delete plate number')
    print('4. Display registered vehicles')
    print('5. Help')
    print('6. Exit\n')

    choose = input('Enter your choice: ')
    if choose == '1':
        funcs.validate()
    if choose == '2':
        funcs.register()
    if choose == '3':
        funcs.delete_plate()
    if choose == '4':
        funcs.display_registered_vehicle()
    if choose == '5':
        funcs.help()
    if choose == '6':
        funcs.exit()
        break
