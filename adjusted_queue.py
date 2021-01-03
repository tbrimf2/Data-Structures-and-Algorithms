#this program implements a queue using a list
#such that the rear of the queue is at the back of the list
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def show(self):
        return self.items

q = Queue()
print(q.isEmpty())
q.enqueue(13)
q.enqueue('hello')
q.enqueue(False)
q.enqueue(8.3)
print(q.show())
print(q.size())
q.dequeue()
print(q.show())