class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SinglyLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Adding new node in a sorted way in the list
    def insert(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
        elif self.headval.dataval >= newdata:
            newnode.nextval = self.headval
            self.headval = newnode
        else:
            nodepos = self.headval
            while nodepos.nextval and nodepos.nextval.dataval < newdata:
                nodepos = nodepos.nextval
            newnode.nextval = nodepos.nextval
            nodepos.nextval = newnode

    # Search for an element in the list
    def search(self, newdata):
        nodepos = self.headval
        while nodepos:
            if nodepos.dataval == newdata:
                print("Element present")
                return
            nodepos = nodepos.nextval
        print("Element not present")

    # Deleting a node
    def deletenode(self, newdata):
        nodepos = self.headval
        if nodepos is not None:
            if nodepos.dataval == newdata:
                if nodepos.nextval is None:
                    print("This is the only element present")
                else:
                    self.headval = nodepos.nextval
                return
        while nodepos is not None and nodepos.nextval is not None and nodepos.nextval.dataval != newdata:
            nodepos = nodepos.nextval
        if nodepos is not None and nodepos.nextval is not None:
            temp = nodepos.nextval
            nodepos.nextval = temp.nextval

# Main program
list1 = SinglyLinkedList()
ch = 0
while ch < 5:
    print("1. Insert 2. Delete 3. Print 4. Search 5. Exit")
    ch = int(input())
    if ch == 1:
        print("Insert value to be inserted:")
        element = int(input())
        list1.insert(element)
    elif ch == 2:
        print("Enter value to be deleted:")
        element = int(input())
        list1.deletenode(element)
    elif ch == 3:
        print("Values are:")
        list1.listprint()
    elif ch == 4:
        print("Enter search element:")
        element = int(input())
        list1.search(element)
