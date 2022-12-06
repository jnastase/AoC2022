f = open("input.txt", "r")
lines = f.readline()

found = False
index = 4
while not found:
    chars = {x for x in input[index-4:index]}
    if len(chars) == 4:
        found = True
        break
    index += 1
        

print(index)
