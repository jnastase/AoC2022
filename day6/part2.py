f = open("input.txt", "r")
lines = f.readline()

input = [x for x in lines]

found = False
index = 14
while not found:
    chars = {x for x in input[index-14:index]}
    if len(chars) == 14:
        found = True
        break
    index += 1
        

print(index)
