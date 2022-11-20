class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('car is starting..')

car=Car('baoma X5')
car.start()
print(car.brand)