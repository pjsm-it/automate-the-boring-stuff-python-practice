retirement_age = 66

print("Hello World!")
name = input("Enter your name: ").title().strip()
# print(name)
print(f"Hi! Nice to meet you {name.title().strip()}! I come in peace!")
print(f"Fun fact! Your name's length is: {len(name.strip())}.")
age = int(input("Enter your age: ").strip())
if age >= 0 and age < 21:
    print(f"{name.title().strip()}, you're still a baby!")
elif age < 45:
    print(f"{name.title().strip()}, you are an adult!")
else:
    print(f"{name.title().strip()}, you are getting kind of old, buddy!")
retirement_waiting_time = retirement_age - age
if retirement_waiting_time >= 0:
    print(f"Your are {retirement_waiting_time} years away from retirement!")
else:
    print(f"Congratulations {name}! Enjoy your well deserved rest!")
