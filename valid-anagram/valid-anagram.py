class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap= {} # val:frequency
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]]+= 1
                
        for i in range(len(t)):
            if t[i] in hashmap and hashmap[t[i]] != 0:
                hashmap[t[i]]-=1
            elif t[i] not in hashmap:
                return False
            
            if hashmap[t[i]] == 0:
                del hashmap[t[i]]
                
        if len(hashmap) == 0:
            return True
        else:
            return False
        
        