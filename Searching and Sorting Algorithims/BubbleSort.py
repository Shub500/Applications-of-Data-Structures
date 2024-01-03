def bubbleSort(list):
    for i in range(0, len(list) - 1, 1):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
    return list

list = [3,4,-3,1,3,2,7,4]
print(bubbleSort(list))