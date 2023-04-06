from collections import defaultdict 

n = int(input())

k = int(input())

adjList = defaultdict(list)

for i in range(k):
    operation = list(map(int, input().split()))

    if operation[0] == 1:
        adjList[operation[1]].append(operation[2])
        adjList[operation[2]].append(operation[1])

    else:
        adjacents = adjList[operation[1]]
        print(*adjacents)
