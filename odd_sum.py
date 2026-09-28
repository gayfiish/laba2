def sum_odd_numbers(n):
    result = 0

    for number in range(1, n + 1):
        if number % 2 != 0:
            result += number

    return result


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Sum of odd numbers:", sum_odd_numbers(n))