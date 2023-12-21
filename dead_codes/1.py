# Used functions and variables


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def used_function():
    result = add(5, 3)
    print(f"Used function result: {result}")


used_variable = 10
print(f"Used variable: {used_variable}")

# Unused functions and variables


def divide(a, b):
    """Divide a by b."""
    return a / b


def unused_function():
    print("This function is unused.")


unused_variable = 20


# Main program
if __name__ == "__main__":
    used_function()

# More code...

# Unused code...

# More unused functions and variables


def another_unused_function():

    print("Another unused function.")


another_unused_variable = 30


# More unused code...

# End of the program