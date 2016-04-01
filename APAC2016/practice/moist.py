from sys import argv
class Solution(object):
    def moist(self, stk):
        count = 0
        pre = stk[0]
        for i in range(1,len(stk)):
            if stk[i] < pre:
                count += 1
            else:
                pre = stk[i]
        return count

if __name__ == "__main__":
    try:
        filename = argv[1]
        try:
            f = open(filename)
            nf = open(filename[:-2]+"out", "w")
    
            sol = Solution()
            n = int(f.readline())
            for i in range(n):
                m = int(f.readline())
                stk = []
                for j in range(m):
                    name = f.readline()
                    stk.append(name)
                t = sol.moist(stk)
                nf.write("Case #%d: %d\n" % (i+1, t))
        except IOError:
            print "No such file: %s" % filename
    except IndexError:
        print "Too few parameters!"
        print "Usage: python moist.py inputfile"
