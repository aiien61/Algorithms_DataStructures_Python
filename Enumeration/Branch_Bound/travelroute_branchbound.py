from toolz import pipe
from queue import PriorityQueue
from dataclasses import dataclass, field

@dataclass(order=True)
class Country:
    name: str = field(compare=False)
    hour_to_take: int


class TravelPlan:

    STATES = {
        "NP": 0, "IS": 1, "CA": 2, "UK": 3, "US": 4
    }

    ROUTE_HOURS = {
        (0, 0): 0,
        (0, 1): 14,
        (0, 2): 15,
        (0, 3): 17,
        (0, 4): 16,

        (1, 0): 14,
        (1, 1): 0,
        (1, 2): 24,
        (1, 3): 8,
        (1, 4): 36,

        (2, 0): 15,
        (2, 1): 24,
        (2, 2): 0,
        (2, 3): 34,
        (2, 4): 4,

        (3, 0): 17,
        (3, 1): 8,
        (3, 2): 34,
        (3, 3): 0,
        (3, 4): 30,

        (4, 0): 16,
        (4, 1): 36,
        (4, 2): 4,
        (4, 3): 30,
        (4, 4): 0
    }

    def __init__(self, departure: str):
        self.start = departure.upper()
        self.route = []
        self.hour_best = None

    def get_hours(self, departure: str, destination: str) -> int:
        hours = pipe(
            (self.get_index(departure), self.get_index(destination)),
            lambda journey: self.ROUTE_HOURS[journey]
        )
        return hours

    def get_index(self, state: str) -> int:
        return self.STATES[state]

    def get_total_hours(self) -> int:
        if not self.route:
            return 0

        start = self.route[0]
        hours = 0
        for end in self.route[1:]:
            hours += self.get_hours(start, end)
            start = end
        return hours

    def print_route(self, total_hours) -> None:
        print(f"{'->'.join(self.route)}: {total_hours}")

    # enumeration -> backtracking -> branch & bound
    def branchbound(self) -> None:
        self.route.append(self.start)
        self.branchbound_recursion()
        return None

    def branchbound_recursion(self, ):
        total_hours = self.get_total_hours()

        if len(self.route) == len(self.STATES):
            if (self.hour_best is None) or (total_hours < self.hour_best):
                self.hour_best = total_hours
            else:
                print("[X]", end=" ")

            self.print_route(total_hours)
            return None
        
        if self.hour_best is not None:
            if total_hours >= self.hour_best:
                print("[bounded]", end=" ")
                self.print_route(total_hours)
                return None

        pq = PriorityQueue()
        current_country = self.route[-1]
        for next_country in self.STATES:
            if next_country in self.route:
                continue
            pq.put(Country(next_country, self.get_hours(current_country, next_country)))

        while not pq.empty():
            next_country_object = pq.get()
            self.route.append(next_country_object.name)
            self.branchbound_recursion()
            self.route = self.route[:-1]

        return None


if __name__ == "__main__":
    myplan = TravelPlan("np")
    myplan.branchbound()
