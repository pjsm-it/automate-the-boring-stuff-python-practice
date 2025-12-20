import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit'.lower():
        sys.exit()
    print('You typed ' + response + '.')
