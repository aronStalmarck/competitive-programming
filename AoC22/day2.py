import sys

outcome = {"X": 0, "Y": 3, "Z": 6}
scor = {"A X": 3, "B X": 1, "C X": 2,
        "A Y": 1, "B Y": 2, "C Y": 3,
        "A Z": 2, "B Z": 3, "C Z": 1}

total = 0
while True:
    input_ = sys.stdin.readline()[:3]
    if input_ == '\n':
        break
    total += outcome[input_[2]]
    total += scor[input_[:3]]

print(total)