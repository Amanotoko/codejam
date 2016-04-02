from sys import argv
import decimal
class Solution(object):
    def gcube(self, nDim, start, end):
        vol = 1
        for i in range(start, end):
            vol *= nDim[i]
        vol = decimal.Decimal(vol)
        return vol**(decimal.Decimal(1.0/(end-start)))

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
                nDim = list(map(int, f.readline().split()))
                nf.write("Case #%d:\n" % (i+1))
                for j in range(m):
                    start, end = list(map(int, f.readline().split()))
                    res = sol.gcube(nDim, start, end+1)
                    nf.write("%f\n" % (res))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python gcube.py inputfile")
