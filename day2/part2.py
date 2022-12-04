f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

my_score = 0
for line in input:
    vals = line.strip().split()
    opp = vals[0]
    me = vals[1]
    if opp == "A":
        if me == "X":
            my_score += 3
        elif me == "Y":
            my_score += 4
        if me == "Z":
            my_score += 8
    elif opp == "B":
        if me == "X":
            my_score += 1
        elif me == "Y":
            my_score += 5
        if me == "Z":
            my_score += 9
    elif opp == "C":
        if me == "X":
            my_score += 2
        elif me == "Y":
            my_score += 6
        if me == "Z":
            my_score += 7


print(my_score)
