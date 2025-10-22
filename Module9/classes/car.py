class Car:
    def __init__(self, new_registration_number, new_maximum_speed):
        self.registration_number = new_registration_number
        self.max_speed = new_maximum_speed
        self.current_speed = 0
        self. travelled_distance = 0

    def accelerate(self, value):
        self.new_speed = self.current_speed + value
        if self.new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.new_speed


