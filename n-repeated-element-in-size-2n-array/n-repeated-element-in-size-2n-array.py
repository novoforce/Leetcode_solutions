class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        req_size= len(A)/2
        hashmap= {} #index:freq
        
        for no in A:
            if no not in hashmap:
                hashmap[no] = 1
            else:
                hashmap[no]+=1
                if req_size == hashmap[no]:
                    return no
                
        