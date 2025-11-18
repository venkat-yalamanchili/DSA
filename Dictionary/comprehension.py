import random

city_names = ["Paris","Los Angeles","New York","London"]

new_dict = {city:random.randint(20,30) for city in city_names}

print(new_dict)

new_dict1 = {city:value for city,value in new_dict.items() if value >= 25}
print(new_dict1)