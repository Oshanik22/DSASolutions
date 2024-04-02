class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        result = []

        def makeGraph():
            graph = defaultdict(set)
            for i,j in prerequisites:
                graph[i].add(j)

            return graph
        
        graph = makeGraph()

        def canDo(i):
            if visited[i] == 1:
                return False

            if visited[i] == 2:
                return True
            
            visited[i] = 1

            for node in graph[i]:
                if not canDo(node):
                    return False
                
            visited[i] = 2
            result.append(i)
            return True

        for i in range(numCourses):
            if not canDo(i):
                return []

        return result

