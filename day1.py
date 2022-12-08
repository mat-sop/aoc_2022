with open("input.txt") as f:
    batches = f.read().split("\n\n")[:-1]

sums = [sum(map(int, b.split("\n"))) for b in batches]
print(max(sums))
print(sum(sorted(sums)[-3:]))
