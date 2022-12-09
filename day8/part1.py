f = open("input.txt", "r")
lines = f.readlines()

trees = []

for line in lines:
    val = line.strip()
    trees.append([int(x) for x in val])

rows = len(trees)
cols = len(trees[0])

visible_count = 0
visible_coords = []
for i in range(rows):
    left_max = -1
    # from left
    for col in range(cols):
        if trees[i][col] > left_max:
            left_max = trees[i][col]
            if not (i, col) in visible_coords:
                visible_coords.append((i, col))
                visible_count +=1

    right_max = -1
    right_counter = cols-1
    while right_counter > 0:
        if trees[i][right_counter] > right_max:
            right_max = trees[i][right_counter]
            if not (i, right_counter) in visible_coords:
                visible_coords.append((i, right_counter))
                visible_count +=1

        right_counter -= 1


for col in range(cols):
    top_max = -1
    # from left
    for row in range(rows):
        if trees[row][col] > top_max:
            top_max = trees[row][col]
            if not (row, col) in visible_coords:
                visible_coords.append((row, col))
                visible_count +=1

    bottom_max = -1
    bottom_counter = rows-1
    while bottom_counter > 0:
        if trees[bottom_counter][col] > bottom_max:
            bottom_max = trees[bottom_counter][col]
            if not (bottom_counter, col) in visible_coords:
                visible_coords.append((bottom_counter, col))
                visible_count +=1

        bottom_counter -= 1
    
     
print(visible_count)