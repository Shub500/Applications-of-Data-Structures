'''
Name: Shubham Mohole
Program: As stated below one of the pre-conditions of this program is that the list has to be already sorted from low
to high. The main principle behind the program is it will check the middle of the current array to see if it is equal to
or not equal to the target. If it is equal then middle is returned, if not then the array is divided so that the next
time the function looks at the array it will be a half smaller than the original. The side of the array the function looks
at depends on if the middle was greater than or less than the target. If it was greater than the function will look at the
left hand side since that contains all values less than the middle value. If it was less than the function will look at the
right hand side since that contains all values greater than the middle value. If the target was not found meaning there
there is no more array to divide then the function return -1.
'''


def BinarySearch (list, low, high, target):
    '''
    :param list: the pre-conditions are that the list is already sorted from low to high
    :param low: the low index
    :param high: the high index
    :param target: the value being searched for
    :return: return's the index which the target was found
    '''
    if len(list) == 0:
        print("Array is empty")
    elif low == high: # this will be our base and will check if any elements remain in the list
        return - 1
    else:
        middle = (low + high) // 2 # will find the middle index
        if (target == list[middle]):
            return middle
        elif(target < list[middle]): # if the key is less than the middle value that means the key must be in the left
            #side of the array
            return BinarySearch(list, low, middle, target) # this call will check if the middle of the list between the low
            # index and the index before the middle has the target
        else: # this means that the target lies in the second half of the list and so the new searh will take place from
            # middle + 1 index to high
            return BinarySearch(list, middle, high, target)


# Test Drive
arr = []
x = 9
print(BinarySearch(arr, 0, len(arr), x))
print("---")
arr = [-1,0,1,2,3,4,5]
for i in range(len(arr)):
    x = arr[i]
    print("Searching for " + str(x) + " found at " + str(BinarySearch(arr, 0, len(arr), x)))
    print("---")
x = -39
print(BinarySearch(arr, 0, len(arr), x))



