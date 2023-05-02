class Guitar:
    """Representing a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Construct a new guitar object with the given name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns the age of the guitar."""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if a Guitar is 50 years old or more than that."""
        return self.get_age() >= 50

