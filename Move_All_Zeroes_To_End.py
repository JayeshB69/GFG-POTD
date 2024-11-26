#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        l = 0
        for r in range(len(arr)):
            if arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
            
        return arr;





 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
