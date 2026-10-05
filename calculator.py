class Calculator:
    def __init__(self, a: float = 0, b: float = 0):
        self.a = a
        self.b = b

    def input(self):
        self.a = float(input("input a = "))
        self.b = float(input("input b = "))

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        # try:
        #     return self.a / self.b
        # except (ValueError, ZeroDivisionError) as mess:
        #     return "Error", mess
        if self.b == 0:
            raise ZeroDivisionError("Error b = 0")
        else:
            return self.a / self.b


calc = Calculator()
calc.input()
print(f"{calc.add()} / {calc.subtract()} / {calc.multiply()} / {calc.divide()}")
