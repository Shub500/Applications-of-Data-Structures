def maxOfList(list):

    if len(list) == 1:
        return list[0]
    else:
        if list[0] > list[len(list) -1]:
           return maxOfList(list[0:len(list)-1])
        else:
            return maxOfList(list[1:len(list)])

array = [3,46,2,3,2]
print(maxOfList(array))

def convertBase(number, base, sourceBase):
    pass


