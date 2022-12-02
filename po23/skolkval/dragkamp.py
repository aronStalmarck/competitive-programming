# Trasig kod

def rm(x, val, goal, margin):
    if goal + margin > x * val:
        goal -= x * val
        x = 0
    else:
        n = (goal - margin) // val
        goal -= n * val
        x -= n
    return int(x), goal

def full_points():
    s = [0] + [int(i) for i in input().split()]

    goal = sum([i * s[i] for i in range(5)]) / 2.0

    if s[4] >= 6 and goal > 24:
        s[4], goal = rm(s[4], 4, goal, 24)

    # reseta s[4] efter varje loop
    for i in range(0, max(1, min(int(goal / 4), s[4]))):
        s[4], goal = rm(s[4], 4, goal, 0)
        s[3], goal = rm(s[3], 3, goal, 0)
        s[2], goal = rm(s[2], 2, goal, 0)
        s[1], goal = rm(s[1], 1, goal, 0)
        if goal == 0:
            print(*s[1:])

full_points()