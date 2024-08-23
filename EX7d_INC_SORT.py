def insertionsort(elements, number):
    for i in range(1, number):
        tmp = elements[i]
        j = i
        while j > 0 and tmp < elements[j - 1]:
            elements[j] = elements[j - 1]
            j = j - 1
        elements[j] = tmp

    print("Sorted elements:")
    print(elements)

# Example usage
elements = [1, 4, 3, 6, 100, 8]
number = len(elements)
insertionsort(elements, number)
