from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Representing a silver service taxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi instance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare"""
        return super().get_fare() + self.flagfall

