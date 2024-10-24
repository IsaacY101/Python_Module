#Exercise 1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#Exercise 2
def inches_to_centimeters(inches):
    return inches * 2.54
def main():
    while True:
        try:
            inches = float(input("Enter the number of inches (negative to quit): "))
            if inches < 0:
                print("Negative value entered. Exiting.")
                break
            centimeters = inches_to_centimeters(inches)
            print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()

#Exercise 3
def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"The smallest number is {smallest}")
        print(f"The largest number is {largest}")
    else:
        print("No numbers were entered.")
if __name__ == "__main__":
    main()

#Exercise 4
import random
def main():
    number_to_guess = random.randint(1, 10)
    print("I have selected a number between 1 and 10. Try to guess it!")
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < number_to_guess:
                print("Too low!")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print("Correct! You've guessed the number!")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()

#Exercise 5
def main():
    correct_username = "python"
    correct_password = "rules"
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_username and password == correct_password:
            print("Welcome!")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect credentials. You have {max_attempts - attempts} attempts left.")
            else:
                print("Access denied. You have exceeded the maximum number of attempts.")

if __name__ == "__main__":
    main()

#Exercise 6
import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_approximation = 4 * (inside_circle / num_points)
    return pi_approximation
def main():
    try:
        num_points = int(input("Enter the number of random points to generate: "))
        if num_points <= 0:
            print("Please enter a positive integer.")
            return
        pi_estimate = estimate_pi(num_points)
        print(f"Approximation of π: {pi_estimate}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")
if __name__ == "__main__":
    main()
