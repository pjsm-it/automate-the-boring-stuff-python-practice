def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


def run_collatz_sequence():
    while True:
        try:
            number = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    while number != 1:
        number = collatz(number)


def main():
    run_collatz_sequence()


if __name__ == "__main__":
    main()
