#Ex1
import random

def roll_dice():
    return random.randint(1, 6)
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")
#Ex 2
import random

def roll_dice(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("Enter the number of sides on the dice: "))
    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print(f"Rolled: {roll}")
main()

#Ex3
def gallons_to_liters(gallons):
    return gallons * 3.78541
def main():
    while True:
        gallons = float(input("Enter the volume in gallons (negative value to quit): "))
        if gallons < 0:
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")
main()

#Ex4
def sum_of_list(numbers):
    return sum(numbers)
def main():
    numbers = [1, 2, 3, 4, 5]
    total = sum_of_list(numbers)
    print(f"The sum of the list is: {total}")
main()

#Ex5
def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = remove_odds(numbers)
    print(f"Original list: {numbers}")
    print(f"List after removing odd numbers: {even_numbers}")
main()

#Ex6
import math

def pizza_price_per_sqm(diameter, price):
    radius = diameter / 2
    area_sqm = math.pi * (radius / 100) ** 2
    price_per_sqm = price / area_sqm
    return price_per_sqm

def main():
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))
    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))
    unit_price1 = pizza_price_per_sqm(diameter1, price1)
    unit_price2 = pizza_price_per_sqm(diameter2, price2)
    print(f"Unit price of the first pizza: {unit_price1:.2f} €/sqm")
    print(f"Unit price of the second pizza: {unit_price2:.2f} €/sqm")
    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza offers better value for money.")
    else:
        print("Both pizzas offer the same value for money.")
main()