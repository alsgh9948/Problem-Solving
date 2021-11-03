class MyStack:
    def __init__(self,size):
        self.data = [0]*size
        self.size = size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def peek(self):
        if self.is_empty():
            raise Exception('스택이 빔')
        return self.data[self.top]

    def push(self,push_data):
        if self.size == self.top+1:
            raise Exception('스택이 꽉참')

        self.top += 1
        self.data[self.top] = push_data

    def pop(self):
        if self.is_empty():
            raise Exception('스택이 빔')

        return_data = self.data[self.top]
        self.top -= 1
        return return_data

s = MyStack(3)
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())

