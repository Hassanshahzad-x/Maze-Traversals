from game2dboard import Board


def isSafe(maze, x, y, row, col):
    if 0 <= x < row and 0 <= y < col and maze[x][y] == 0:
        return True
    return False


class Greedy:

    def __init__(self, maze, row, col):
        self.maze = maze
        self.path = [[0 for j in range(col)] for i in range(row)]

    def greedyAlgorithm(self, x, y, row, col):
        if x == row - 1 and y == col - 1:
            self.path[x][y] = 1
            return True

        if isSafe(self.maze, x, y, row, col):
            self.path[x][y] = 1

            if self.greedyAlgorithm(x, y + 1, row, col):
                return True

            if self.greedyAlgorithm(x + 1, y, row, col):
                return True

            self.path[x][y] = 0
            return False

    def greedy(self, start, end, row, col) -> bool:

        if not self.greedyAlgorithm(start[0], start[1], row, col):
            print("Solution doesn't exist")
            return False

        grid = Board(row, col)

        index = 1

        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if self.path[j][k] == 1:
                    grid[j][k] = index
                    index += 1

        grid[end[0]][end[1]] = index

        grid.cell_size = 70
        grid.title = "Greedy"
        grid.show()
