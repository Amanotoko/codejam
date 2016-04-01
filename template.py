from sys import argv
class Solution(object):
    def test(self, ):


if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            n = int(f.readline())
            for i in range(n):
                t = sol.test()
                nf.write("Case #%d: %d\n" % (i+1, t))
        except IOError:
            print ("No such file: %s" % filename)
    except IndexError:
        print ("Too few parameters!")
        print ("Usage: python test.py inputfile")
