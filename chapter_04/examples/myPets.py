myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a oet named ' + name.title())
else:
    print(name.title() + ' is my pet.')
