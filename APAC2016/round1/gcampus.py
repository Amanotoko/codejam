from sys import argv
class Solution(object):
    def gcampus(self, n, paths):
        graph = [[1000001]*n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        #init graph
        
        for path in paths:
            i,j,l = path
            graph[i][j] = min(graph[i][j], l)
            graph[j][i] = min(graph[j][i], l)
       
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

        ineff = []
        for i, path in enumerate(paths):
            s,d,l = path
            if graph[s][d] < l:
                ineff.append(i)
        
        return ineff

if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            t = int(f.readline())
            for i in range(t):
                n, m = list(map(int, f.readline().split()))
                paths = []
                for j in range(m):
                    path = list(map(int, f.readline().split()))
                    paths.append(path)
                res = sol.gcampus(n, paths)
                nf.write("Case #%d:\n" % (i+1))
                for j in range(len(res)):
                    nf.write("%d\n" % (res[j]))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python gcampus.py inputfile")
