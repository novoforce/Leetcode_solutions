class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        #3 way partitioning
        left= mid = 0
        right= len(nums)-1
        
        while(mid <= right):
            if nums[mid] == 0:
                nums[mid],nums[left] = nums[left],nums[mid]
                left+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid],nums[right] = nums[right],nums[mid]
                right-=1
        
#         #counting approach
#         count_0 = count_1 = count_2 = 0
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 count_0+=1
#             elif nums[i] == 1:
#                 count_1+=1
#             elif nums[i] == 2:
#                 count_2+=1
        
#         for i in range(0,count_0):
#             nums[i] = 0
#         for i in range(count_0,(count_0+count_1)):
#             nums[i] = 1
#         for i in range((count_0+count_1),len(nums)):
#             nums[i] = 2

        
        