def getWinner():
    #approach - the same with merge sort    
    n, k = list(map(int, input().split()))
    rates = list(map(int, input().split()))
    players = [i for i in range(2**n)]
 
    winners = determineWinner(rates, players, 0, len(players) - 1, k)
    winners.sort()
 
    #add one to indices
    winners = [i + 1 for i in winners]
    print(*winners)
 
def determineWinner(rates, players, start, end, k):
    if start == end:
        return [players[start]]
    
    mid = start + (end - start) // 2
    leftWinner = determineWinner(rates, players, start, mid, k)
    rightWinner = determineWinner(rates, players, mid + 1, end, k)
 
    p1 = 0
    p2 = 0
    result = []
 
    while p1 < len(leftWinner) and p2 < len(rightWinner):
        #append the possible winners
        if rates[leftWinner[p1]] < rates[rightWinner[p2]]:
            if rates[rightWinner[0]] - rates[leftWinner[p1]] <= k:
                result.append(leftWinner[p1])
            p1 += 1
 
        else:
            if rates[leftWinner[0]] - rates[rightWinner[p2]] <= k:
                result.append(rightWinner[p2])
            p2 += 1
 
    while p1 < len(leftWinner):
        if rates[rightWinner[0]] - rates[leftWinner[p1]] <= k:
            result.append(leftWinner[p1])
        p1 += 1
 
    while p2 < len(rightWinner):
        if rates[leftWinner[0]] - rates[rightWinner[p2]] <= k:
            result.append(rightWinner[p2])
        p2 += 1
 
    return result
 
getWinner()
