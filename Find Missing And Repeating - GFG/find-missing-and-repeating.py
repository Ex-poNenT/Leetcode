#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        a = None
 
        i = 0
   
        s = {i for i in range(1,n+1)}
        while i<n : 
            if arr[i] not in s :
                a = arr[i]
            if arr[i] in s :
                s.discard(arr[i])
            i+=1
      
        b = list(s)[0]
        return [a,b]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends