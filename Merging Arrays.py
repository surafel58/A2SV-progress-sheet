def mergeArray():
    n,m = list(map(int, input().split()))
 
    list1 = input().split()
    list2 = input().split()
 
    p1 = 0
    p2 = 0
    result = []
    while p1 < n and p2 < m:
        if int(list1[p1]) < int(list2[p2]):    
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
 
    result = result + list1[p1:]
    result = result + list2[p2:]
 
    
    
    print(" ".join(result))
 
mergeArray()
