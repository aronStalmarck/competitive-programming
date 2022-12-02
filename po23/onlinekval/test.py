import random

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

from random import randint

s = randomSet()
for el in [randint(1, 100) for _ in range(1000_000)]:
    s.add(el)

print(s.getRandom())


#print("A random number from the set is: " , random.sample(set, 1))