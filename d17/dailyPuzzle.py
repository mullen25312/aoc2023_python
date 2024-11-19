from dxx.superDailyPuzzle import SuperDailyPuzzle

# import dijkstra
from dijkstra import AbstractDijkstraSPF, Graph

class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        (n, m) = (len(grid), len(grid[0]))
        ((y,x), (y_cnt, x_cnt)) = u

        # adjacent = []
        # if (0 < y) and (-3 < y_cnt <= 0): adjacent.append(((y-1,x), (y_cnt -1, 0)))
        # if (y < n-1) and (0 <= y_cnt < 3): adjacent.append(((y+1,x), (y_cnt +1, 0)))
        # if (0 < x) and (-3 < x_cnt <= 0): adjacent.append(((y,x-1), (0, x_cnt-1)))
        # if (x < m-1) and (0 <= x_cnt < 3): adjacent.append(((y,x+1), (0, x_cnt+1)))

        adjacent = []
        if (0 < y) and (-4 < y_cnt <= -1): 
            adjacent.append(((y-1,x), (y_cnt-1, 0)))
            return adjacent
        if (y < n-1) and (1 <= y_cnt < 4): 
            adjacent.append(((y+1,x), (y_cnt+1, 0)))
            return adjacent
        if (0 < x) and (-4 < x_cnt <= -1): 
            adjacent.append(((y,x-1), (0, x_cnt-1)))
            return adjacent
        if (x < m-1) and (1 <= x_cnt < 4): 
            adjacent.append(((y,x+1), (0, x_cnt+1)))
            return adjacent
        if (0 < y) and ((-10 < y_cnt <= -4)): adjacent.append(((y-1,x), (y_cnt -1, 0)))
        if (y < n-1) and ((4 <= y_cnt < 10)): adjacent.append(((y+1,x), (y_cnt +1, 0)))
        if (0 < x) and ((-10 < x_cnt <= -4)): adjacent.append(((y,x-1), (0, x_cnt-1)))
        if (x < m-1) and ((4 <= x_cnt < 10)): adjacent.append(((y,x+1), (0, x_cnt+1)))

        if (3 < y) and (y_cnt == 0): adjacent.append(((y-1,x), (y_cnt -1, 0)))
        if (y < n-1-3) and (y_cnt == 0): adjacent.append(((y+1,x), (y_cnt +1, 0)))
        if (3 < x) and (x_cnt == 0): adjacent.append(((y,x-1), (0, x_cnt-1)))
        if (x < m-1-3) and (x_cnt == 0): adjacent.append(((y,x+1), (0, x_cnt+1)))

        return adjacent
    
    @staticmethod
    def get_edge_weight(G, u, v):
        grid = G
        return grid[v[0][0]][v[0][1]]

# advent of code 2023 day 0 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        grid = []
        for line in self.data.splitlines():
            grid.append([int(x) for x in list(line)])
        
        self.parsed = grid

    def part_one(self, **kwargs):
        grid = self.parsed

        (n, m) = (len(grid), len(grid[0]))
        S = ((0,0), (0,0))

        dijkstra = DijkstraSPF(grid, S)
        results = []
        for k, v in dijkstra.get_distances().items():
            if k[0] == (n-1, m-1): results.append((k,v))
        results.sort(key=lambda result: result[1])
        # print(results)

        # print(" -> \n".join([str(x) for x in dijkstra.get_path(results[0][0])]))
        self.part_one_result = results[0][1]

    def part_two(self, **kwargs):
        self.part_two_result = 0
