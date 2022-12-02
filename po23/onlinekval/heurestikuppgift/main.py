from sys import setrecursionlimit

from random import randint

setrecursionlimit(100000000)


class randomSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def add(self, item):
        if item not in self.dict:
            self.dict[item] = len(self.list)
            self.list.append(item)

    def addIterable(self, item):
        for a in item:
            self.add(a)

    def delete(self, item):
        if item in self.dict:
            index = self.dict[item]
            if index == len(self.list)-1:
                del self.dict[self.list[index]]
                del self.list[index]
            else:
                self.list[index] = self.list.pop()
                self.dict[self.list[index]] = index
                del self.dict[item]

    def getRandom(self):
        if self.list:
            return self.list[randint(0,len(self.list)-1)]

    def popRandom(self):
        if self.list:
            index = randint(0,len(self.list)-1)
            if index == len(self.list)-1:
                del self.dict[self.list[index]]
                return self.list.pop()
            returnValue = self.list[index]
            self.list[index] = self.list.pop()
            self.dict[self.list[index]] = index
            del self.dict[returnValue]
            return returnValue

class Point:
    def __init__(self, params, id):
        self.x, self.y = params[0], params[1]
        self.id = id

    def __repr__(self) -> str:
        return f"p{self.id}: ({self.x}, {self.y})"

def distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def get_closest(cur, points):
    closest = -1
    d = float("inf")
    for p in points.list:
        if distance(cur, p) < d:
            closest = p
            d = distance(cur, p)
    return closest

T, N = int(input()), int(input())

if T in (1, 2):
    points = [Point([int(i) for i in input().split()], idx + 1) for idx in range(N)]

    y_max, y_min = max([p.y for p in points]), min([p.y for p in points])
    y_mid = (y_max + y_min) / 2
    y_delta = y_max - y_mid
    y_mean = sum((p.y for p in points)) / N
    y_median = sorted([p.y for p in points])[int(N/2)]

    points_mid = [p for p in points if abs(p.y - (y_mean)) < (y_max - y_min) / 3.7]


    if len(points_mid) >= N/2:
        points_mid.sort(key=lambda p: (p.x, p.y))
        print(*[p.id for p in points_mid[:int(N/2)]])

    else:
        points.sort(key=lambda p: (p.x, p.y))
        print(*[p.id for p in points[:int(N/2)]])
    exit(0)

num_tries = {
    0: 10,
    1: 1,
    2: 1,
    3: 10,
    4: 40,
    5: 50,
    6: 10,
    7: 1,
    8: 1,
    9: 1,
    10: 1
}



points_save = [Point([int(i) for i in input().split()], idx + 1) for idx in range(N)]

best_out = []
min_path_len = float("inf")


for try_num in range(min(num_tries[T], N)):
    # init points
    points = randomSet()
    for el in points_save:
        points.add(el)

    start = points.popRandom()
    
    # 
    cur = start
    p_len = 0
    path = [cur]
    
    for i in range(int(N/2) - 1):
        to = get_closest(cur, points)
        points.delete(to)
                
        p_len += distance(cur, to)
        cur = to
        path.append(cur)
    
    if p_len < min_path_len:
        best_out = path
        min_path_len = p_len

print(" ".join([str(p.id) for p in best_out]))
