class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        bo_no = 0
        while left <= right:
            if left == right:
                bo_no+= 1
                break
                
            if people[left] + people[right] <= limit:
                left+= 1
                right-= 1
                bo_no+= 1
            else:
                right-=1
                bo_no+= 1
                
        return bo_no
            
        