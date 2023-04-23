class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.familyTree = defaultdict(list)
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.familyTree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # print(self.familyTree)
        visited = []
        def dfs(node, visited):
            
            if node not in self.deaths:
                visited.append(node)
            
            for child in self.familyTree[node]:
                    dfs(child, visited)
        
        dfs(self.root, visited)

        return visited

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
