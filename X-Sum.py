test_case = int(input())

for _ in range(test_case):
   n,m = list(map(int, input().split()))
   nums = []

   for _ in range(n):
      rowInput = list(map(int, input().split()))
      nums.append(rowInput)

   maxSum = 0

   for i in range(n):
      for j in range(m):
         sum = nums[i][j]
         
         row = i - 1
         col = j - 1

         #left up
         while row >= 0 and col >= 0:
            sum += nums[row][col]
            row -= 1
            col -= 1

         row = i - 1
         col = j + 1

         #right up
         while row >= 0 and col < m:
            sum += nums[row][col]
            row -= 1
            col += 1

         row = i + 1
         col = j - 1

         #left down
         while row < n and col >= 0:
            sum += nums[row][col]
            row += 1
            col -= 1

         row = i + 1
         col = j + 1

         #right down
         while row < n and col < m:
            sum += nums[row][col]
            row += 1
            col += 1

         maxSum = max(maxSum, sum)
         # print(maxSum, i, j)

   print(maxSum)    
