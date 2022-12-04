f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

total = 0
for line in input:
    vals = line.strip().split(",")
    first_start, first_end = [int(x) for x in vals[0].split("-")]
    second_start, second_end = [int(x) for x in vals[1].split("-")]
    

    if (first_start >= second_start and first_start <= second_end) or (first_end >= second_start and first_end <= second_end):
        total += 1
    elif (second_start >= first_start and second_start <= first_end) or (second_end >= first_start and second_end <= first_end):
        total += 1
        


print(total)
