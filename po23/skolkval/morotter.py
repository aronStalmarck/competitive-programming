class Person:
    def __init__(self, t) -> None:
        self.t = t
        self.until_next = 0
        self.num_carrots = 0

Tor = Person(int(input()))
Mom = Person(int(input()))

N = 40
while N > 0:
    if N == 1 and Tor.until_next == Mom.until_next == 0:
        break
    if Tor.until_next == 0:
        N -= 1
        Tor.num_carrots += 1
        Tor.until_next = Tor.t
    if Mom.until_next == 0:
        N -= 1
        Mom.num_carrots += 1
        Mom.until_next = Mom.t
    Tor.until_next -= 1
    Mom.until_next -= 1

print(f"Tor: {Tor.num_carrots}, Mor: {Mom.num_carrots}")