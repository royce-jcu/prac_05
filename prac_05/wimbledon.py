FILENAME = "wimbledon.csv"


def main():
    """ Get data from file """
    data = read_csv(FILENAME)
    champions, countries = process_data(data)
    display_results(champions, countries)


def read_csv(filename):
    """Read data from file and return as a list """
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(",") for line in file][1:]


def process_data(data):
    """ Create dictionary of champions and set of countries"""
    champions = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, countries


def display_results(champions, countries):
    """ Display champions and countries """
    print("Wimbledon Champions: ")
    for champion, count in champions.items():
        print(champion, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()