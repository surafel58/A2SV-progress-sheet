from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		colors = [0] * V
		def dfs(node, parent):
		    
		    if colors[node] == 1:
		        return True
		  
		    colors[node] = 1
		    
		    for neighbour in adj[node]:
		        
		        if neighbour != parent:
		            if dfs(neighbour, node):
		                return True
		                
		    colors[node] = 2
		    return False
	
    	for node in range(V):
    	    
    	    if colors[node] != 2:
    	        if dfs(node, -1):
    	            return True
    	            
        return False
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
