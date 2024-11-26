#User function Template for python3
import sys

class Solution:
    def getSecondLargest(self, arr):
      first_largest = -sys.maxsize
      second_largest = -sys.maxsize
      
      for element in arr:
          if element > first_largest:
              second_largest = first_largest
              first_largest = element 
          elif element != first_largest and element > second_largest:
              second_largest = element 
      if second_largest != -sys.maxsize:
          return second_largest
      return -1;

#{  # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
