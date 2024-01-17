class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        allMails = {}
        uf = UnionFind(len(accounts))
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in allMails:
                    uf.union(idx, allMails[email])
                allMails[email] = idx
        mergedAccounts = defaultdict(list)
        for email, idx in allMails.items():
            root = uf.find(idx)
            mergedAccounts[root].append(email)
        
        result = []
        for idx, emails in mergedAccounts.items():
            result.append([accounts[idx][0]] + sorted(emails))

        return result


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, target):
        if self.root[target] != target:
            self.root[target] = self.find(self.root[target])
        return self.root[target]
    
    def union(self, x, y):
        if x == y:
            return
        rootX, rootY = self.find(x), self.find(y)
        rankX, rankY = self.rank[rootX], self.rank[rootY]

        if rankX > rankY:
            self.root[rootY] = rootX
        elif rankY > rankX:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
