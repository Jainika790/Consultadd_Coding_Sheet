#Move all zeros to end of array---------------
#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
        a = [0]*n
    	index = 0 
    	for i in arr:
    	    if i !=0:
    	        a[index]=i
    	        index+=1  
    	arr[::] = a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends