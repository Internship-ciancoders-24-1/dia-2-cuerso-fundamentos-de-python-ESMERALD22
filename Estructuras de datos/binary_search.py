import random 

def binary_search(data, target, lowIndex, highIndex):
    if(lowIndex > highIndex):
        return False
    
    mid =(lowIndex + highIndex) // 2
    
    if target == data[mid]:
        return True
    
    elif target < data[mid]:
        return binary_search(data,target,lowIndex, mid-1)
    else:
        return binary_search(data,target, mid+1, highIndex)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    print(data)
    data.sort()
    #sorted_data= sorted(data)
    print(data)

    target =  int (input('What number would do you like to find'))
    found = binary_search(data, target, 0, len(data)-1)
    print(found)



