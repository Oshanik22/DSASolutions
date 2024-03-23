class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        neighbours = defaultdict(set)
        for p,q in edges:
            neighbours[p].add(q)
            neighbours[q].add(p)

        leaves = deque()

        for node in neighbours:
            if len(neighbours[node]) == 1:
                leaves.append(node)
        
        while n>2:
            leaves_size = len(leaves)
            n -= leaves_size

            for _ in range(leaves_size):
                leaf = leaves.popleft()
                neighbour = neighbours[leaf].pop()
                neighbours[neighbour].remove(leaf)

                if len(neighbours[neighbour]) == 1:
                    leaves.append(neighbour)
        
        result = []
        for node in neighbours:
            if len(neighbours[node]) > 0:
                result.append(node)

        return list(leaves)