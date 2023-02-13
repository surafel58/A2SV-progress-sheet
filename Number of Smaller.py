def getSmallerFreq():
    n,m = list(map(int, input().split()))
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    
    p1 = 0
    p2 = 0
    counter = 0
    result = []
    while p1 < n and p2 < m:
        if list1[p1] < list2[p2]:
            counter += 1
            p1 += 1
        else:
            result.append(str(counter))
            p2 += 1
            
    if p1 == n:
        while p2 < m:
            result.append(str(counter))
            p2 += 1
    
    print(" ".join(result))
 
getSmallerFreq()
