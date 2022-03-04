import csv
from pubsub import pub
from inventory_control import InventoryControl
from track_orders import TrackOrders


def print_info(tracker, control):
    print(tracker.get_most_ordered_dish_per_costumer('maria'))
    print(tracker.get_order_frequency_per_costumer('arnaldo', 'hamburguer'))
    print(tracker.get_never_ordered_per_costumer('joao'))
    print(tracker.get_days_never_visited_per_costumer('joao'))
    print(control.get_quantities_to_buy())


def main():
    topic = 'order'
    path = ""

    tracker = TrackOrders()
    control = InventoryControl()
    subs = [tracker.add_new_order, control.add_new_order]

    for sub in subs:
        pub.subscribe(sub, topic)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for costumer, order, day in csv_reader:
            pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control)


if __name__ == "__main__":
    main()
