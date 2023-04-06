import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PER_LINE = 6


def main():
    """Display random numbers"""
    number_picks = int(input("How many quick picks? "))
    get_quick_picks(number_picks)


def get_quick_picks(number_picks):
    """Choose random numbers in a set."""
    for i in range(number_picks):
        quick_pick = []
        while len(quick_pick) < NUM_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()