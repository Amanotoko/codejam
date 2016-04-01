from sys import argv
from math import sqrt, asin, acos, degrees
class Solution(object):
    def captainhammer(self, v, d):
       a = 9.8
       t1 = v**4 - a*a*d*d
       if t1 < 0: t1 = 0
       t2 = sqrt(t1)
       v1 = sqrt((v**2 - t2)/2)
       return degrees(asin(v1/v))

if __name__ == "__main__":
    filename = argv[1]
    f = open(filename)
    nf = open(filename[:-2]+"out", "w")

    sol = Solution()
    n = int(f.readline())
    for i in range(n):
        v, d = map(int,f.readline().split()) 
        t = sol.captainhammer(v, d)
        nf.write("Case #%d: %f\n" % (i+1, t))
