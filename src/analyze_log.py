import csv


def readFile(path_to_file):
    with open(path_to_file) as file:
        if path_to_file.endswith(".csv"):
            the_file = csv.reader(file)
            logs = list(the_file)
            return logs
        else:
            raise FileNotFoundError

# Qual o prato mais pedido por 'maria'?


def most_requested_dish(file, name):
    food = dict()
    for client_name, food_name, _ in file:
        food[client_name] = food_name
    return food[name]

# Quantas vezes 'arnaldo' pediu 'hamburguer'?


def number_of_times_requested(file, name, dish):
    quantity = []
    for request in file:
        if request[0] == name:
            if request[1] == dish:
                quantity.append(request)
    return len(quantity)

# Quais pratos 'joao' nunca pediu?


def unordered_dishes(file, name):
    all_food = set()
    for _, food_name, _ in file:
        all_food.add(food_name)

    ordered_dishes = set()
    for order in file:
        if name in order:
            ordered_dishes.add(order[1])

    unordered_dishes = all_food - ordered_dishes
    return unordered_dishes

# Quais dias 'joao' nunca foi na lanchonete?


def days_not_frequented(file, name):
    all_days = set()
    for _, _, days in file:
        all_days.add(days)

    days_frequented = set()
    for order in file:
        if name in order:
            days_frequented.add(order[2])

    days_not_frequented = all_days - days_frequented
    return days_not_frequented


def analyze_log(path_to_file):
    file = readFile(path_to_file)
    maria = most_requested_dish(file, 'maria')
    arnaldo = number_of_times_requested(file, 'arnaldo', 'hamburguer')
    joao = unordered_dishes(file, 'joao')
    days_joao = days_not_frequented(file, 'joao')
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria}\n"
            f"{arnaldo}\n"
            f"{joao}\n"
            f"{days_joao}\n"
        )
    file.close()
