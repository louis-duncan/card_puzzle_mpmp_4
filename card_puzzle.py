import os
import time

os.system("title Parker's Puzzle")


def process_combinations(combs):
    printed = 0
    left_most = len(combs[0]) - 1
    counts = [0 for i in range(len(combs[0]))]
    for c in combs:
        if not "0" in c:
            print(" ".join(c.replace("0", "□").replace("1", "■")), "√")
        else:
            printed += 1
            for i, d in enumerate(c):
                if d == "0":
                    counts[i] += 1
            print(" ".join(c.replace("0", "□").replace("1", "■")))
            if c.count("0") == 1:
                pos = c.find("0")
                if pos < left_most:
                    left_most = pos
    if printed == 0:
        print("Done!")
        left_most = None
    else:
        print("Suggest:", left_most + 1)
    return left_most


def add_move(move, moves, combinations):
    for c in range(len(combinations)):
        if not "0" in combinations[c]:
            pass
        else:
            combinations[c] = flip(move-1, combinations[c])
    moves += str(move)
    return moves


def flip(n, string):
    if string[n] == "0":
        return replace("1", n, string)
    else:
        return replace("0", n, string)


def replace(c, n, string):
    return string[:n] + c + string[n+1:]


while True:
    os.system("cls")
    n = int(input("Enter n: "))
    combinations = [str(bin(i).split("b")[1].zfill(n)) for i in range((2**n)-1)]
    moves = ""

    while True:
        os.system("cls")
        print("Moves:", moves)
        action = process_combinations(combinations)
        if action is None:
            break
        else:
            time.sleep(0.5)
            moves = add_move(action + 1, moves, combinations)
    input()
