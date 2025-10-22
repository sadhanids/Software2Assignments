from classes.car import Car

new_car = Car("ABC-123", 142 )

new_car.travelled_distance = 2000
new_car.accelerate(60)

print(f"Initial Travelled Distance: {new_car.travelled_distance} km")

new_car.drive (1.5)
print(f"New Travel Distance: {new_car.travelled_distance} km")


