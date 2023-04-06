n = int(input())

graph = []
sinks = []
sources = []

for i in range(n):
    row = list(map(int, input().split()))

    graph.append(row)

isSource = False
isSink = False

for i in range(n):
    isSource = False
    isSink = False

    if 1 in graph[i]:
        isSource = True

    for j in range(n):
        if graph[j][i] == 1:
            isSink = True
            break 
    
    if not isSource and not isSink:
        sinks.append(i + 1)
        sources.append(i + 1)
    
    elif not isSource and isSink:
        sinks.append(i + 1)

    elif isSource and not isSink:
        sources.append(i + 1)


print(len(sources), *sources)
print(len(sinks), *sinks)
