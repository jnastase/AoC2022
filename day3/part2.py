import string

f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

my_score = 0
index = 0
while index < len(input):
    first = {x for x in input[index].strip()}
    second = {x for x in input[index+1].strip()}
    third = {x for x in input[index+2].strip()}


    index += 3
    
    same = {a for a in first if a in second and a in third}
    my_score += sum([string.ascii_letters.index(x) + 1 for x in same])


print(my_score)
