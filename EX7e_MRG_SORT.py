def mergesort(elements, temp, arraysize):
    m_sort(elements, temp, 0, arraysize - 1)

def m_sort(elements, temp, left, right):
    if right > left:
        mid = (right + left) // 2
        m_sort(elements, temp, left, mid)
        m_sort(elements, temp, mid + 1, right)
        merge(elements, temp, left, mid + 1, right)

def merge(elements, temp, left, mid, right):
    left_end = mid - 1
    temp_pos = left
    num_elements = right - left + 1
    
    while left <= left_end and mid <= right:
        if elements[left] <= elements[mid]:
            temp[temp_pos] = elements[left]
            temp_pos += 1
            left += 1
        else:
            temp[temp_pos] = elements[mid]
            temp_pos += 1
            mid += 1
    
    while left <= left_end:
        temp[temp_pos] = elements[left]
        temp_pos += 1
        left += 1
    
    while mid <= right:
        temp[temp_pos] = elements[mid]
        temp_pos += 1
        mid += 1
    
    for i in range(num_elements):
        elements[right] = temp[right]
        right -= 1
    
    print(elements)

# Example usage
elements = [5, 3, 7, 8, 1, 2, 9]
arraysize = len(elements)
temp = [0] * arraysize
mergesort(elements, temp, arraysize)
