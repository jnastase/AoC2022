f = open("input.txt", "r")
lines = f.readlines()

# input = [x for x in lines]


root = {
    "dirs": {},
    "files": [],
    "parent": None
}
current_dir = root
root_size = 0
is_in_list = False
for line in lines:
    val = line.strip()
    values = val.split()
    if values[0] == "$" and values[1] == "ls":
        is_in_list = True
        continue
    elif values[0] == "$" and values[1] == "cd":
        is_in_list = False
        
        if values[2] == "..":
            current_dir = current_dir["parent"]
        elif values[2] == "/":
            continue
        else:
            new_dir = {
                "dirs": {},
                "files": [],
                "parent": current_dir,
            }
            current_dir["dirs"][values[2]] = new_dir 
            current_dir = new_dir

    if is_in_list:
        if values[0] == "dir":
            current_dir["dirs"][values[1]] = {
                "dirs": {},
                "files": [],
                "parent": current_dir,
            }
        else:
            root_size += int(values[0])
            current_dir["files"].append({"size": int(values[0]), "name": values[1]}) 
    
while current_dir["parent"]:
    current_dir = current_dir["parent"]

less_than_vals = []
dirs_to_delete_sizes = []
def get_dir_size(item):
    file_size = 0
    if item.get("files", []):
        file_size = sum([x["size"] for x in item["files"]])

    dir_size = 0
    
    if item.get("dirs", {}):
        for item2 in item["dirs"].values():
            dir_size += get_dir_size(item2)
        

    total = dir_size + file_size
    if 70000000 - root_size + total > 30000000:
        dirs_to_delete_sizes.append(total)
    return total

for item in current_dir["dirs"].values():
    size = get_dir_size(item)

print(min(dirs_to_delete_sizes))

# 2709965