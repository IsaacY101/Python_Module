#Ex1
def month_to_season():
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    month = int(input("Enter the number of the month (1-12): "))
    if month in [12, 1, 2]:
        season = seasons[0]
    elif month in [3, 4, 5]:
        season = seasons[1]
    elif month in [6, 7, 8]:
        season = seasons[2]
    elif month in [9, 10, 11]:
        season = seasons[3]
    else:
        season = "Invalid month!"
    print(f"The season is: {season}")
month_to_season()

#Ex2
def check_names():
    names_set = set()
    while True:
        name = input("Enter a name (or press Enter to finish): ")

        if name == "":
            break
        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)
    print("\nEntered names:")
    for name in names_set:
        print(name)
check_names()

#Ex3
def airport_data():
    airports = {}
    while True:
        print("\n1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        option = input("Choose an option (1, 2, or 3): ")
        if option == "1":
            icao = input("Enter the ICAO code: ").upper()
            name = input("Enter the airport name: ")
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} added.")
        elif option == "2":
            icao = input("Enter the ICAO code: ").upper()
            if icao in airports:
                print(f"The airport name is: {airports[icao]}")
            else:
                print("Airport not found.")
        elif option == "3":
            # Quit the program
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")
airport_data()
