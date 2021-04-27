class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count= 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[count] = nums[i]
                count+= 1
        # print('count:> ',count)
        
        while count <= len(nums)-1:
            nums[count] = 0
            count+= 1
        