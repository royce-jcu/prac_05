from prac_06.guitar import Guitar


guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)
another_guitar = Guitar("Another Guitar", 2013, 500)

print(f"{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")

print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")