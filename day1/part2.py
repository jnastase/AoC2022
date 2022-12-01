f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

last_number = None
increases = 0
elfs = []
curr_val = 0
for reading in input:
    val = reading.strip()
    if not val:
        elfs.append(curr_val)
        curr_val = 0
        continue

    
    curr_val += int(val)

elfs.sort(reverse=True)
print(sum(elfs[:3]))
