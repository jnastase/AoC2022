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


visited = [start]
to_go = [(start, None)]
last_node = None
highest_val = 0
while to_go:
    item, *rest = to_go
    to_go = rest
    node, parent = item
    if node == end:
        last_node = item
        break
    else:
        row, col = node
        val = grid[row][col]
        if val > highest_val:
            highest_val = val
            last_node = item

    neighbors = get_possible_neighbors(grid, node)
    for n in neighbors:
        if n in visited:
            continue

        to_go.append((n, item))
        visited.append(n)


step_count = 0
last_item, parent = last_node
while parent:
    _, pre_parent = parent
    parent = pre_parent
    step_count += 1

print(step_count)
