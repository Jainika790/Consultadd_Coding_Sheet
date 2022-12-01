class Solution:
	def matSearch(self,mat, N, M, X):
		# Complete this function
		for i in range(N):
		    if X in mat[i]:
		        return 1
		return 0
	#print(matSearch(1,[[3 30 38][44 52 54][57 60 69]],3,3,62))