#User function Template for python3

class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            
            start += 1
            end -= 1
            
    def return_pivot(self, arr): 
        i = len(arr) - 2
        while i>=0:
            if arr[i] < arr[i+1]:
              return i
            
            i -= 1
            
        return -1
            
    def find_greater(self, arr, pivot):
        i = len(arr) - 1
        
        while i > pivot:
            if arr[i] > arr[pivot]:
               return i
               
            i -= 1
            
        return -1
          
    def nextPermutation(self, arr):
        pivot = self.return_pivot(arr)
        
        if pivot == -1:
          self.reverse(arr, 0, len(arr) -1)
          return
          
        index = self.find_greater(arr, pivot)
        tmp = arr[index]
        arr[index] = arr[pivot]
        arr[pivot] = tmp
        
        self.reverse(arr, pivot + 1, len(arr) - 1)               
