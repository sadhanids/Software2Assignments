from classes.car import Car

new_car = Car("ABC-123", 142 )

print("New Car Properties,")
print(f"""   Registration Number: {new_car.registration_number} 
   Maximum Speed: {new_car.max_speed} 
   Current Speed: {new_car.current_speed} 
   Travelled Distance: {new_car.travelled_distance} """)