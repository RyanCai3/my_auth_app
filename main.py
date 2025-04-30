# The login page, called when the user chose "login"
def login_page():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("source.csv") as source:
        for line in source:
            s_username, s_password = line.rstrip().split(",")
    main_menu()

# The main menu, called when the user logs in
def main_menu():
    while True:
        m_task = input("Hello user, what would you like to do: \n Change Password \n Logout\n")
        if m_task == "Change Password":
            change_password()
        elif m_task == "Logout":
            break
        else:
            print("Please choose an available option.")

# To change the user's password, called when the user chose "cahnge password"
def change_password():
    while True:
        changed_password = input("Enter new password: ")
        if len(changed_password) < 4:
            print("Password too short.")
        else:
            print("Password changed.")
            break
    main_menu()

# User register page, called when the user chose "register"
def register_user():
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    with open("source.csv", "a") as source:
        source.write(f"\n{new_username},{new_password}")
    print("New login details saved.")

# The first page the user sees, leads onto other pages
while True:
    task = input("What would you like to do: \n Login \n Register \n Quit\n")
    if task == "Login":
        login_page()
        break
    elif task == "Register":
        register_user()
    elif task == "Quit":
        break
    else:
        print("Please choose an available option.")