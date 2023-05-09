from prac_06.guitar import Guitar

guitars = []

with open("guitars.csv") as file:
    for line in file:
        name, year, price = line.strip().split(",")
        guitar = Guitar(name, int(year), float(price))
        guitars.append(guitar)

name = input("Enter name: ")
while name != "":
    year = int(input("Enter year: "))
    price = float(input("Enter price: "))
    guitar = Guitar(name, year, price)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Enter name: ")

with open("guitars.csv", "w") as file:
    for guitar in guitars:
        file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

for guitar in guitars:
    print(guitar)


def get_year(guitar):
    return guitar.year


guitars.sort(key=get_year)

print("\nSorted by year (oldest to newest):")
for guitar in guitars:
    print(guitar)
