'''

Name: Shubham Mohole
Two classes are implemented: a Question class and the main game class. The question class will act as the nodes in
the BST. Each node will store the question as well as pointers to its left and right children and a pointer
back to the parent that lead to this node. If this question is a leaf that means this is a yes or no question
that either guesses the user's animal or leads to an update of the tree. In the main game class, we will just
go through all the Question objects, going to the right node if the response was Yes or to the left node if the
response was No until we reach a dead end (leaf node). If we guess the user animal (i.e the response to the leaf node
was yes then we win and allow the user to play again. If not we call the updateBST graph again. In the updateBST
method we essentially create two new questions: the new leaf node that is in the format of Is it --? and then
a distinguishing question as well as the response. We connect the leaf to the disting question based on if it is yes or
no and connect the previous leaf to the opposite side. We then make the disting question the child of the parent
that lead to the previous leaf.
'''


class Question:
    def __init__(self, type, question, yesNodeOption, noNodeOption, parent, object):
        '''

        :param type: the type of question
        :param question: question or key value of this node
        :param yesNodeOption: the pointer to the yes logic node
        :param noNodeOption: the pointer to the no logic node
        :param parent: the parent of the question
        :param object: if it is leaf the actual object
        '''
        self.type = type # the type of question
        self.question = question # question or key value of this node
        self.yesNode = yesNodeOption # the pointer to the yes logic node
        self.noNode = noNodeOption # the pointer to the no logic node
        self.parent = parent # the parent of the question
        self.object = object # if it is leaf the actual object

    def updateReferenceLeft(self, destNode):
        '''

        :param destNode: this new node will be the node that the current node will have its left pointer to
        :return: update left pointer
        '''
        self.noNode = destNode

    def updateReferenceRight(self, destNode):
        '''

        :param destNode: this new node will be the node that the current node will have its right pointer to
        :return: update right pointer
        '''
        self.yesNode = destNode

class TwentyQuestionBSTTree:
    def __init__(self):
        '''
        Starts the game
        '''
        # sets default a tree of height 1 with the root having two leaf nodes

        self.root = Question("question", "Is it bigger than a bread box?", None, None, None, None)
        noNode = Question("leaf", "Is it a mouse?", None, None, self.root, "mouse")
        self.root.updateReferenceLeft(noNode)
        yesNode = Question("leaf", "Is it a lion?", None, None, self.root, "lion")
        self.root.updateReferenceRight(yesNode)
        self.responses = {} # also store a set of responses so we can back track to make sure that
        # when we update the BST we have know which subtree and pointer we are coming from
        self.walkTree(self.root, None, None) # we call the walk tree to start playing the game

    def clearGame(self):
        '''
        resets the game to the original three node BST with height 1 and calls walk tree again to start
        playing
        '''
        self.root = Question("question", "Is it bigger than a bread box?", None, None, None, None)
        noNode = Question("leaf", "Is it a mouse?", None, None, self.root, "mouse")
        self.root.updateReferenceLeft(noNode)
        yesNode = Question("leaf", "Is it a lion?", None, None, self.root, "lion")
        self.root.updateReferenceRight(yesNode)
        self.walkTree(self.root, None, None)


    def walkTree(self, node, previousNode, previousResponse):
        '''

        :param node: the current node we are at
        :param previousNode: the parent of the current node
        :param previousResponse: the response that lead us from parent to current
        :return:
        '''
        if node != None: # if the node exists (i.e our base case and ensurer that we have not passed a leaf node)
            print(node.question) # we print the question
            # and then they reponse Yes or No
            # if yes the we go to the yes node pointer (i.e the right subtree and continue our recurisve call)
            # if no then we go the no node pointer (i.e the left subtree)
            response = input("Yes or No:")
            self.responses[node] = response
            if response == "Yes":
                self.walkTree(node.yesNode, node, "Yes")
            elif response == "No":
                self.walkTree(node.noNode, node, "No")
            else:
                print("Invalid input")
                self.clearGame()
        else:
            # if we have finished going through a path from the root to a certain leaf node
            # and our response to that leaf node was NO that means we have did not guess the animal
            # and so we must update the tree
            if previousResponse == "No":
                print("Oh no, I couldn't get it!")
                self.updateTree(previousNode, self.responses[previousNode.parent])
                self.walkTree(self.root, None, None)
            elif previousResponse == "Yes":
                # if have guessed the animal then we are done and we ask the user
                # if they want to play again. If yes then clear the game to default and play, if not then exit
                print("Yay I have guessed your object!")
                gameAgain = input("Do you want to play again?")
                if gameAgain == "Yes":
                    self.clearGame()
                elif gameAgain == "No":
                    print("Bye")
                    exit(1)
                else:
                    print("Invalid input") # input checks
                    self.clearGame()
            else:
                print("Invalid input")
                self.clearGame()


    def updateTree(self, nodeToUpdate, previousResponse):
        '''

        :param nodeToUpdate: the leaf node that will be moved
        :param previousResponse: the response will help us in knowing how we got from the parent to the leaf
        so that we can put the disting question in between the two
        :return:
        '''
        newObject = input("What were you thinking?")
        newQuestion = input("What is a yes/no question that distinguishes it from " + nodeToUpdate.object + "?")
        decision = input("Is yes or no the correct answer to get to the " + newObject + "?")
        # the three inputs give us the new leaf node question, the disting question, and how to get from
        # the disting question to the new leaf nodee question

        newParentNode = Question("question", newQuestion, None, None, nodeToUpdate.parent, None)
        # create new question (disting question) object with reference to the parent of the previous

        if previousResponse == "Yes":
            nodeToUpdate.parent.updateReferenceRight(newParentNode)
            # if we came from the right subtree of the parent then we insert the disting question in the right
            # subtree
        elif previousResponse == "No":
            nodeToUpdate.parent.updateReferenceLeft(newParentNode)
            # if we came from the left subtree of the parent then we insert the disting question in the left
            # subtree
        nodeToUpdate.parent = newParentNode
        # now the previous leaf node will have its reference as the disting question
        if decision == "Yes":
            # if to get from disting to new animal is yes then we have the prev leaf as a left node
            # of disting question and the right will be the new leaf node
            newParentNode.updateReferenceLeft(nodeToUpdate)
            newObjectNode = Question("leaf", "Is it a " + newObject, None, None, newParentNode, newObject)
            newParentNode.updateReferenceRight(newObjectNode)
        elif decision == "No":
            # if to get from disting to new animal is no then we have the prev leaf as a right node
            # of disting question and the left will be the new leaf node
            newParentNode.updateReferenceRight(nodeToUpdate)
            newObjectNode = Question("leaf", "Is it a " + newObject, None, None, newParentNode, newObject)
            newParentNode.updateReferenceLeft(newObjectNode)
        else:
            print("Invalid Input")
            self.clearGame()

testGame = TwentyQuestionBSTTree()

