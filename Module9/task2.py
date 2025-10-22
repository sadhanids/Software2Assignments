from classes.car import Car

new_car = Car("ABC-123", 142 )

print(f"Initial Speed: {new_car.current_speed} km/h")

new_car.accelerate(30)
print(f"Speed Increased by 30 km/h, Current Speed: {new_car.current_speed} km/h")

new_car.accelerate(70)
print(f"Speed Increased by 70 km/h, Current Speed: {new_car.current_speed} km/h")

new_car.accelerate(50)
print(f"Speed Increased by 50 km/h, {new_car.current_speed} km/h")

new_car.accelerate(-200)
print(f"Speed Decreased by 200 km/h, {new_car.current_speed} km/h")
