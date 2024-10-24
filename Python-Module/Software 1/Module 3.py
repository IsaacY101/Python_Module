# Exercise 1
size_limit = 42
zan_length = float(input("Enter the length of the zander in centimeters: "))
if zan_length >= size_limit:
    print("The zander meets the size limit.")
else:
    difference = size_limit - zan_length
    print(f"The zander does not meet the size limit. Release it back into the lake.")
    print(f"The zander is {difference:.1f} centimeters below the size limit.")

# Exercise 2
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#Exercise 3
gender = input("Enter your biological gender (male/female): ").strip().lower()
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender entered.")

#Exercise 4
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")