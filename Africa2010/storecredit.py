class Solution(object):
    def storeCredit(self, credit, items):
        d = {}
        for i, item in enumerate(items):
            if item in d:
                d[item].append(i)
            else:
                d[item] = [i]

        for i, item in enumerate(items):
            if item >= credit:
                continue
            if credit - item in d:
                if credit - item == item:
                    if len(d[item]) == 2:
                        return map(lambda x:x+1,d[item])
                    else: continue
                else:
                    j = d[credit-item][0]
                    return [min(i,j)+1, max(i,j)+1]

if __name__=="__main__":
    #filename = "A-small-practice.in" 
    filename = "A-large-practice.in" 
    nf = open(filename[:-2]+"out", "w")
    sol = Solution()
    f = open(filename)
    n = int(f.readline().strip())
#    print n
    for i in xrange(n):
        credit = int(f.readline().strip())
        #print credit
        itemnum = int(f.readline().strip())
        items = map(int, f.readline().split())
        #print items
        res = sol.storeCredit(credit, items)
        nf.write("Case #%d: %d %d\n" % (i+1, res[0], res[1])) 
