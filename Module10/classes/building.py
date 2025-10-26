from Module10. classes.elevator import Elevator

class Building:
    def __init__ (self, new_number_of_top_floor,new_number_of_bottom_floor,no_of_elevators):
        self.top_floor = new_number_of_top_floor
        self.bottom_floor = new_number_of_bottom_floor
        self.is_fire_alarm_warning = False
        self.elevators = []
        for i in range(no_of_elevators):
            new_elevator = Elevator(self.bottom_floor,self.top_floor)
            self.elevators.append(new_elevator)
            print(f"Created Elevator {i+1}, Commencing at floor {self.bottom_floor}")

    def run_elevator(self, elevator_number, destination_floor ):
# the elevator number starts from 0
        if 0 <= elevator_number < len(self.elevators):
            selected_elevator = self.elevators[elevator_number]
            print(f"Elevator {elevator_number} to floor {destination_floor}")
            selected_elevator.go_to_floor(destination_floor)
        else:
            print(f"{elevator_number} is Invalid Elevator Number")

    def fire_alarm(self):
        self.is_fire_alarm_warning = True
        print("Fire Alarm Warning! All elevators are back to the bottom floor.")
        for i in range (len(self.elevators)):
            elevator = self.elevators[i]
            start_floor = elevator.current_floor
            print(f"Recalling Elevator {i} from floor {start_floor} due to Fire Emergency")
            elevator.go_to_floor(self.bottom_floor)





