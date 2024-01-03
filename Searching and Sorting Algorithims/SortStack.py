def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def sorted(stack):
    sorted = True
    if not isEmpty(stack):
        for i in range(len(stack)-1):
            if stack[i] > stack[i+1]:
                sorted = False
    return sorted

def sort(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        sort(stack)
        insertSort(stack, temp)

def insertSort(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        if item > max(stack):
                push(stack, item)
        else:
            temp = pop(stack)
            insertSort(stack, item)
            push(stack, temp)

def str(stack):
    for i in range(len(stack)):
        print(stack[i], end=' ')


stack = createStack()
push(stack, -2)
push(stack, 4)
push(stack, 1)
push(stack, 5)
push(stack, -5)
str(stack)
print(sorted(stack))
sort(stack)
print("")
str(stack)
print(sorted(stack))




