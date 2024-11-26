class Solution:
    def reverseArray(self, arr):
        m = 0
        n = len(arr) - 1
        
        while m < n:
            temp = arr[m]
            arr[m] = arr[n]
            arr[n] = temp
            
            m += 1
            n -= 1
