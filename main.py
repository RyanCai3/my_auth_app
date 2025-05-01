import bcrypt

# LOGIN FUNCTION
# Prompts the user for username and password
def login_page(): 
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check stored data in CSV file
    try:
        with open("source.csv", "r") as source:
            for line in source:
                s_username, s_password = line.rstrip().split(",")
                # Check if the username matches
                if username == s_username:
                    # Compare input password with hashed password
                    if bcrypt.checkpw(password.encode(), s_password.encode()):
                        print("Login successful!")
                        main_menu()
                        return
                    else:
                        print("Invalid username or password.")
                        return
        # If username doesn't exist
        print("Invalid username or password.")
    
    # Create new CSV file if there is none existing
    except FileNotFoundError:
        with open("source.csv", "w") as source:
            pass
        print("A new user database has been created.\nPlease register in new user database.")
        return

# MAIN MENU
# Lets the user change their password or logout
def main_menu(): 
    while True:
        menu_task = input("Hello user, what would you like to do:\n Change Password\n Logout\n").strip().lower()
        if menu_task == "change password":
            change_password()
            break
        elif menu_task == "logout":
            break
        else:
            print("Please choose an available option.")

# PASSWORD CHANGE
# Prompts the user for their username and a new password
def change_password(): 
    username = input("Enter your username: ")
    new_password = input("Enter new password: ")
        
    # Check if password length is at least 4 letters
    if len(new_password) < 4:
        print("Password too short!")
        return
        
    # Hash new password
    hashed_new = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
    rows = []
        
    # Reads stored data in CSV file
    try:
        with open("source.csv", "r") as source:
            for line in source:
                s_username, s_password = line.rstrip().split(",")
                # If username matches, update the password hash
                if username == s_username:
                    rows.append(f"{s_username},{hashed_new}")
                # Keep other rows unchanged
                else:
                    rows.append(line.rstrip())
            
        # Write updated data back to CSV file
        with open("source.csv", "w") as source:
            source.write("\n".join(rows) + "\n")
        
        print("Password changed successfully!")
        return
    
    # Create new CSV file if there is none existing
    except FileNotFoundError:
        with open("source.csv", "w") as source:
            pass
        print("A new user database has been created.\nPlease register in new user database.")
        return

# REGISTRATION PAGE
# Prompts the user for a new username and password
def register_user(): 
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")
    
    # Check if password length is at least 4 letters
    if len(new_password) < 4:
        print("Password too short!")
        return
    
    # Check stored data in CSV file whether if the username already exists
    try:
        with open("source.csv", "r") as source:
            for line in source:
                s_username, _ = line.rstrip().split(",")
                if s_username == new_username:
                    print("Username taken.")
                    return
    
    # Create new CSV file if there is none existing
    except FileNotFoundError:
        with open("source.csv", "w") as source:
            pass
        print("A new user database has been created.\nPlease register in new user database.")
        return
    
    # Hash the password and save new login details
    hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
    with open ("source.csv", "a") as source:
        source.write(f"{new_username},{hashed}\n")
    print("New login details saved.")

# STARTING MENU
# Lets the user login, register, or quit
while True: 
    user_request = input("What would you like to do:\n Login\n Register\n Quit\n").strip().lower()
    
    # Take user to login page
    if user_request == "login":
        login_page()
    # Take user to registration page
    elif user_request == "register":
        register_user()
    # Exit program
    elif user_request == "quit":
        break
    # Invalid input
    else:
        print("Please choose an available option.")