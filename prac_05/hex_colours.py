COLOUR_CODES = {"AliceBlue": "#f0f8ff", "Army Green": "4b5320", "Baby Blue": "89cff0", "Metallic Gold": "#d3af37",
                "Barn Red": "#7c0a02", "Blond": "#faf0be", "Brown": "#a52a2a", "Charcoal": "#36454f",
                "Coral Pink": "#f88379", "Earth Yellow": "#e1a95f"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")