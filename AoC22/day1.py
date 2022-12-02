import heapq
hi = -1
A = []
i = 0
while True:
    x = 0
    while True:

        s = input()

        if not s:
            break
        
        x += int(s)
    heapq.heappush(A, -x)
    if len(A) > 2:
        a, b, c = [-heapq.heappop(A) for _ in range(3)]
        heapq.heappush(A, -a)
        heapq.heappush(A, -b)
        heapq.heappush(A, -c)

        i += 1
        #if i > 400:
        #   break
        

        hi = max(a + b + c, hi)
        print("hi: ", hi)