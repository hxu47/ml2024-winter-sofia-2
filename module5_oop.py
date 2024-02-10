class NumberFinder:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        print(f"\nPlease input {n} numbers one by one.")
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            self.numbers.append(num)

    def find_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
