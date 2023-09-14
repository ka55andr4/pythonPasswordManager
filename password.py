#ask user for a master password
password = input ("Enter master password")

while True:
    #ask user if they want to list passwords or add a password
    mode = input("Would you like to add a new password or view passwords (view, add), press q to quit?").lower()
    if mode == "q":
        break
    
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid input")
        continue