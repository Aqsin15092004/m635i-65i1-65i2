# app.py - Demo Python Application


def add(a, b):
    """Add two numbers"""
    return a + b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"4 x 6 = {multiply(4, 6)}")
    print(f"5! = {factorial(5)}")
