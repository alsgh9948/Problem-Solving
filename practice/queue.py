class MyQueue:
    def __init__(self,size):
        self.data = [0]*(size+1)
        self.size = size+1
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def peek(self):
        if self.is_empty():
            raise Exception('큐가 빔')
        return self.data[self.front]

    def en_queue(self,insert_data):
        if (self.rear+1)%self.size == self.front:
            raise Exception('큐가 꽉참')

        self.data[self.rear] = insert_data
        self.rear = (self.rear+1)%self.size
    def de_queue(self):
        if self.is_empty():
            raise Exception('큐가 빔')

        return_data = self.data[self.front]
        self.front = (self.front+1)%self.size
        return return_data

q = MyQueue(3)
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)
print(q.de_queue())
print(q.de_queue())
q.en_queue(4)
print(q.de_queue())
print(q.de_queue())

