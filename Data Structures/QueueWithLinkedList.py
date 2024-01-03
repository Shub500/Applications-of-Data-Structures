class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.nextNode = next_node

    def setNextNode(self, newNode):
        self.nextNode = newNode

    def getNextNode(self):
        return self.nextNode

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class QueueViaLL:
    def __init__(self, size):
        self.max_size = size
        self.array = [None] * self.max_size
        self.front = None
        self.back = None

    def enqueue(self, value):
        newNode = Node(value)
        if self.back == None:
            self.front = newNode
            self.back = newNode
        self.back.setNextNode(newNode)
        self.back = newNode

    def dequeue(self):
        if self.front == None:
            return None
        removeNode = self.front
        self.front = removeNode.getNextNode()

        if (self.front == None):
            self.back = None

    def __str__(self):
        for i in range(len(self.array)):
            if self.array[i] != None:
                print(str(self.array[i].getValue()), end=" ")


test = QueueViaLL(5)
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
test.enqueue(9)
test.dequeue()
test.enqueue(10)
test.dequeue()
test.dequeue()
test.dequeue()
test.enqueue(6)
print(test.front.value)
print(test.back.value)

