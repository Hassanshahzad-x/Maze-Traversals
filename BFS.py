from game2dboard import Board


class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.node = None
        self.path = []

    def bfsAlgorithm(self, visited, maze, node):
        visited.add(node)
        queue = [node]

        while queue:
            value = queue.pop(0)
            self.path.append(value)

            for neighbour in maze[value]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def bfs(self, start, end, row, col):
        self.node = start
        self.bfsAlgorithm(self.visited, self.maze, self.node)

        grid = Board(row, col)

        index = 1
        a, b = 0, 0
        path = []

        try:
            while self.path[a] != end:
                path.append(self.path[a])
                a += 1
            path.append(end)

            for i in path:
                for j in range(len(grid)):
                    for k in range(len(grid[0])):
                        if i == (j, k):
                            grid[j][k] = index
                            index += 1
        except:
            print("No path possible through BFS")

        grid.cell_size = 70
        grid.title = "BFS"
        grid.show()
