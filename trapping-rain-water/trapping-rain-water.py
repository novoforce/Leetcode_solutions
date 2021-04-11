class Solution:
    def trap(self, height: List[int]) -> int:
        max_left= []
        max_right= []
        for i in range(0, len(height)):
            if i == 0:
                max_left.append(height[i])
            else:
                max_left.append(max(height[0:i]))
                
        for i in range(len(height),0,-1):
            if i == len(height):
                max_right.append(height[i-1])
            else:
                max_right.append(max(height[i:len(height)]))
                
        max_right= max_right[::-1]
        ans=0
        for i in range(0,len(height)):
            if min(max_left[i],max_right[i]) - height[i] >=0:
                ans+= min(max_left[i],max_right[i]) - height[i]
        # print('----> ',ans)
        
        return ans