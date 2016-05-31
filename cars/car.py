#creating a class exercise


class Car:

    number_of_wheels = 4

    def __init__(self, number_of_doors=3, color='grey', car_sound='honk'):
        self.number_of_doors = number_of_doors
        self.color = color
        self.car_sound = car_sound

    def honk(self):
        if self.car_sound is 'honk':
            print("honk")
        else:
            print(self.car_sound)
