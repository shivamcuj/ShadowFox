# This program checks if a given city is in Australia, UAE, or India and prints the corresponding country name. If the city is not found in any of these countries, it prints a message indicating that the city was not found.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter a City name: ").title()
city2 = input("Enter a City name: ").title()

if city1 in Australia and city2 in Australia:
    print(f"Both {city1} and {city2} are in Australia")

elif city1 in UAE and city2 in UAE:
    print(f"Both {city1} and {city2} are in UAE")

elif city1 in India and city2 in India:
    print(f"Both {city1} and {city2} are in India")

else:
    print(f"{city1} and {city2} don't belong to the same country")S