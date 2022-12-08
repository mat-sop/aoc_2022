def parse_stacks_data(stacks_data):
    stacks_lines = stacks_data.split("\n")
    indexes = {
        int(e): stacks_lines[-1].find(e) for e in stacks_lines[-1] if e and e != " "
    }
    stacks = {k: [] for k in indexes.keys()}
    for line in reversed(stacks_lines[:-1]):
        for key in stacks.keys():
            val = line[indexes[key]]
            if val and val != " ":
                stacks[key].append(val)
    return stacks


def parse_move_data(move_data):
    splitted = move_data.split(" ")
    return int(splitted[1]), int(splitted[3]), int(splitted[5])


def simulate(stacks_data, moves_data, order):
    stacks = parse_stacks_data(stacks_data)

    for move_data in moves_data.split("\n")[:-1]:
        times, from_, to = parse_move_data(move_data)
        crates = stacks[from_][-times:]
        stacks[from_] = stacks[from_][:-times]
        stacks[to].extend(crates[::order])

    left = [stacks[k].pop() for k in sorted(stacks.keys()) if stacks[k]]
    return "".join(left)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
        stacks_data, moves_data = data.split("\n\n")

    print(simulate(stacks_data, moves_data, -1))
    print(simulate(stacks_data, moves_data, 1))
