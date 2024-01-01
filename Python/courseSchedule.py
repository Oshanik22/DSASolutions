class Solution:
    def canFinish(self, num: int, req: List[List[int]]) -> bool:
        graph = self.makeGraph(num, req)
        state = [0 for i in range(num)] #state=0 means not visited, state = 1 means visited, state = -1 means visiting
        for course in range(num):
            if not self.canComplete(course, graph, state):
                return False
        
        return True
    
    def makeGraph(self, num, req):
        graph = {}

        for i in range(num):
            graph[i] = []

        for i,j in req:
            graph[i].append(j)

        return graph
    
    def canComplete(self, i, graph, state):
        if state[i] == 1:
            return True
        if state[i] == -1:
            return False
        state[i] = -1

        for dep in graph[i]:
            if not self.canComplete(dep, graph, state):
                return False
        
        state[i] = 1
        return True