class Solution:
    def longestValidParentheses(self, s):
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result

#     def longestValidParentheses(self, s: str) -> int:
#         str1= list(s)
#         if len(str1) == 0:
#             return 0
#         stx= [str1[0]] #initialise stack with the first item from string
#         count= 0
#         top = -1
        
#         for i in range(1,len(s)):
#             if s[i] == '(':
#                 stx.append(s[i])
#             elif s[i] == ')' and len(stx):
#                 if stx.pop(top) == '(':
#                     count+=2
#         return count
        
        