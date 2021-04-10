class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap= {}#val: feq
        
        for a in arr:
            if a in hashmap:
                hashmap[a]+= 1
            else:
                hashmap[a]= 1
        
        for h in hashmap.values():
            if list(hashmap.values()).count(h) > 1:
                return False
        return True
                