n,m = list(map(int, input().split()))

grid = []

for i in range(n):
    row = list(input())
    grid.append(row)

directions = [(0,1), (1,0)]

checkBound = lambda row, col : (row < len(grid) and col < len(grid[0])) 

duplicatePos = set()
result = []

for i in range(len(grid)):
    for j in range(len(grid[0])):

        for direction in directions:
            current_row = i
            current_col = j

            temp = grid[current_row][current_col]

            while checkBound(current_row, current_col):
                #check if its not unique
                if (i != current_row or j != current_col) and grid[current_row][current_col] == temp:
                    duplicatePos.add((i, j))
                    duplicatePos.add((current_row, current_col))

                current_row += direction[0]
                current_col += direction[1]

 
#check if the current character is valid
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in duplicatePos:
            result.append(grid[i][j])

print(''.join(result))
