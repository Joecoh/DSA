def quicksort(elements, left, right):
    if left < right:
        pivot = right - 1
        i = left
        j = right - 1

        while True:
            while i < pivot and elements[i] < elements[pivot]:
                i += 1
            while j >= left and elements[j] > elements[pivot]:
                j -= 1

            if i < j:
                # Swap elements
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
            else:
                break

        # Swap pivot into correct position
        temp = elements[i]
        elements[i] = elements[pivot]
        elements[pivot] = temp

        print(elements, 'mid:', i)

        # Recursively sort the partitions
        quicksort(elements, left, i)
        quicksort(elements, i + 1, right)

# Example usage
elements = [1, 4, 6, 3, 2, 7, 9, 30, 23, 21, 44]
quicksort(elements, 0, len(elements))
print("Sorted elements:", elements)
