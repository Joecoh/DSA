class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def display(self):
        if self.left is not None:
            self.left.display()
        print(self.data)
        if self.right is not None:
            self.right.display()

# Driver code
print("Enter Root value:")
root_value = int(input())
obj = Node(root_value)

ch = 0
while ch < 4:
    print("1. Insert 2. Display 3. Exit")
    ch = int(input())
    if ch == 1:
        print("Enter the value to insert:")
        element = int(input())
        obj.insert(element)
    elif ch == 2:
        print("Depth First Traversal")
        obj.display()
    elif ch == 3:
        break
    else:
        print("Invalid option. Please enter a number between 1 and 3.")
