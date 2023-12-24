
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def reverse(stack):
    if not isEmpty(stack):
        poppedValue = pop(stack)
        reverse(stack)
        insertAtBottom(stack, poppedValue)

def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack,temp)


def str(stack):
    for i in range(len(stack)):
        print(stack[i], end=' ')


stack = createStack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
str(stack)
reverse(stack)
print("")
str(stack)

