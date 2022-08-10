from game2dboard import Board


class UCS:
    def __init__(self, maze):
        self.path = []
        self.maze = maze

    def ucsAlgorithm(self, start, end, way):
        way = way + [start]
        if start == end:
            return way
        shortest = None
        for node in self.maze[start]:
            if node not in way:
                new_path = self.ucsAlgorithm(node, end, way)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

    def ucs(self, start, end,row,col):
        way = []
        self.path = self.ucsAlgorithm(start, end, way)
        grid = Board(row, col)

        index = 1

        try:
            for i in self.path:
                for j in range(len(grid)):
                    for k in range(len(grid[0])):
                        if i == (j, k):
                            grid[j][k] = index
                            index += 1
        except:
            print("No path possible through UCS")

        grid.cell_size = 70
        grid.title = "UCS"
        grid.show()
