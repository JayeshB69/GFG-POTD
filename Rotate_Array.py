#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverse_arr(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            
            start += 1
            end -= 1
    
    def rotateArr(self, arr, d):
        d = d%len(arr)
        self.reverse_arr(arr, 0, d - 1)
        self.reverse_arr(arr, d, len(arr) - 1)
        self.reverse_arr(arr, 0,len(arr) - 1)
