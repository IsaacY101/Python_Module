#Exercise 1
name = input("What is your name? : ")
print(f"Hello, {name}! ")

#Exercise 2
import math
r = float(input("What is the radius of the circle? : "))
print(f"Area of the Circle is {math.pi*r**2:.2f}")

#Exercise 3
rect_L = float(input("What is the length of the rectangle? : "))
rect_W = float(input("What is the width of the rectangle? : "))
Peri_rect = 2*rect_L * 2*rect_W
area_rect = rect_L * rect_W
print(f"The area of the rectangle is: {area_rect:.1f}")
print(f"The perimeter of the rectangle is: {Peri_rect:.1f}")

#Exercise 4
num1 = int(input("Give three Integer numbers : "))
num2 = int(input())
num3 = int(input())
print(f"The sum of the numbers is: {num1+num2+num3}, The product is: {num1*num2*num3}, The average is: {(num1+num2+num3)/3}")

#Exercise 5
print("Enter Talents")
talents = float(input())
print("Enter Pounds")
pounds = float(input())
print("Enter Lots")
lots = float(input())
w_kg = ((talents*20+pounds)*32 + lots)*0.0133
w_g = 1000*(w_kg - int(w_kg))
print(f"The weight in Modern unit is: \n{int(w_kg)} Killograms and {w_g:.2f} Grams")

#Excercise 6
import random
comb_1 = [random.randint(0, 9) for _ in range(3)]
comb_2 = [random.randint(1, 6) for _ in range(4)]
print("3-digit code:", comb_1)
print("4-digit code:", comb_2)