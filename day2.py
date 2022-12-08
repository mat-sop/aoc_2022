ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

matrix = {
    "A": {
        "X": ROCK + DRAW,
        "Y": PAPER + WIN,
        "Z": SCISSORS + LOSE,
    },
    "B": {
        "X": ROCK + LOSE,
        "Y": PAPER + DRAW,
        "Z": SCISSORS + WIN,
    },
    "C": {
        "X": ROCK + WIN,
        "Y": PAPER + LOSE,
        "Z": SCISSORS + DRAW,
    },
}

matrix2 = {
    "A": {
        "X": LOSE + SCISSORS,
        "Y": DRAW + ROCK,
        "Z": WIN + PAPER,
    },
    "B": {
        "X": LOSE + ROCK,
        "Y": DRAW + PAPER,
        "Z": WIN + SCISSORS,
    },
    "C": {
        "X": LOSE + PAPER,
        "Y": DRAW + SCISSORS,
        "Z": WIN + ROCK,
    },
}


def calculate_points(pairs, matrix):
    points = 0
    for pair in pairs:
        if pair:
            opponent, me = pair.split(" ")
            points += matrix[opponent][me]
    return points


if __name__ == "__main__":
    with open("input.txt") as f:
        pairs = f.read().split("\n")
        
    print(calculate_points(pairs, matrix))
    print(calculate_points(pairs, matrix2))
