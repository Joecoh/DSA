print("Code for binary search tree traversal")

class Node:
    # Initialize the node with data and left/right children
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert method to add nodes to the BST
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
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
        else:
            self.data = data

    # Print the tree - INORDER TRAVERSAL - ALWAYS IN ASCENDING ORDER
    def pt1(self):
        if self.left:
            self.left.pt1()
        print(self.data)  # INORDER
        if self.right:
            self.right.pt1()

    # Print the tree - POSTORDER TRAVERSAL
    def pt2(self):
        if self.left:
            self.left.pt2()
        if self.right:
            self.right.pt2()
        print(self.data)  # POSTORDER

# Use the insert method to add nodes
r = int(input("Enter root node value: "))
root = Node(r)
i = int(input("Enter number of child nodes: "))
for _ in range(i):
    c = int(input("Enter child node value: "))
    root.insert(c)

print("\nINORDER TRAVERSAL (LEFT -> ROOT -> RIGHT) ALWAYS IN ASCENDING ORDER:")
root.pt1()

print("\nPOSTORDER TRAVERSAL (LEFT -> RIGHT -> ROOT):")
root.pt2()
