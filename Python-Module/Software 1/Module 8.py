#E1
import sqlite3
def get_airport_details(icao_code):
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    if result:
        name, municipality = result
        print(f"Airport Name: {name}")
        print(f"Location (Town): {municipality}")
    else:
        print(f"No airport found with ICAO code: {icao_code}")
    connection.close()
icao_code = input("Enter the ICAO code of the airport: ").upper()
get_airport_details(icao_code)

#Ex2
import sqlite3


def get_airports_by_area(area_code)
    cursor = connection.cursor()
    results = cursor.fetchall()
    if results:
        print(f"Airports in country {area_code.upper()} by type:")
        for airport_type, count in results:
            print(f"{airport_type}: {count} airports")
    else:
        print(f"No airports found for the country code: {area_code}")
    connection.close()
area_code = input("Enter the area code (for example, FI for Finland): ").upper()
get_airports_by_area(area_code)

#Ex3
import sqlite3

def get_airports_by_area(area_code)
    cursor = connection.cursor()
    cursor.execute(query, (area_code.upper(),))
    # Fetch all results
    results = cursor.fetchall()
    if results:
        print(f"Airports in country {area_code.upper()} by type:")
        for airport_type, count in results:
            print(f"{airport_type}: {count} airports")
    else:
        print(f"No airports found for the country code: {area_code}")
    connection.close()
area_code = input("Enter the area code (for example, FI for Finland): ").upper()
get_airports_by_area(area_code)

