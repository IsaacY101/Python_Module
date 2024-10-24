#Ex1
import random
def roll_dice():
    num_dice = int(input("How many dice would you like to roll? "))
    total_sum = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total_sum += roll
    print(f"The sum of the dice rolls is: {total_sum}")
roll_dice()

#Ex2
def greatest_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    numbers.sort(reverse=True)
    greatest_five = numbers[:5]
    print("The five greatest numbers are:")
    for number in greatest_five:
        print(number)
greatest_numbers()

#Ex3
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def prime_checker():
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
prime_checker()

#Ex4
def city_names():
    cities = []
    for _ in range(5):
        city = input("Enter the name of a city: ")
        cities.append(city)
    print("The cities you entered are:")
    for city in cities:
        print(city)
city_names()