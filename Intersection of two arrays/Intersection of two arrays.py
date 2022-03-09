
#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        c = set(a)
        d = set(b)
        f = c.intersection(d)
        return len(f)
        
