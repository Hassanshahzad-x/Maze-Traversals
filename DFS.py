from game2dboard import Board


class DFS:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.node = None
        self.path = []

    def dfsAlgorithm(self,maze, node):
        if node not in self.visited:
            self.path.append(node)

            self.visited.add(node)
            for neighbour in maze[node]:
                self.dfsAlgorithm(maze, neighbour)

    def dfs(self, start, end, row, col):
        self.node = start
        self.dfsAlgorithm(self.maze, self.node)

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
            print("No path possible through DFS")

        grid.cell_size = 70
        grid.title = "DFS"
        grid.show()
