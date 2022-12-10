f = open("input.txt", "r")
lines = f.readlines()

cycle_count = 0
X = 1
pixels = []
for line in lines:
    line_val = line.strip()

    cycle_count += 1
    if X <= cycle_count % 40 <= X + 2:
        pixels.append("#")
    else:
        pixels.append(".")
    if line_val.startswith("noop"):
        pass
    else:
        _, value = line_val.split()
        cycle_count += 1
        if X <= cycle_count % 40 <= X + 2:
            pixels.append("#")
        else:
            pixels.append(".")

        X += int(value)

p = 0
while p < 240:
    print("".join(pixels[p:p+40]))
    p +=40