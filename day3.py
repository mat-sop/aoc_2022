def duplicated(backpack):
    half = len(backpack) // 2
    return set(backpack[:half]).intersection(set(backpack[half:])).pop()

def priority(s):
    return ord(s) - (96 if s.islower() else 38)


def badge(group):
    return set.intersection(*list(map(set, group))).pop()


if __name__ == "__main__":
    with open("input.txt") as f:
        backpacks = f.read().split("\n")[:-1]

    sum_ = sum([priority(duplicated(b)) for b in backpacks])
    print(sum_)

    groups = [backpacks[x : x + 3] for x in range(0, len(backpacks), 3)]
    sum_2 = sum([priority(badge(g)) for g in groups])
    print(sum_2)
