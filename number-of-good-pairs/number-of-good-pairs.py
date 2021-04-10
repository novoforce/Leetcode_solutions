class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #creating frequency hashmap
        hashmap= {} 
        count= 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]= 1
            else:
                hashmap[nums[i]]+= 1
                
        for h in hashmap:
            c= hashmap[h]
            c= c*(c-1)//2
            count+=c
            
        return count