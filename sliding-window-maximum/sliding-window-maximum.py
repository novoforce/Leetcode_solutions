class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i>=k-1:
                out.append(nums[d[0]])
        return out
    
#         final_arr= []
#         # hashmap= {}
#         #create a sliding window
#         i=0
#         j = i+k
#         final_arr.append(max(nums[i:j]))
#         # hashmap[nums.index(final_arr[0])] = final_arr[-1] #first val in hashmap
#         i+=1
#         j+=1

#         while j <= len(nums):
#             final_arr.append(max(nums[i:j]))
#             j+=1
#             i+=1
#         return final_arr
    
    
        
        
        