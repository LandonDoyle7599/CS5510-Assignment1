from Car import Car
import time

if __name__ == '__main__':
    car = Car()
    left = 50
    right = 50
    for x in range(4):
        car.control_car(left, right)
        time.sleep(2)
        car.control_car(0, 0)
        time.sleep(.1)
        car.control_car(3*left, -3*right)
        time.sleep(.8)
        car.control_car(0, 0)
        time.sleep(.1)
    car.control_car(0, 0)


