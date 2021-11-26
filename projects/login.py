class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    print("Login, Register")
    a = input("What would you like to do: ")
    if(a == "register" or a == "Register"):
        register()
    elif(a == "Login" or a == "login"):
        login(user)
    else:
        print("Choose a valid option")
        home('')

def register():
    n = input("Name: ")
    u = input("Username: ")
    p = input("Password: ")
    u = User(n, u, p)
    print("Welcome, " + u.name)
    home(u)


def login(user):
    l = input("Username: ")
    l2 = input("Password")
    if(l2 == user.password):
        print("Welcome, " + user.name)
    else:
        print("Incorrect username or password")
        login(user)
    home('')

home('')