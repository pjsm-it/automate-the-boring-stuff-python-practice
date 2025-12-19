client_name = input("Enter the client's first and last name: ").strip().lower()
# print(client_name)

with open("clients.txt", "r") as f:
    clients = [line.strip().lower() for line in f]

if client_name in clients:
    print(f"{client_name.title()} found!")
else:
    print(f"{client_name.title()} not found!")
