from classes.car import ElectricCar, GasolineCar
import random

electric_car = ElectricCar("ABC-15", 180, 52.5)

gasoline_car = GasolineCar("ACD-123", 165, 32.3)

driving_time = 3

random_speed_ec = random.randint(80, 120)
electric_car.accelerate(random_speed_ec)

print(f"Starting speed for Electric Car ABC-15: {electric_car.current_speed} km/h")

electric_car.drive(driving_time)

random_speed_gc = random.randint(90, 130)
gasoline_car.accelerate(random_speed_gc)

print(f"Starting speed for Gasoline Car ACD-123: {gasoline_car.current_speed} km/h")

gasoline_car.drive(driving_time)

print("Electric Car (ABC-15):")
electric_car.print_information()

print("Gasoline Car (ACD-123):")
gasoline_car.print_information()
