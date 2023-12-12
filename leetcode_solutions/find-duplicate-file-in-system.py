class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for path in paths:
            path = path.split()
            root = path[0]
            for n in path[1:]:
                name, _, contents = n.partition('(')
                c[contents].append(root+'/'+name)
        return [x for x in c.values() if len(x) > 1]