from collections import defaultdict


def dfs(node):

    for neighbour in graph[node]:
        
        if neighbour not in color:
            color[neighbour] = 1 - color[node]
            traverse = dfs(neighbour)

            if not traverse:
                return False
        
        elif color[node] == color[neighbour]:
            return False
    
    return True


while True: 
    n = int(input())

    #break 
    if n == 0:
        break

    n_edges = int(input())
    edges = []
    
    graph = defaultdict(list)

    for _ in range(n_edges):
        edge = list(map(int, input().split()))
        
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


    color = dict()
    ans = 'BICOLOURABLE.'

    for node in graph:
        if node not in color:
            
            color[node] = 0
            result = dfs(node)
            
            if not result:
                ans = 'NOT BICOLOURABLE.'
                break
    print(ans)
