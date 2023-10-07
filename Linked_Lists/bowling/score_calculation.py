score = [[9, 1], [8, 2], [10], [5, 0], [3, 6], [4, 2], [7, 3], [6, 3], [10], [9, 1, 9]]

def calc(score):
    result, next1, next2 = 0, 0, 0
    while len(score) > 0:
        frame = score.pop(-1)
        total = sum(frame)

        if len(frame) == 3:
            result += total
            next1, next2, _ = frame
        
        elif len(frame) == 1:
            result += 10 + next1 + next2
            next1, next2 = 10, next1
        
        elif total == 10:
            result += 10 + next1
            next1, next2 = frame
        
        else:
            result += total
            next1, next2 = frame
        
    return result


class Frame:
    def __init__(self, data: list=None, next=None, prev=None):
        self.points = data if data else []
        self.length = len(self.points)
        self.next = next
        self.prev = prev


class Game:
    def __init__(self, table: list):
        self.head = None
        if table:
            self.head = Frame(table[0])
            frame = self.head
            for data in table[1:]:
                new_frame = Frame(data)
                frame.next = new_frame
                new_frame.prev = frame
                frame = new_frame


def calculate(table):
    frames = Game(table)
    frame = frames.head
    total = 0
    while frame:
        total += sum(frame.points)
        
        if frame.length == 1:
            total += sum(frame.next.points[:2])
        
        elif sum(frame.points) == 10:
            total += frame.next.points[0]
        
        frame = frame.next
    return total
            


if __name__ == "__main__":
    print(calculate(score))
    print(calc(score))