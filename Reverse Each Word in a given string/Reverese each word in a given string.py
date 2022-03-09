
class Solution:
    def reverseWords(self, s):
        # code here
        s = s.split('.')
        s = [i[::-1] for i in s]
        return '.'.join(s)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver 
