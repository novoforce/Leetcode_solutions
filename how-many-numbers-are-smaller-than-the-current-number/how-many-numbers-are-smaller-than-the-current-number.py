class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap= {} #number:index
        sorted_nums= sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in hashmap:
                hashmap[sorted_nums[i]] = i
                
        for i in range(len(nums)):
            nums[i] = hashmap[nums[i]]
            
        return nums
        
        