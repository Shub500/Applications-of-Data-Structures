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


class StackViaLL:

    def __init__(self):
       self.head = None
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.nextNode = self.head
            self.head = newNode

    def pop(self):
        if self.isEmpty():
            return
        else:
            poppedNode = self.head
            self.head = self.head.nextNode
            poppedNode.nextNode = None
            return poppedNode.value






test = StackViaLL(5)
test.push(1)
test.push(2)
test.push(3)
test.pop()
test.__str__()