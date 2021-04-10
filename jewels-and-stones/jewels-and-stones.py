class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap= {} #index:frequency
        count= 0
        for stone in stones:
            if stone in hashmap:
                hashmap[stone]+= 1
            else:
                hashmap[stone] = 1
        for j in jewels:
            if j in hashmap:
                count+= hashmap[j]
        return count
                
            
        