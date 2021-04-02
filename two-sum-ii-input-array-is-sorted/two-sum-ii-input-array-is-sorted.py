class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #typical 2 pointer method
        i= 0
        j= len(numbers)-1
        
        while(i<=len(numbers) and j >=0):
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                break
            
        return [i+1,j+1]
        