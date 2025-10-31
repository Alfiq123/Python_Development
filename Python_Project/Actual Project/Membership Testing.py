MEMBERS = {}
CURRENT_MEMBER = None

MEMBER_FILE = "members.txt"

def load_members():
    global MEMBERS
    try:
        with open(MEMBER_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(":", 1)
                    MEMBERS[username] = password
    except FileNotFoundError:
        pass

def save_members():
    with open(MEMBER_FILE, "w") as f:
        for username, password in MEMBERS.items():
            f.write(f"{username}:{password}\n")

def register():
    print("--- Register ---")
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in MEMBERS:
        print("Username already taken. Please choose another.")
        return

    password = input("Choose a password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    MEMBERS[username] = password
    save_members()
    print("Registration successful! You can now log in.")

def login():
    global CURRENT_MEMBER
    if CURRENT_MEMBER:
        print(f"You are already logged in as {CURRENT_MEMBER}.")
        return

    print("--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in MEMBERS and MEMBERS[username] == password:
        CURRENT_MEMBER = username
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print("Invalid username or password.")

def logout():
    global CURRENT_MEMBER
    if CURRENT_MEMBER:
        print(f"Goodbye, {CURRENT_MEMBER}. You have been logged out.")
        CURRENT_MEMBER = None
    else:
        print("You are not currently logged in.")

def access_member_content():
    if CURRENT_MEMBER:
        print(f"\n--- Member Content for {CURRENT_MEMBER} ---")
        print("This is super secret information only for members!")
        print("Here's your secret discount code: MEMBER2024!")
        print("------------------------------------\n")
    else:
        print("You must be logged in to access member content.")

def show_menu():
    print("\n--- Membership System ---")
    if CURRENT_MEMBER:
        print(f"Logged in as: {CURRENT_MEMBER}")
    else:
        print("Not logged in.")
    print("1. Register")
    print("2. Login")
    print("3. Access Member Content")
    if CURRENT_MEMBER:
        print("4. Logout")
    print("5. Exit")
    print("-------------------------")

def main():
    load_members()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            access_member_content()
        elif choice == '4' and CURRENT_MEMBER:
            logout()
        elif choice == '5':
            print("Exiting membership system. See you next time!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()