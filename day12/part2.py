import string
f = open("input.txt", "r")
lines = f.readlines()

asciis = string.ascii_letters
grid = []
start = None
end = None
i = 0

for line in lines:
    value = line.strip()
    grid.append([string.ascii_letters.index(x) + 1 if x not in ["S", "E"] else x for x in value])
    if "S" in value:
        start_index = value.index("S")
        start = (i, start_index)
        grid[i][start_index] = 1
    if "E" in value:
        end_index = value.index("E")
        end = (i, end_index)
        grid[i][end_index] = 26
    
    i += 1


rows = len(grid)
cols = len(grid[0])
starts = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            starts.append((i,j))


def get_possible_neighbors(grid, node):
    row, col = node
    value = grid[row][col]
    neighbors = []
    if row - 1 >= 0 and (grid[row-1][col]-value) <= 1:
        neighbors.append((row-1, col))
    if row + 1 < rows and (grid[row+1][col]-value) <= 1:
        neighbors.append((row+1, col))
    if col - 1 >= 0 and (grid[row][col-1]-value) <= 1:
        neighbors.append((row, col-1))
    if col + 1 < cols and (grid[row][col+1]-value) <= 1:
        neighbors.append((row, col+1))

    return neighbors

def search(start_coord, starts_attempted):
    visited = [start_coord]
    to_go = [(start_coord, None)]
    while to_go:
        item, *rest = to_go
        to_go = rest
        node, parent = item
        if node == end:
            return item

        neighbors = get_possible_neighbors(grid, node)
        for n in neighbors:
            if n in visited or n in starts_attempted:
                continue

            to_go.append((n, item))
            visited.append(n)

    return None
    


def get_count(path):
    step_count = 0
    last_item, parent = path
    while parent:
        _, pre_parent = parent
        parent = pre_parent
        step_count += 1

    return step_count

path_count = 0
starts_attempted = []
lowest_step_count = 1000
for start in starts:
    end_node = search(start, starts_attempted)
    starts_attempted.append(start)
    if end_node:
        step_count = get_count(end_node)
        if step_count < lowest_step_count:
            lowest_step_count = step_count

    path_count += 1


print(lowest_step_count)
