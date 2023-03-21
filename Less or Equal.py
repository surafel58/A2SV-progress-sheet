# n, k = list(map(int, input().split()))

# nums = list(map(int, input().split()))
def lessOrEqual():
   n, k = list(map(int, input().split()))

   nums = list(map(int, input().split()))

   nums.sort()
   x = 0

   if k == 0 and nums[0] == 1:
      print(-1)
      return
   if k == 0 and nums[0] != 1:
      print(1)
      return

   if k != 0:
      x = nums[k-1]
   else:
      x = nums[0]

   counter = 0

   for i in range(n):
      if nums[i] <= x:
         counter += 1

   if counter != k:
      print(-1)

   else:
      print(x)


      
lessOrEqual()
