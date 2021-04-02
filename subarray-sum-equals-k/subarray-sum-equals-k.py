class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap= {} #index:frequency
        hashmap[0] = 1 # start the hashmap with 0 size or we already have a hashmap of size 0, 1time
        sum_= 0
        result = 0
        
        for i in range(len(nums)):
            sum_ += nums[i]
            
            if (sum_ - k) in hashmap:
                result+= hashmap[sum_ - k]
                
            if sum_ in hashmap:
                hashmap[sum_] = hashmap[sum_] + 1
            else:
                hashmap[sum_] = 1
            
        
        
        
        
        
        
        return result
        
        
        
        
        
        # TLE
#         count=0
#         for start in range(0,len(nums)):
#             subarr_sum= 0
#             for end in range(start,len(nums)):
#                 subarr_sum+= nums[end]
                
#                 if subarr_sum == k:
#                     count+=1
#         return count
            
            
                