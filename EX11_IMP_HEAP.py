def childNodes(i):
    return (2 * i) + 1, (2 * i) + 2  # (2 * i) + 1 -> LEFT NODE, (2 * i) + 2 -> RIGHT NODE

def traversed(a, i=0, d=0):
    if i >= len(a):
        return
    l, r = childNodes(i)
    traversed(a, r, d + 1)  # Traverse the right subtree
    print(" " * d + str(a[i]))  # Print the current node
    traversed(a, l, d + 1)  # Traverse the left subtree

# Instead of taking inputs directly, give values
a = []
r = int(input("root: "))
a.append(r)
i = int(input("Enter number of child nodes: "))
# Enter values in ascending order
for _ in range(i):
    c = int(input("child: "))
    a.append(c)

a.sort()
print("\nTREE REPRESENTATION IN MIN HEAP\n")
traversed(a)

a.reverse()
print("\nTREE REPRESENTATION IN MAX HEAP\n")
traversed(a)
