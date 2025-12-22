spam = ['cat', 'bat', 'rat', 'elephant']

print(f"The {spam[-1]} is afraid of the {spam[-2]}.")

print()
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[1:])
print(spam[:])

print()
print(len(spam))

print()
print(spam[1])
spam[1] = 'aardvark'
print(spam)

print()
spam = spam + ['1', '2', '3']
print(spam)

print()
del spam[-1]
print(spam)

print()
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print()
greetings = ['helo', 'hi', 'howdy', 'heyas']

print('howdy' in greetings)
print('cat' not in greetings)
