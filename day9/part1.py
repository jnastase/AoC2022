f = open("input.txt", "r")
lines = f.readlines()


head = (0, 0)
tail = (0, 0)
tail_visits = []
for line in lines:
    direction, steps = line.strip().split()
    for i in range(int(steps)):
        prev_loc = head
        row, col = head
        if direction == "R":
            col += 1
        elif direction == "L":
            col -= 1
        elif direction == "U":
            row -= 1
        elif direction == "D":
            row += 1

        head = (row, col)

        tail_row, tail_col = tail

        row_diff = abs(row-tail_row)
        col_diff = abs(col-tail_col)

        if row_diff <= 1 and col_diff <= 1:
            if tail not in tail_visits:
                tail_visits.append((tail_row, tail_col))

            continue

        tail = prev_loc
        if tail not in tail_visits:
            tail_visits.append(tail)
    
    
     
print(len(tail_visits))