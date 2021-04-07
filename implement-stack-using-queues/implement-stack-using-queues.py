class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size= len(self.stack)-1
        i=0
        # print('--->',self.stack)
        while i < size:
            pop_ele = self.stack.pop(0)
            # print('pop_ele:>',pop_ele)
            self.stack.append(pop_ele)
            i+=1
        pop = self.stack.pop(0) 
        # print('pop:>',pop)
        return pop

    def top(self) -> int:
        """
        Get the top element.
        """
        size= len(self.stack)-1
        return self.stack[size]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.stack) == 0:
            return True 
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()