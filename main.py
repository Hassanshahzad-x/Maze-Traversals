from DFS import DFS
from BFS import BFS
from UCS import UCS
from Greedy import Greedy


def transform(maze):
    rows = len(maze)
    columns = len(maze[0])

    graph = {(i, j): [] for j in range(columns) for i in range(rows) if maze[i][j] == 0}

    for row, col in graph.keys():

        if row < rows - 1 and not maze[row + 1][col]:
            graph[(row, col)].append((row + 1, col))
            graph[(row + 1, col)].append((row, col))

        if col < columns - 1 and not maze[row][col + 1]:
            graph[(row, col)].append((row, col + 1))
            graph[(row, col + 1)].append((row, col))

    return graph


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0]]

    M = len(maze)
    N = len(maze[0])

    graph = transform(maze)

    dfs = DFS(graph)
    bfs = BFS(graph)
    ucs = UCS(graph)
    greedy = Greedy(maze, M, N)

    dfs.dfs((0, 0), (M - 1, N - 1), M, N)
    bfs.bfs((0, 0), (M - 1, N - 1), M, N)
    ucs.ucs((0, 0), (M - 1, N - 1), M, N)
    greedy.greedy((0, 0), (M - 1, N - 1), M, N)
