class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        
        dec_q = []
        
        for i in range(len(temperatures)):
            while dec_q and temperatures[i] > temperatures[dec_q[-1]]:
                pre_i = dec_q.pop()
                ans[pre_i] = i-pre_i
            dec_q.append(i)
            
        return ans
        