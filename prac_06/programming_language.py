class ProgrammingLanguage:
    """Representing a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage instance with the given attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns True if the programming language is dynamically typed."""
        return self.typing == "Dynamic"


