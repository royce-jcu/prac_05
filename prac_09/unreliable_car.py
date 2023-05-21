from random import randint
from prac_06.car import Car


class UnreliableCar(Car):
    """Representing an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car a given distance, based on the car's reliability."""
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0

        return distance_driven
