from classes.car import Car
from classes.race import Race
import random

cars_in_race = 10
car_list =[]

for i in range(cars_in_race):
    max_speed = random.randint(100, 200)
    car = Car('ABC-' + str(i + 1), max_speed)
    car_list.append(car)

race = Race("Grand Demolition Derby", 8000, car_list)

hours = 0
while not race.race_finished():
    race.hours_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()