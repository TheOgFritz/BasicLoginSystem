import time, os 
import json
import hashlib

CurrentUser = ""


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

def LoadUsers():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump({}, file)

    with open(USERS_FILE, "r") as file:
        return json.load(file)

users = LoadUsers() 

def SaveUsers(users): 
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def HashPassword(password): 
    return hashlib.sha256(password.encode()).hexdigest()

def Login():
    users = LoadUsers() 
    time.sleep(1) 
    os.system('cls')
    Tempuser = input("What Is Your Username? \n") 
    if Tempuser in users: 
        Temppassword = input("What Is Your Password? \n") 
        if users[Tempuser]["Password"] == HashPassword(Temppassword): 
            os.system('cls')
            print("Login Successful") 
            CurrentUser = Tempuser 
            time.sleep(1.5)
            os.system('cls')
        else: 
            os.system('cls')
            print("Incorrect Password") 
            time.sleep(1.5) 
            os.system('cls')

def UserOverwrite(User,Pass) :
    users = LoadUsers()
    users[User] = {} 
    users[User]["Password"] = Pass
    SaveUsers(users) 


def SignUp(): 
    users = LoadUsers()
    tempuser = input("What Do You Want Your Username To Be? \n") 
    if tempuser in users: 
        print("Username Already Exists")   
    time.sleep(1) 
    os.system('cls')
    confirm = input(f'Are you sure you want your username to be: {tempuser}? Yes or No \n').strip().lower() 
    time.sleep(1) 
    os.system('cls') 
    if confirm == 'yes': 
        Temppass = input("What Do You Want Your Password To Be? \n") 
        UserOverwrite(tempuser, HashPassword(Temppass))
      
    else: 
        print("Username Not Saved") 
        time.sleep(1.5) 
        os.system('cls') 
    
    


#Main Loop
while True:   
    os.system('cls')
    start = input("Login Or Sign Up? \n").strip().lower() 
    print(start) 
    if start == "login" :    
        os.system('cls') 
        print("Logging In") 
        time.sleep(1.5) 
        Login() 
    elif start == "sign up" : 
        os.system('cls')
        print("Signing Up") 
        time.sleep(1.5) 
        os.system('cls')
        SignUp()  
    else: 
        print("Invalid Input") 
        time.sleep(2) 
        os.system('cls')


