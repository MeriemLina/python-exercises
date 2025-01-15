cities = []

while True:
    city_name = input("enter a city, type stop when you're done..")
    if city_name.lower().strip() == "stop":
        break

    city_info = (city_name.strip(), len(city_name)*1000000)
    cities.append(city_info)

    cities.sort(key=lambda x: x[1], reverse=True)

for city, population in cities:
    print(f"{city} has {population}")