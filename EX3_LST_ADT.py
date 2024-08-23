n = 0
list1 = []

while n < 5:
    print('1.append 2.remove 3.size 4.display 5.exit')
    n = int(input())
    
    if n == 1:
        print('Enter a number')
        num = int(input())
        list1.append(num)
        
    elif n == 2:
        print('Enter a number to be removed')
        num = int(input())
        if num in list1:
            list1.remove(num)
        else:
            print('Number not in list')
    
    elif n == 3:
        print('Size:', len(list1))
    
    elif n == 4:
        print(list1)
