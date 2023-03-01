class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque()

        for i in range(n):
            queue.append((tickets[i], i))


        # print(queue)
        timer = 0

        while True:
            value = queue.popleft()
            temp = (value[0] - 1, value[1])
            timer += 1

            if temp[1] == k and temp[0] == 0:
                return timer

            if temp[0] > 0:
                queue.append(temp)


        return timer
        

