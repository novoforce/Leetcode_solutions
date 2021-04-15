class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [] #empty array
        self.top = -1

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.arr.insert(0,x)
        self.top= self.arr[-1]
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ele= self.arr.pop(-1)
        if len(self.arr) == 0:
            self.top= -1
        else:
            self.top= self.arr[-1]
        return ele
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.arr[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.arr) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()