from prac_09.unreliable_car import UnreliableCar


def main():
    """Test an UnreliableCar."""

    car = UnreliableCar("Unreliable Car", 100, 50)

    # attempt to drive the car multiple times
    # output the distance driven
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{car.name:12} drove {car.drive(i):2}km")

    # print the final state of the car
    print(car)


main()