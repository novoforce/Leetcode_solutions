class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr= [-1,-1] #let the first and the last position be -1 -1
        if len(nums) == 0:
            return arr
        
        start= 0
        end= len(nums)-1
        
        while(start <= end):
            mid= start + (end-start)//2
            if nums[mid] == target:
                arr[0] = mid #storing the first occurrance
                end= mid - 1 #for the first occurrance
            elif target < nums[mid]:
                end= mid - 1
            else:
                start= mid + 1
            
        start= 0
        end= len(nums)-1
        
        while(start <= end):
            mid= start + (end-start)//2
            if nums[mid] == target:
                arr[1] = mid #storing the 2nd occurrance
                start= mid + 1 #for the last occurrance
            elif target < nums[mid]:
                end= mid - 1
            else:
                start= mid + 1
        
        return arr #returning the occurrances
        
        
        