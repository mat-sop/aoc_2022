def count_visible(grid):
    counter = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            left = row[:x]
            right = row[x + 1 :]
            up = [grid[yy][x] for yy in range(y)]
            down = [grid[yy][x] for yy in range(y + 1, len(grid))]
            if (
                val > max(left, default=-1)
                or val > max(right, default=-1)
                or val > max(up, default=-1)
                or val > max(down, default=-1)
            ):
                counter += 1
    return counter


def count_smaller(list_, v):
    counter = 0
    while counter < len(list_) and list_[counter] < v:
        counter += 1
    if counter < len(list_) and list_[counter] == v:
        return counter + 1
    return counter


def get_max_scenic_score(grid):
    scores = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            left = row[:x]
            left.reverse()
            right = row[x + 1 :]
            up = [grid[yy][x] for yy in range(y)]
            up.reverse()
            down = [grid[yy][x] for yy in range(y + 1, len(grid))]
            l_score = count_smaller(left, val)
            r_score = count_smaller(right, val)
            u_score = count_smaller(up, val)
            d_score = count_smaller(down, val)
            score = l_score * r_score * u_score * d_score
            scores.append(score)
    return max(scores)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [list(map(int, line.strip())) for line in lines]

    print(count_visible(grid))
    print(get_max_scenic_score(grid))
