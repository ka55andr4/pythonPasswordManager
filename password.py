from cryptography.fernet import Fernet #module that allows us to encrypt text

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#ask user for a master password

key = load_key() 
fer = Fernet(key)

#function for view mode 
def view():
     #opens file and reads it
     with open('passwords.txt', 'r') as f:
         for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", 
                  fer.decrypt(passw.encode()).decode())
        
             
        
#function for add mode 
def add():
    #get username and and password to add
    name = input("Account Name: ")
    pwd = input("Password: ")

    #file for password storing in append mode
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    #ask user if they want to list passwords or add a password
    mode = input("Would you like to add a new password or view passwords (view, add), press q to quit?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue