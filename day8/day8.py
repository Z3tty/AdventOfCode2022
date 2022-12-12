grid: list = []
length: int = 0
height: int = 0

def process() -> None:
    global length, height
    line_length: int = 0
    line_height: int = 0
    with open("day8_input.txt", "r+") as tree_grid:
        line: str = tree_grid.readline().rstrip()
        line_length = len(line) - 1
        while True:
            if not line:
                break
            split: list = list(line)
            grid.append(split)
            line_height += 1
            line = tree_grid.readline().rstrip()
    length = line_length
    height = line_height
    for GL in grid:
        for C in GL:
            C = int(C)

def visible_trees(G: list) -> int:
    global length, height
    total_visible: int = length * 2 + height * 2 - 2
    t_left: int = 0
    t_right: int = 0
    t_up: int = 0
    t_down: int = 0
    for i in range(1, height):
        for j in range(1, length):
            tree: int = G[i][j]
            for k in range(i):
                if G[k][j] > tree:
                    t_left += 1
                    break
            for v in range(i, length):
                if G[v][j] > tree:
                    t_right += 1
                    break
            for x in range(j):
                if G[i][x] > tree:
                    t_up += 1
                    break
            for y in range(j, height):
                if G[i][y] > tree:
                    t_down += 1
                    break
            if t_left == 0 or t_right == 0 or t_up == 0 or t_down == 0:
                total_visible += 1
    return total_visible

if __name__ == '__main__':
    process()
    t: int = visible_trees(grid)
    print(t)
