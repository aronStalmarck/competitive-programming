# group 3: 10
# group 4: 10
# group 5: 9.5
# group 6: 9.75
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

def get_closest(cur, points, sample_size):
    closest = -1
    d = float("inf")
    sample = []
    for _ in range(min(sample_size, len(points.dict))):
        sample.append(points.popRandom())
    for p in sample:
        if distance(cur, p) < d:
            closest = p
            d = distance(cur, p)
    for p in sample:
        if p.id != closest.id:
            points.add(p)
    return closest

T, N = int(input()), int(input())
num_tries = {
    0: 10,
    1: 1,
    2: 1,
    3: 10,
    4: 40,
    5: 50,
    6: 10,
    7: 10,
    8: 2,
    9: 1,
    10: 1
}

sample_size = {
    0: 100,
    1: 100,
    2: 100,
    3: 1000,
    4: 1000,
    5: 1000,
    6: 1000,
    7: 1000,
    8: 1000,
    9: 100,
    10: 100
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
        to = get_closest(cur, points, sample_size[T])
        points.delete(to)
                
        p_len += distance(cur, to)
        cur = to
        path.append(cur)
    
    if p_len < min_path_len:
        best_out = path
        min_path_len = p_len

print(" ".join([str(p.id) for p in best_out]))