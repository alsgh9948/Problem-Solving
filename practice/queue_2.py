#스택 두개로 큐 만들기

class MyQueue:
    def __init__(self,size):
        self.size = size
        self.__en_stack = Mystack(size)
        self.__de_stack = Mystack(size)

        #0 : enqueue 상태, 1 : dequeue 상태
        self.__status = 0
    def is_empty(self):
        return self.__en_stack.is_empty() and self.__de_stack.is_empty()
    def peek(self):
        if self.__status == 0:
            self.change_status(self.__status)

        if self.__de_stack.is_empty():
            raise Exception('큐가 빔')

        return self.__de_stack.peek()
    def en_queue(self,insert_data):
        if self.__status == 1:
            self.change_status(self.__status)

        if self.size == self.__en_stack.top + 1:
            raise Exception('큐가 꽉참')

        self.__en_stack.push(insert_data)
    def de_queue(self):
        if self.__status == 0:
            self.change_status(self.__status)

        if self.__de_stack.is_empty():
            raise Exception('큐가 빔')

        return self.__de_stack.pop()

    def change_status(self,status):
        if status == 0:
            while not self.__en_stack.is_empty():
                self.__de_stack.push(self.__en_stack.pop())
            self.__status = 1
        else:
            while not self.__de_stack.is_empty():
                self.__en_stack.push(self.__de_stack.pop())
            self.__status = 0

class Mystack:
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

q = MyQueue(3)
q.en_queue(1)
q.en_queue(3)
q.en_queue(2)
print(q.de_queue())
print(q.de_queue())
print(q.de_queue())
q.en_queue(5)
q.en_queue(5)
q.en_queue(5)
q.en_queue(5)
print(q.de_queue())