from mathlib.utils.convert_to_num import to_number


class Calculator:
    """Arithmetic calculator supporting int, float, and numeric strings."""

    def add(self, a, b):
        a = to_number(a)
        b = to_number(b)
        return a + b

    def subtract(self, a, b):
        a = to_number(a)
        b = to_number(b)
        return a - b

    def multiply(self, a, b):
        a = to_number(a)
        b = to_number(b)
        return a * b

    def divide(self, a, b):
        a = to_number(a)
        b = to_number(b)

        if b == 0:
            raise ValueError("Division by zero is not allowed")

        return a / b
