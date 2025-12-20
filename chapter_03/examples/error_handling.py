def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    except Exception as e:
        print(f'Unexpected error: {e}')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print(spam('a'))
