f = open("input.txt", "r")
lines = f.readlines()

trees = []

for line in lines:
    val = line.strip()
    trees.append([int(x) for x in val])

rows = len(trees)
cols = len(trees[0])

max_sight = 0
for row in range(rows):
    for col in range(cols):
        left_col = col -1
        left_val = 1
        while left_col > 0:
            if trees[row][left_col] < trees[row][col]:
                left_val += 1
            else:
                left_col = 0
                break
            left_col -= 1

        right_col = col + 1
        right_val = 1
        while right_col < cols-1:
            if trees[row][right_col] < trees[row][col]:
                right_val += 1
            else:
                right_col = cols
                break
            right_col += 1

        top_row = row - 1
        top_val = 1
        while top_row > 0:
            if trees[top_row][col] < trees[row][col]:
                top_val += 1
            else:
                top_row = 0
                break
            top_row -= 1

        bottom_row = row + 1
        bottom_val = 1
        while bottom_row < rows-1:
            if trees[bottom_row][col] < trees[row][col]:
                bottom_val += 1
            else:
                bottom_row = rows
                break
            bottom_row += 1

        product = left_val * right_val * bottom_val * top_val
        print(f"({row}, {col}): {product}")
        
        if product > max_sight:
            # print(left_val)
            # print(right_val)
            # print(top_val)
            # print(bottom_val)
            # print((row, col))
            max_sight = product
    
     
print(max_sight)