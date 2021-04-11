class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        #let the max_value be 0
        max_value=0
        val1 = val2 = val3 = val4 = []
        
        val1 = [i+arr1[i]+arr2[i]   for i in range(len(arr1))]
        val2 = [i+arr1[i]-arr2[i]   for i in range(len(arr1))]
        val3 = [i-arr1[i]+arr2[i]   for i in range(len(arr1))]
        val4 = [i-arr1[i]-arr2[i]   for i in range(len(arr1))]
        
        max_value= max(max_value,max(val1) - min(val1))
        max_value= max(max_value,max(val2) - min(val2))
        max_value= max(max_value,max(val3) - min(val3))
        max_value= max(max_value,max(val4) - min(val4))
        
        
        return max_value
        