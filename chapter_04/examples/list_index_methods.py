spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

print()
spam = ['cat', 'dog', 'bat']
print(spam)
spam.append('moose')
print(spam)
spam.insert(1, 'chicken')
print(spam)
spam.remove('bat')
print(spam)

print()
spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spam = ['a', 'z', 'A', 'Z']
print(spam)
spam.sort(key=str.lower)
print(spam)
spam.sort(key=str.lower, reverse=True)
print(spam)
