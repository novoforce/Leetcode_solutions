class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #sort the array
        arr.sort()
        result= [[]]
        pairs= []
        min_diff= 10^6
        for i in range(1,len(arr)):
            min_diff = min(arr[i] - arr[i-1], min_diff)
            
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == min_diff:
                pairs.append(arr[i-1])
                pairs.append(arr[i])
        result = [pairs[i:i+2] for i in range(0,len(pairs),2)]
        return result
        