        #using insertion sort
        for i in range(1, len(nums)):
            temp = nums[i]

            for j in range(i, 0, -1):
                if temp < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
