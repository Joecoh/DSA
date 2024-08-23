# Stack ADT
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Queue ADT
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Stack ADT operation example
n1 = 0
n2 = 0
print('Enter number. 1.Stack 2.Queue')
i = int(input())
if i == 1:
    s = Stack()
    while n1 < 5:
        print("Enter number. 1.push 2.pop 3.size 4.display 5.exit")
        n1 = int(input())
        if n1 == 1:
            print('Enter number')
            num = int(input())
            s.push(num)
        elif n1 == 2:
            s.pop()
            print('Value popped')
        elif n1 == 3:
            print('Size:', s.size())
        elif n1 == 4:
            print(s.items)
elif i == 2:
    q = Queue()
    while n2 < 5:
        print("Enter number. 1.enqueue 2.dequeue 3.size 4.display 5.exit")
        n2 = int(input())
        if n2 == 1:
            print('Enter number')
            num = int(input())
            q.enqueue(num)
        elif n2 == 2:
            q.dequeue()
            print('dequeue done')
        elif n2 == 3:
            print('Size:', q.size())
        elif n2 == 4:
            print(q.items)
