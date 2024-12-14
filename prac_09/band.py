class Band:
    """Band class with a list of musicians."""

    def __init__(self, name):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musician_list = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_list})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        play = [f"{musician.play()}" for musician in self.musicians]
        return "\n".join(play)
