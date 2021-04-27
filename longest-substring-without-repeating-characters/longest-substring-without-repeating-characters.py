class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap= {} #value:index
        left = 0
        right = 0
        long_str= 0
        
        while left < len(s) and right < len(s):
            if s[right] in hashmap:
                #since we found the duplicate so update the left pointer to the duplicate
                left = max(left,hashmap[s[right]]+1) 
            # print(left,right)
            hashmap[s[right]] = right
            long_str= max(long_str,right-left+1)
            right+=1 #increment the pointer
            
        return long_str
                
        