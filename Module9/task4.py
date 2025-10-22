from classes.car1 import Car
import random
from tabulate import tabulate

car_list = []

race_duration_hours = 0

for i in range(10):
    max_speed = random.randint(100,200)
    car = Car('ABC-' + str(i + 1), max_speed)
    car_list.append(car)

while max(car.travelled_distance for car in car_list) < 10000:
    race_duration_hours += 1
    for car in car_list:
        car.accelerate()
        car.drive(1)

car_list.sort(key=lambda car:car.travelled_distance, reverse=True)

print(f"Race Finished: Total Duration: {race_duration_hours} hours")

table_data = []
headers = ["Place", "Registration No", "Max Speed", "Distance"]
for i, car in enumerate(car_list):
    if i == 0:
        place_str = "1st Place"
    elif i == 1:
        place_str = "2nd Place"
    elif i == 2:
        place_str = "3rd Place"
    else:
        place_str = f" {i+1}th Place"

    table_data.append([
        place_str,
        car.registration_number,
        car.max_speed,
        f"{car.travelled_distance}"
    ])

print(tabulate(table_data, headers = headers, tablefmt='grid',numalign='right'))
