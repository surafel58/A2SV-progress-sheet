n = int(input())

graph = []
counter = 0

for i in range(n):
    row = list(map(int, input().split()))

    graph.append(row)


for i in range(n):
    counter += graph[i].count(1)

print(counter // 2)
