class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap= {} #val:freq
        count=0
        if len(nums)==1:
            return nums[0]
        for no in nums:
            if no not in hashmap:
                hashmap[no] = 1
            else:
                hashmap[no]+= 1
                
        if len(hashmap) == 1:
            return 0
        
        for h in hashmap:
            if hashmap[h]==1:
                count+= h
            
        return count
        