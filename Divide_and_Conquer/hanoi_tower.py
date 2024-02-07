import os, sys
sys.path.append(os.pardir)

from Stack.Array.pystack import PyStack

class Hanoi:
    def __init__(self, number_of_plates: int):
        self.pillar_a = PyStack(number_of_plates, list(range(number_of_plates, 0, -1)))
        self.pillar_b = PyStack(number_of_plates)
        self.pillar_c = PyStack(number_of_plates)

    def __repr__(self):
        overview = "Pillar A: {a}\nPillar B: {b}\nPillar C: {c}"
        return overview.format(a=self.pillar_a, b=self.pillar_b, c=self.pillar_c)
    
    def main(self) -> None:
        self.move(self.pillar_a.size, self.pillar_a, self.pillar_b, self.pillar_c)
        print(self)
        return None

    def move(self, layer: int, p_from: PyStack, p_mid: PyStack, p_to: PyStack) -> None:
        if layer == 0:
            return None

        # upper layer from a to b
        self.move(layer-1, p_from, p_to, p_mid)

        # target layer from a to c
        target_layer = p_from.pop()
        p_to.push(target_layer)
        
        # upper layer from b to c        
        self.move(layer-1, p_mid, p_from, p_to)

        return None        
        

if __name__ == "__main__":
    hanoi = Hanoi(5)
    print(hanoi)
    print("--- after movement ---")
    hanoi.main()