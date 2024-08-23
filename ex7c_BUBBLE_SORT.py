def bubblesort(elements, number):
    for i in range(number):
        for j in range(1, number - i):
            if elements[j - 1] > elements[j]:
                # Swap numbers
                temp = elements[j - 1]
                elements[j - 1] = elements[j]
                elements[j] = temp
    print("Sorted elements:")
    print(elements)

# Example usage
elements = [1, 4, 2, 7, 5, 10, 5]
number = len(elements)
bubblesort(elements, number)
