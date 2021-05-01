class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos= [0,0]
        for i in moves:
            if i == 'U':
                pos[1]+= 1
            elif i == 'D':
                pos[1]+= -1
            elif i == 'L':
                pos[0]+= 1
            elif i == 'R':
                pos[0]-= 1
        
        return pos[0] == pos[1] == 0