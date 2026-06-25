# This program checks if a given city is in Australia, UAE, or India and prints the corresponding country name. If the city is not found in any of these countries, it prints a message indicating that the city was not found.
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a City name: ").title()

if city in Australia:
    print(f"{city} is in Australia")

elif city in UAE:
    print(f"{city} is in UAE")

elif city in India:
    print(f"{city} is in India")

else:
    print(f"Not able to find {city}")