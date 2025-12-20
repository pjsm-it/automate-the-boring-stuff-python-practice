users = {
    "mary": {"password": "swordfish", "email": "mary12@email.com"},
    "john": {"password": "1234", "email": "me@email.com"},
    "pedro": {"password": "amordemae", "email": "imsus@email.com"}
}

attempts = 3

while attempts > 0:
    user_name = input("Username: ").strip().lower()
    user_password = input("Password: ")

    if user_name in users and users[user_name]["password"] == user_password:
        print(f"Access granted. Check your email: {users[user_name]["email"]}")
        break
    else:
        attempts -= 1
        print("Wrong username or password.")
        print(f"Try again! Attempts left: {attempts}.")

if attempts == 0:
    print("Too many attempts.")
