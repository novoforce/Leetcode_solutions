class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
        
        
        # n log(n) solution
#         num_set= set(nums)
#         num_list= list(num_set)
#         num_list.sort() #nlogn
#         nums = num_list

#         if len(nums) == 0:
#             return 0
#         elif len(nums) == 1:
#             return 1
        
#         # print(nums)
#         count=0
#         max_count=-1
        
#         for i in range(len(nums)-1): #n
#             # print(nums[i],nums[i+1],nums[i+1]+1)
#             if nums[i] != nums[i+1] and nums[i]+1 == (nums[i+1]):
#                 count+=1
#             if nums[i]+1 != (nums[i+1]):
#                 count=0
#             max_count= max(count,max_count)
#         # print('max_count ',max_count)
#         return max_count+1