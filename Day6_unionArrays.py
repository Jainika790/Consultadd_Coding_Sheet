#Union of 2 sorted arrays
def mergeArrays(self,a,b,n,m):
        # code here 
        x = set()
        for i in a:
            x.add(i)
        for i in b:
            x.add(i)
        return sorted(x)
print(mergeArrays(1,[2,2,3,4,5],[1,1,2,3,4],5,5))