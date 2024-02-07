from toolz import pipe


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

    def get_hours(self, departure: str, destination: str) -> int:
        hours = pipe(
            (self.get_index(departure), self.get_index(destination)),
            lambda journey: self.ROUTE_HOURS[journey]
        )
        return hours

    def get_index(self, state: str) -> int:
        return self.STATES[state]

    # enumeration -> backtracking
    def backtracking(self, hour_constraint: int) -> None:
        self.route.append(self.start)
        self.backtracking_recursion(hour_constraint)
        return None

    def backtracking_recursion(self, hour_constraint: int):
        total_hours = self.get_total_hours()
        if len(self.route) == len(self.STATES):
            if total_hours <= hour_constraint:
                print("[O]", end=" ")
            else:
                print("[X]", end=" ")

            self.print_route(total_hours)
            return None

        if total_hours > hour_constraint:
            print("[backtracked]", end=" ")
            self.print_route(total_hours)
            return None

        for next_state, index in self.STATES.items():
            if next_state in self.route:
                continue

            self.route.append(next_state)
            self.backtracking_recursion(hour_constraint)

            self.route = self.route[:-1]

        return None

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


if __name__ == "__main__":
    myplan = TravelPlan("np")
    myplan.backtracking(hour_constraint=60)
