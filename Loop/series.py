"""Calculate series 1 + x/2 + x^2/4 + x^3/8 + x^4/16 + x^5/32 where x = 1.4
"""
from icecream import ic

sum: float = 0
term: float = 1
x: float = 1.5

for _ in range(0, 6):
    sum += term
    term *= x/2

ic(sum)