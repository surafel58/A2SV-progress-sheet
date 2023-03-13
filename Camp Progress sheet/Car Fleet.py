class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        decStack = []
        cars = list(zip(position, speed))
        cars.sort()
        timeSpent = []

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            timeSpent.append(time)

        for i in range(len(cars)):
            while decStack and decStack[-1] <= timeSpent[i]:
                decStack.pop()

            decStack.append(timeSpent[i])

        return len(decStack)
