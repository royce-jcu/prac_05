import datetime


class Project:
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.completion = int(completion)

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.completion}"

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost}, {self.completion}"

    def is_complete(self):
        return int(self.completion) == 100

    def __lt__(self,other):
        return self.priority <= other.priority

    def compare_date(self, input_date):
        input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
        return self.start_date >= input_date

    def update_percentage(self, value):
        self.completion = value

    def update_priority(self, value):
        self.priority = value