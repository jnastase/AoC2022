f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

def create_crates(input):
    defs = [x for x in input if "[" in x]
    crates = []

    for item in defs:
        line = item
        index = 0
        while len(line):
            val = line[:4]
            line = line[4:]
            crate = val[1].strip()
            
            if len(crates) <= index:
                crates.append([])

            if crate:
                crates[index].insert(0, crate)

            index += 1
    return crates

crates = create_crates(input)


for line in [x for x in input if x.startswith("move")]:
    vals = line.strip().split()
    move =int(vals[1])
    fro =int(vals[3])-1
    to =int(vals[5])-1

    items = []
    for index in range(move):
        items.append(crates[fro].pop())
    items.reverse()
    for item in items:
        crates[to].append(item)
        

print("".join([x[len(x)-1] for x in crates]))
