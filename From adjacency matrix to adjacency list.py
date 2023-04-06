n = int(input())

graph = []

for i in range(n):
    row = list(map(int, input().split()))

    graph.append(row)


for i in range(n):
    temp = []
    for j in range(n):
        if graph[i][j] == 1:
            temp.append(j + 1)
    
    print(len(temp), *temp)
