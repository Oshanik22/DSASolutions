class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathMap = defaultdict(set)
        cities = set()

        for source,dest in paths:
            pathMap[source].add(dest)
            cities.add(source)
            cities.add(dest)
        
        for city in cities:
            if len(pathMap[city]) == 0:
                return city

        return ""
