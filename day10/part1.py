f = open("input.txt", "r")
lines = f.readlines()

cycle_count = 0
X = 1
notable_cycles = [20, 60, 100, 140, 180, 220]
cycle_products = []
for line in lines:
    line_val = line.strip()

    cycle_count += 1
    if cycle_count in notable_cycles:
        cycle_products.append(X * cycle_count)
    if line_val.startswith("noop"):
        pass
    else:
        _, value = line_val.split()
        cycle_count += 1
        if cycle_count in notable_cycles:
            cycle_products.append(X * cycle_count)

        X += int(value)

print(sum(cycle_products))