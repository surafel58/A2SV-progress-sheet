test_case = int(input())
 
for _ in range(test_case):
   n = int(input())
   nums = list(map(int, input().split()))
 
   nums.sort()
 
   # left = 0
   right = n - 1
   answer = 'YES'
 
   while right > 0:
      if nums[right] - nums[right - 1] > 1:
         answer = 'NO'
         break 
      # left += 1
      right -= 1
 
   print(answer)
