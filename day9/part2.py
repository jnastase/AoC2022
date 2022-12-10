f = open("input.txt", "r")
lines = f.readlines()

rope_links = []
for i in range(10):
    rope_links.append((0, 0))

def print_links(rope_links):
    i = -10
    while i < 10:
        j = -10
        while j < 10:
            coords = (i,j)
            index = -1
            try:
                index = rope_links.index(coords)
            except:
                pass
            print(index if index > -1 else ".", end="")
            j += 1
        print("")
        i += 1

tail_visits = []
for line in lines:
    direction, steps = line.strip().split()
    for step in range(int(steps)):

        head, *rest = rope_links
        
        row, col = head
        if direction == "R":
            col += 1
        elif direction == "L":
            col -= 1
        elif direction == "U":
            row -= 1
        elif direction == "D":
            row += 1

        rope_links = [(row, col), *rest]

        for i in range(len(rope_links)):
            if i == 0:
                continue
            
            prev_row, prev_col = rope_links[i-1]
            curr_row, curr_col = rope_links[i]

            row_diff = abs(prev_row-curr_row)
            col_diff = abs(prev_col-curr_col)

            if row_diff <= 1 and col_diff <= 1:
                break

            move_row = False
            move_col = False
            if row_diff + col_diff >= 3:
                move_row = True
                move_col = True
            elif row_diff:
                move_row = True
            elif col_diff:
                move_col = True

            if move_row:
                if prev_row - curr_row > 0:
                    curr_row+=1
                else:
                    curr_row-=1
            if move_col:
                if prev_col - curr_col > 0:
                    curr_col+=1
                else:
                    curr_col-=1

            rope_links[i] = (curr_row, curr_col)
            # print_links(rope_links)
            # input()

        tail = rope_links[-1]

        if tail not in tail_visits:
            tail_visits.append(tail)

        # print_links(rope_links)
        # input()
        # print(rope_links)
     
print(len(tail_visits))  


