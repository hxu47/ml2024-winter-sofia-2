from module5_oop import NumberFinder

def main():
    finder = NumberFinder()

    n = int(input("Please input a positive integer: "))
    print(f"N = {n}")
    finder.read_numbers(n)

    x = int(input("\nEnter the number to find: "))
    index = finder.find_number(x)

    print(f"\nThe index of {x} is: {index}")
