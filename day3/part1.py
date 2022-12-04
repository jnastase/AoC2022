import string

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

my_score = 0
for line in input:
    val = line.strip()
    first = {x for x in val[:len(val)//2]}
    second = {x for x in val[len(val)//2:]}
    
    same = {a for a in first if a in second}
    my_score += sum([string.ascii_letters.index(x) + 1 for x in same])


print(my_score)
