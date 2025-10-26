import random
from tabulate import tabulate

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list


    def hours_passes(self):
        for car in self.car_list:
            speed_change = random.randint(10,20)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"Race Status: ")

        table_data = []
        headers = ["Name", "Distance", "Car List"]
        for i, car in enumerate(self.car_list):
            if i == 0:
                place_str = "1st Place"
            elif i == 1:
                place_str = "2nd Place"
            elif i == 2:
                place_str = "3rd Place"
            else:
                place_str = f" {i + 1}th Place"

            table_data.append([
                place_str,
                car.registration_number,
                car.max_speed,
                f"{car.travelled_distance}"
            ])

        print(tabulate(table_data, headers=headers, tablefmt='grid', numalign='right'))

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
            else:
                return False
