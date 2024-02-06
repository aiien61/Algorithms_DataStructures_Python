import numpy as np
from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class MazeNode:
    row: int = field(compare=False)
    column: int = field(compare=False)
    cost: int = None


class GreedyMazeCost:

    def __init__(self, maze: np.ndarray):
        self.maze = maze
        self.pq = PriorityQueue()
        self.maze_best_cost = np.full(maze.shape, np.nan)

    def find_min_cost(self, start_coord: tuple, target_coord: tuple) -> int:
        row, column = start_coord
        start = MazeNode(row, column)
        start.cost = self.maze[row][column]
        
        target = MazeNode(*target_coord)
        return self.walkthrough(start, target)


    def walkthrough(self, start: MazeNode, target: MazeNode) -> int:
        self.pq.put(start)

        while not self.pq.empty():
            now = self.pq.get()

            if not np.isnan(self.maze_best_cost[now.row][now.column]):
                continue

            self.maze_best_cost[now.row][now.column] = now.cost

            # explore
            if now.row - 1 >= 0:
                up = MazeNode(now.row - 1, now.column)
                up.cost = now.cost + self.maze[up.row][up.column]
                self.pq.put(up)
            
            if now.row + 1 < self.maze.shape[0]:
                down = MazeNode(now.row + 1, now.column)
                down.cost = now.cost + self.maze[down.row][down.column]
                self.pq.put(down)

            if now.column - 1 >= 0:
                left = MazeNode(now.row, now.column - 1)
                left.cost = now.cost + self.maze[left.row][left.column]
                self.pq.put(left)

            if now.column + 1 < self.maze.shape[1]:
                right = MazeNode(now.row, now.column + 1)
                right.cost = now.cost + self.maze[right.row][right.column]
                self.pq.put(right)

        return self.maze_best_cost[target.row][target.column]



if __name__ == "__main__":
    MAZE = np.array([
        [1, 3, 1, 2, 9],
        [7, 3, 4, 9, 9],
        [1, 7, 5, 5, 3],
        [2, 3, 4, 2, 5],
    ])

    gmc = GreedyMazeCost(MAZE)

    start = (0, 0)
    target = (3, 4)

    min_cost = gmc.find_min_cost(start_coord=start, target_coord=target)
    print(min_cost)
    print(gmc.maze_best_cost)

