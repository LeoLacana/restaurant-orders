from src.analyze_log import (
    most_requested_dish,
    unordered_dishes,
    days_not_frequented,
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_requested_dish(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return unordered_dishes(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return days_not_frequented(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
