class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        unlocked = dict()
        queue = deque()

        unlocked[0] = 'U'
        queue.append(0)

        while queue:

            node = queue.popleft()

            for neighbour in rooms[node]:

                if neighbour not in unlocked:
                    unlocked[neighbour] = 'U'
                    queue.append(neighbour)
        
        if len(unlocked) == len(rooms):
            return True
        
        return False
