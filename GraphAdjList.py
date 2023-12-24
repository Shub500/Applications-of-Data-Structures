'''
Name: Shubham Mohole
Program: The main idea behind the graph implementation is that we use a dictionary where the keys are all the vertices of the
graph and the values for each key are the adjacent vertices linked lists. We import the Lab01DLLArray to help create
those linked lists for each vertex. We assume that each linked list has a maximum adjaceny list of 50. For each operation
on the graph we make sure to check if the vertex even exists and then proceed to either add, delete, or search for a edge.

'''


import Lab01DLLArray

class GraphAdjList:
    def __init__(self):
        self.verticesAdjacencyList = {} # create a dictionary so we can have the keys as the vertices and the values as
        # being linked lists

    def addVertex(self, vertex):
        self.verticesAdjacencyList[vertex] = Lab01DLLArray.DLLArray(50) # we assume that the maximum vertices we hold is 50
        # so that is what we intialize our linked lists to be

    def addEdge(self, u, v):
        '''

        :param u: one of the vertices ( is this type Node?? )
        :param v: one of the other vertices
        :return: each vertex points to the other
        '''
        if u not in self.verticesAdjacencyList.keys(): # if the vertex does not exist then we print an error statement
            self.addVertex(u)
        elif v not in self.verticesAdjacencyList.keys():
            self.addVertex(v)
        else: # if the vertex does exist then we need to set that vertex to have its next pointer to the other vertex
            # and the other way around
            self.verticesAdjacencyList[u].insert(v)

    def deleteEdge(self, u, v):
        '''

        :param u: one of the vertices
        :param v: one of the other vertices
        :return: the connection between the vertex is broken
        '''
        if u not in self.verticesAdjacencyList.keys():  # if the vertex does not exist then we print an error statement
            print("Vertex" + u + "does not exist")
        elif v not in self.verticesAdjacencyList.keys():
            print("Vertex" + u + "does not exist")
        else:
            if v in self.verticesAdjacencyList[u].storageArray:
                self.verticesAdjacencyList[u].delete(v) # removes the nodes from each of the graph lists
                self.verticesAdjacencyList[v].delete(u)
                # if there are no neighbors for either of the vertices we would then delete the key from the dictionary

                if len(self.getNeighbors(u)) == 0:
                    del self.verticesAdjacencyList[u]
                if len(self.getNeighbors(v)) == 0:
                    del self.verticesAdjacencyList[v]
            else:
                print("There is no connection between those two vertices")


    def getNeighbors(self, u):
        # print only the vertices and right now it is printing out the entire array
        if u not in self.verticesAdjacencyList.keys():  # if the vertex does not exist then we print an error statement
            print("Vertex" + u + "does not exist")
        else:
            list = self.verticesAdjacencyList[u].storageArray # gets the list of adjacent values
            listofAdjacentNodes = []
            for element in list:
                if element in self.verticesAdjacencyList.keys(): # as long the elements are the keys and not the pointers
                    # we just add that to the neighbors list
                    listofAdjacentNodes.append(element)
            return listofAdjacentNodes

    def isAdjacent(self, u, v):
        if self.verticesAdjacencyList[u].search(v) is not None: # a search will return the index in the list of the vertex
            # and if it exists we return True
            return True
        else:
            return False

def TestDrive():
    test = GraphAdjList()
    test.addVertex("A")
    test.addVertex("B")
    test.addVertex("C")
    test.addVertex("D")
    test.addEdge("A", "B")
    test.addEdge("A", "C")
    print(test.getNeighbors("A"))
    test.deleteEdge("A", "C")
    print(test.getNeighbors("A"))
    print(test.isAdjacent("A", "B"))
    print(test.isAdjacent("A", "C"))





