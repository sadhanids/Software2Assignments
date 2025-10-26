class Elevator:
    def __init__(self, new_number_of_bottom_floor, new_number_of_top_floor):
        self.bottom_floor = new_number_of_bottom_floor
        self.top_floor = new_number_of_top_floor
        self.current_floor = self. bottom_floor

    def go_to_floor(self, targeted_floor):
        if not (self.bottom_floor <= targeted_floor <= self.top_floor):
            print(f"Floor {targeted_floor} is invalid.")
            return
        while self.current_floor != targeted_floor:
            if targeted_floor > self.current_floor:
                self.floor_up()
            elif targeted_floor < self.current_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor == self.top_floor:
            print(f"Elevator can not move, it is already at the top floor")
        elif self.current_floor != self.top_floor:
            self.current_floor+=1
            print(f"Elevator's New Floor Number = {self.current_floor}")

    def floor_down(self):
        if self.current_floor == self.bottom_floor:
            print(f"Elevator can not move, it is already at the bottom floor")
        elif self.current_floor != self. bottom_floor:
            self.current_floor -=1
            print(f"Elevator's New Floor Number = {self.current_floor}")
