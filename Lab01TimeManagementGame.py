'''
Name: Shubham Mohole
Code Description: Three customer objects are created with unique names and a random patience. They are then added
into the queue. A score variable is also tabulated with a +1 if the customer is seated and -1 if a customer has left.
The program start time is also used to simulate the waiting and lowering of patience for all three customers. If a customer
has less than or equal to 0 patience the customer leaves and is removed from the queue. If the customer has a positive patience then the customer can
be seated or waited. If the customer is seated the the score increases and is removed from the queue. If the customer i
is waited then they will return back into the queue at the end of the line. If the player decides to quit the customer
leaves and the score decreases.
'''


import random
import Lab01Queue
import time

print("Hello welcome to Mini Cafe!")
print("The goal is to serve all of the customers before they lose patience")
print("The higher the number the more patience the customer has and the lower the "
      "number the more impatient a customer is. Also you have to be quick because as time goes on the patience of "
      "your customers goes down...")
print("Number of customers that are in line: 3")
print("Let's play!")


class Queue:
    def __init__(self, n):
        '''

        :param n: maximum size of the array

        This function creates two stacks of n length and head pointers to the begginning of the stacks
        '''
        self.arrSize = n
        self.queueStack = [None] * n
        self.top1 = -1
        self.popStack = [None] * n
        self.top2 = -1

    def length(self):
        '''
        :return: will return the length of the stack by adding one to the top of both stacks
        '''
        return self.top1 + 1

    def push(self, stackNum, item):
        if item == None: # if the item nothing then None will be returned
            return None
        elif stackNum == 1:
            if len(self.queueStack) != 0:# if the push is happening at the stack 1 then:
                self.top1 = self.top1 + 1  # moves the head pointer up and inserts the item
                self.queueStack[self.top1] = item
            else:
                print("Queue Stack is empty")
                return None
        elif stackNum == 2:
            if len(self.popStack) != 0:
                self.top2 = self.top2 + 1
                self.popStack[self.top2] = item
            else:
                print("Pop Stack is empty")
        else:
            print("Invalid Stack Number")
            return None
            # if the stack number is not 1 or 2 then it is invalid

    def pop(self, stackNum):
        if stackNum == 1:
            transferValue = self.queueStack[self.top1]  # stores the value on the top of StackQueue
            self.queueStack[self.top1] = None  # changes that index to None
            self.top1 = self.top1 - 1  # moves the top pointer down one to the next non-None value
            return transferValue
        elif stackNum == 2:
            poppedValue = self.popStack[self.top2]  # stores the value on the top of PopQueue
            self.popStack[self.top2] = None  # changes it to None
            self.top2 = self.top2 - 1  # moves the top pointer down one to the next non-None value
            return poppedValue
        else:
            print("Invalid Stack Number")
            return None


    def enqueue(self, item):
        self.push(1, item)

    def dequeue(self):
        '''
        # Scenarios: A) StackQueue has elements and PopStack has none so then transfer of elements occurs and pops the
        top of PopStack

        B) PopStack has an element

        C) StackQueue does not have an element and Pop Stack does not have an element

        '''
        if self.top1 != -1:
                while self.queueStack[self.top1] != None:  # this condition would represent that all the values in
                    # StackQueue are None
                    self.push(2, self.pop(1))  # the second parameter calls the pop function which will return the
                    # popped
                # value while keeping the array size of the stacks the same
                poppedValue = self.pop(2)  # will return the top of stack 2
                while self.popStack[self.top2] != None:
                    # then all the values are going to transferred back to queue stack
                    self.push(1, self.pop(2))
                return poppedValue
        else:
            print("No values in queue")
            return None # if no values in queue stack then there are no elements

# NOTE: Because I am importing the Queue class the test functionality in Lab01Queue gets carried over but that can be
# removed if you comment out the last two lines of Lab01Queue

class Customer():
    def __init__(self, name):
        '''

        :param name: The name of the customer will be make the customer unique
        The function also assigns the customer a random patience level
        '''
        self.patience = random.randrange(1, 10) # each Customer object will have a random patience
        self.name = name # each customer will also have an Id as a unique indentifier
        self.inQueueStatus = True # all customers are placed in the queue



class CustomerLine(Queue):

    def __init__(self):
        '''
        Creates three customer objects and adds them to the queue and also starts the score and time
        '''
        self.line = Lab01Queue.Queue(3)
        self.Customer1 = Customer("Bob") # hard code three customer objects with a unique id
        self.Customer2 = Customer("Simon")
        self.Customer3 = Customer("Katie")
        self.line.enqueue(self.Customer1) # add all customers to the queue
        self.line.enqueue(self.Customer2)
        self.line.enqueue(self.Customer3)
        self.score = 0 # to tabulate how well the user is doing in managing customers
        self.programStartTime = time.time() # when the program started and so elapsed time can be calculated

        self.projectionCustomers() # starts the projection of the UI

    def projectionCustomers(self):
        '''

        :return: As long as the queue exists then a customer will be taken out of the queue and if the customer has
        a current patience greater than 0 then the user can interact with the customer
        '''

        while (self.line.length() > 0):
            currentCustomerObject = self.line.dequeue()
            pastPatience = currentCustomerObject.patience
            customerCurrentPatience = pastPatience - ((time.time() - self.programStartTime)/10)
            customerCurrentPatience = round(customerCurrentPatience, 2)
            if customerCurrentPatience <= 0:  # if the customer has lower than 0 patience then they will leave
                print("A customer has filed a complaint against your restaurant and stormed off!")
                currentCustomerObject.inQueueStatus = False
                self.customerQuit()
            else:
                print(str(currentCustomerObject.name) + " is waiting with patience: " + str(customerCurrentPatience))
                print("(1) Seat customer")
                print("(2) Wait")
                print("(3) Quit")
                decision = int(input("Action (1,2,3): "))
                self.decisionTree(decision, currentCustomerObject)
            print("Waiting for next checkpoint...")
            time.sleep(5)

        if self.line.length() == 0: # if length of queue is 0 then game is over
            print("There are no more customers in line")
            print("Your score was: " + str(self.score))

    def customerQuit(self):
        '''

        :return: decreases the score if a customer leaves
        '''
        self.score = self.score - 1

    def customerSeated(self, customer):
        '''

        :param customer: The customer will be seated and the score will increase
        :return: The score will increase by 1
        '''
        print(customer.name + " was seated. Score will increase by 1")
        self.score = self.score + 1


    def decisionTree(self, decision, customer):
        '''
        :param decision: The decision is decided by the user and if it is one the customer is seated. If is two the
        customer is added back into the line. If the customer presses 3 then the game is over
        :param customer: The customer object is the current customer being served
        :return: It will call the customerSeated function or will simply add the customer to the back of the line or
        quit the program
        '''
        if decision == 1:
            customer.inQueueStatus = False
            self.customerSeated(customer) # if customer was seated and had positive patience then one point added to score

        elif decision == 2:
            self.line.enqueue(customer) # customer will be placed at the end of the line

        elif decision == 3:
            print("You quit your job! Better luck next time")
            exit(1)



customerLine = CustomerLine()

