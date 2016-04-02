from sys import argv
class Solution(object):
    def googol(self, k):
        pow2 = 1
        while pow2 <= k:
            if pow2 == k:
                return 0
            pow2 *= 2

        tmp = self.googol(pow2-k)
        if tmp == 0:
            return 1
        else:
            return 0
        

if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            n = int(f.readline())
            for i in range(n):
                k = int(f.readline())
                t = sol.googol(k)
                nf.write("Case #%d: %d\n" % (i+1, t))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python googol.py inputfile")
