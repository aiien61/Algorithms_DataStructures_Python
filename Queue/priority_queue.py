import random
from attr import define, attrib
from dataclasses import dataclass, field
from queue import PriorityQueue


@dataclass(order=True)
class Client:
    name: str = field(compare=False)
    rank: int


@define(order=True)
class Customer:
    name: str = attrib(eq=False)
    rank: int


class Person:
    def __init__(self, name: str, rank: int):
        self.name = name
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank
    
    def __repr__(self):
        return f"Person({self.name}, {self.rank})"


if __name__ == "__main__":
    names = ["Harry", "Charles", "Charlotte", "Stacy"]
    ranks = random.sample(range(10), len(names))

    # ------------------------------
    clients = [Client(name, rank) for name, rank in zip(names, ranks)]
    print(clients)
    
    clients_queue = PriorityQueue()
    print(clients_queue.empty())

    for client in clients:
        clients_queue.put(client)

    while not clients_queue.empty():
        print(clients_queue.get())

    print("------------------------------")

    customers = [Customer(name, rank) for name, rank in zip(names, ranks)]
    print(customers)

    customers_queue = PriorityQueue()
    print(customers_queue.empty())

    for customer in customers:
        customers_queue.put(customer)
    
    while not customers_queue.empty():
        print(customers_queue.get())

    print("------------------------------")

    persons = [Person(name, rank) for name, rank in zip(names, ranks)]
    print(persons)

    persons_queue = PriorityQueue()
    print(persons_queue.empty())

    for person in persons:
        persons_queue.put(person)

    while not persons_queue.empty():
        print(persons_queue.get())

    print("------------------------------")

    guests = {name: rank for name, rank in zip(names, ranks)}
    print(guests)

    guests_queue = PriorityQueue()
    print(guests_queue.empty())

    for name, rank in guests.items():
        guests_queue.put((rank, name))

    while not guests_queue.empty():
        print(guests_queue.get())


