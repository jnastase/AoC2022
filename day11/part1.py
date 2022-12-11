f = open("input.txt", "r")
lines = f.readlines()
starting_lines = [i for i, x in enumerate(lines) if x.startswith("Monkey")]

def get_op(symbol, value):
    if symbol == "+":
        return lambda x: x + (value if value else x)
    elif symbol == "*":
        return lambda x: x * (value if value else x)

monkeys = []

for item in starting_lines:
    items = [int(x) for x in lines[item+1].split(":")[1].split(", ")]
    op_values = lines[item+2].split()
    
    op = get_op(op_values[-2], int(op_values[-1]) if op_values[-1] != "old" else None)
    test = lines[item+3].split()[-1]
    true_cond = lines[item+4].split()[-1]
    false_cond = lines[item+5].split()[-1]

    monkeys.append({
        "items": items,
        "op": op,
        "test": int(test),
        "true": int(true_cond),
        "false": int(false_cond),
        "count": 0,
    })

# print(monkeys[7]["op"](6))

round = 1
while round <= 20:
    for monkey in monkeys:
        item = monkey.get("items").pop() if monkey.get("items") else None
        while item:
            monkey["count"] += 1 
            op = monkey.get("op")
            worry = op(item)
            new_worry = worry // 3
            check = new_worry % monkey.get("test")
            if check == 0:
                monkeys[monkey.get("true")]["items"].append(new_worry)
            else:
                monkeys[monkey.get("false")]["items"].append(new_worry)

            if monkey.get("items"):
                item = monkey.get("items").pop()
            else:
                item = None
    round += 1

counts = [x["count"] for x in monkeys]
counts.sort()
# for monkey in monkeys:
#     print(monkey.get("count"))

print(counts[-1]*counts[-2])