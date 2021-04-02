class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #let the current_sum and the max_sum_sum be the first element
        max_sum = curr_sum = nums[0] 
        
        for num in nums[1:]: #iterate from first element to the end of the array
            
            #check for where the current no or the sum of the values till the no is greater and make that value as the curr_sum
            
            curr_sum = max(num,num+curr_sum)
            
            # print(curr_sum,max_sum)
            max_sum = max(curr_sum,max_sum)
            
        return max_sum