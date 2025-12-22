def list_to_string(list):
    for i in range(len(list)):
        if i < len(list) - 2:
            print(list[i], end=", ")
        elif i == len(list) - 2:
            print(list[i], end=", and ")
        else:
            print(list[i])


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    list_to_string(spam)


if __name__ == "__main__":
    main()
