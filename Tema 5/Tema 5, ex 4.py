user_name = None
password = None
e_mail = None

while True:
    print("Press 1 to enter the user name")
    print("Press 2 to enter the  password")
    print("Press 3 to enter the  e-mail")
    print("Press 4 to show the details (user, password, e-mail)")
    print(f"Press E/e to exit the program\n")
    alegerea_userului = input("Please enter your choice:")

    if alegerea_userului == "1":
        user_name = input("Please enter your username:")
        print()
    elif alegerea_userului == "2":
        password = input("Please enter your password:")
        print()
    elif alegerea_userului == "3":
        e_mail = input("Please enter your e-mail address:")
        print()
    elif alegerea_userului == "4":
        print(f"\nusername: {user_name}")
        print(f"password: {password}")
        print(f"e-mail: {e_mail}")
        print()
        if user_name is None or password is None or e_mail is None:
            print(f"Please enter data for all NONE fields:\n")
    elif alegerea_userului in ["E", "e"]:
        print("Exiting the program!")
        break
    else:
        print()
        print(f"Invalid input, please try again!\n")