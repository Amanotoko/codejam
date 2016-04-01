from sys import argv
class Solution(object):
    def badhorse(self, pairs):
        graph = {}
        d = {}
        for pair in pairs:
            a, b = pair
            d[a] = d[b] = 0
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set([b])
            if b in graph:
                graph[b].add(a)
            else:
                graph[b] = set([a])
        
        def dfs(graph, d, p, groupnum):
            d[p] = groupnum
            for op in graph[p]:
                if d[op] == groupnum:
                    return False
                if d[op] == 0:
                    if not dfs(graph, d, op, -1*groupnum):
                        return False
            return True
        
        for p in d:
            if d[p] == 0:
                if not dfs(graph, d, p, 1):
                    return "No"

        return "Yes"

if __name__ == "__main__":
    filename = argv[1]
    f = open(filename)
    nf = open(filename[:-2]+"out", "w")

    sol = Solution()
    n = int(f.readline())
    for i in range(n):
        m = int(f.readline())
        pairs = []
        for j in range(m):
            pair = f.readline().split()
            pairs.append(pair)
        t = sol.badhorse(pairs)
        nf.write("Case #%d: %s\n" % (i+1, t))
