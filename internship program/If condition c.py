australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in australia:
    country1 = "Australia"

elif city1 in uae:
    country1 = "UAE"

elif city1 in india:
    country1 = "India"

else:
    print(city1,"is not found in any of the countries")
    exit()


if city2 in australia:
    country2 = "Australia"

elif city2 in uae:
    country2 = "UAE"

elif city2 in india:
    country2 = "India"

else:
    print(city2,"is not found in any of the countries")
    exit()


if country1 == country2:
    print("Both cities are in",country1)
else:
    print("They don't belong to the same country")