class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        #increasing sequence
        while(i < len(arr) and arr[i] > arr[i-1]):
            i+= 1
        #if there is only single element OR only increasing sequence element
        if i == 1 or i == len(arr):
            return False
        #decreasing sequence
        while(i < len(arr) and arr[i] < arr[i-1]):
            i+= 1
        
        return i == len(arr)
        