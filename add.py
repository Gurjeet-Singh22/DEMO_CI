def add_numbers(a: int, b: int) -> int:
    """Return the sum of two numbers"""
    return a + b


if __name__ == "__main__":
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid integers.")
