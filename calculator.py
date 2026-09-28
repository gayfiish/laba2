def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Неизвестная операция"


if __name__ == "__main__":
    print(calculator(10, 5, "+"))
    print(calculator(10, 5, "/"))