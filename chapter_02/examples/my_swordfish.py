MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    print("Identify yourself, stranger:")
    user_name = input("Enter your username: ").strip()

    if user_name.lower() != "alex":
        print("User not recognized. Try again.\n")
        attempts += 1
        continue

    print("Welcome, Alex. Please provide the secret code.")
    secret_code = input("Enter the secret code: ").strip()

    if secret_code == "oceanwave":
        print("Access granted. You may proceed!")
        break
    else:
        print("Wrong code. Try again.\n")
        attempts += 1

else:
    print("Maximum login attempts reached. Access denied.")
