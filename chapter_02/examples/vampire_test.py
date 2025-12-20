print(
    "Hello possible fiend!\nWelcome to M.O.R.G.A.N.A - Monitoring "
    "of Rare Gothic and Nocturnal Anomalies")

fiend_name = input("Enter your name, possible fiend: ").strip().title()
while True:
    try:
        fiend_age = int(input("Enter your age, possible fiend: ").strip())
        break
    except ValueError:
        print("Please enter a valid number for age.")

print(f"\nHello, {fiend_name}.")

if fiend_age < 12:
    print("Nothing suspicious here. You are a human child.")
elif fiend_age < 90:
    print("Nothing suspicious here. You are a human adult.")
elif fiend_age <= 150:
    print("This is looking kinda sus!")
else:
    print("For sure a vampire!\nSelect your extermination method!")
    print(
        "1 - Stake to the heart\n2 - Sunlight\n3 - "
        "Cocktail spiked with holy water")

    while True:
        extermination_method = input(
            "Please, select an option (1-3): ").strip()
        if extermination_method in ["1", "2", "3"]:
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

    if extermination_method in ["1", "2"]:
        print(
            "Please walk to the red 'X' on the floor next to you "
            "and wait for extermination!")
    elif extermination_method == "3":
        print(
            "Please wait for our mixologist robot"
            " to bring you your beverage!")

    print("Thank you for your cooperation!")
