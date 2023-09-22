from Car import Car
import readchar

if __name__ == '__main__':
    car = Car()
    left = 50
    right = 50

    while True:
        car.stop()
        key = readchar.readkey()
        if key == 'w':
            car.control_car(left, right)
        elif key == "s":
            car.control_car(-left, -right)
        elif key == "a":
            car.control_car(-left, right)
        elif key == "d":
            car.control_car(left, -right)
        elif key == "+":
            left += 25
            right += 25
        elif key == "-":
            left -= 25
            right -= 25
        elif key == "space":
            car.stop()
        elif key == "x":
            car.stop()
            break
        else:
            car.stop()