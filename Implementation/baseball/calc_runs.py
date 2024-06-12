from functools import lru_cache


def search(inning: int, runs: int):
    if inning == 1:
        return 1
    
    result = 0
    for i in range(runs + 1):
        result += search(inning - 1, runs - i)
    
    return result


@lru_cache(maxsize=100000)
def calc(away_runs, home_runs):
    away_pattern = search(9, away_runs)

    if away_runs > home_runs:
        home_pattern = search(9, home_runs)
    else:
        home_pattern = search(8, home_runs)
        for i in range(away_runs + 1):
            home_pattern += search(8, i)

    return away_pattern * home_pattern


if __name__ == '__main__':
    print(calc(7, 8))