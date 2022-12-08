from collections import defaultdict

input_lines = open("input.txt").read().split("\n")[:-1]

sizes = defaultdict(lambda: 0)
current_path = []

for line in input_lines:
    if line.startswith("$ cd"):
        arg = line[5:]
        if arg == "/":
            current_path = ["/"]
        elif arg == "..":
            current_path.pop()
        else:
            current_path.append(arg)
    elif not (line.startswith("$") or line.startswith("dir")):
        size, name = line.split(" ")
        for i, d in enumerate(current_path):
            p = "".join(current_path[: i + 1])
            sizes[p] += int(size)

part1 = sum([v for v in sizes.values() if v <= 100000])
print(part1)

missing_space = 30000000 - (70000000 - sizes["/"])
part2 = min([v for v in sizes.values() if v >= missing_space])
print(part2)
