'''
Name: Shubham Mohole
Program: We have a 2D array that increases in size depending on the vertices being added. The main assumption in the
implementation is that the indicies of our 2D array will represent the vertices. One improvement we could have done
was just when adding a non-integer vertex like a string we could just convert that into an integer, but since it would be
easier and more efficient to use integer vertices we will stick to that. Like the other implemenation of a graph, we
always make sure the vertex exists and if it does we add a 1 or a 0 in the respective position meaning if we add a
1 in cell (2,3) we know that there is an edge between 2 and 3. We would also do that for (3,2) because an edge goes
both ways. This applies to deleting since we would just add a 0. Searching is also just seeing if there is a 1 at a given
cell which would signify that there is a connection.
'''




class GraphAdjMatrix:
    def __init__(self, size = 0):
        '''

        :param size: creates a matrix of size 0 x 0
        '''
        self.adjMatrix = [[None] * size for i in range(size)] # creates the array of 0 x 0 to start
        self.size = size # this instance variable will update each time a vertex is added

    def add_vertex(self, u):
        '''

        :param u: the vertex being added
        :return: the size of the array increases to accomadate the vertex
        '''
        self.size = self.size + u
        newMatrix = [[0] * self.size for i in range(self.size)] # we create a new matrix of a size that will hold the new
        # matrix but we will need to copy over the previous matrix over so the data is preserved
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                newMatrix[i][j] = self.adjMatrix[i][j]
        self.adjMatrix = newMatrix

    def delete_vertex(self, u):
        self.size = self.size - 1 # when we delete a vertex our matrix is going to shrink
        newMatrix = [[0] * self.size for i in range(self.size)]
        # we do the same thing of copying the data but this time we need to offset how the data is being
        # added because we are deleting a row and column of elements
        rowCopyOffset = 0
        for i in range(len(self.adjMatrix)):
            columnCopyOffset = 0
            if i == u:
                rowCopyOffset = -1
                continue
            for j in range(len(self.adjMatrix[i])):
                if j == u:
                    columnCopyOffset = -1
                    continue
                newMatrix[i+rowCopyOffset][j+columnCopyOffset] = self.adjMatrix[i][j]
        self.adjMatrix = newMatrix

    def addEdge(self, u, v, weight):
        '''

        :param u: a vertex that may or may not be in the graph
        :param v: a vertex that may or may not be in the graph
        :return: if the vertices do not exist we size the 2D matrix to accomadate the vertices and then we add the edge
        '''
        if u-1 > len(self.adjMatrix): # if the 2D grid is too small then we add the vertices
            self.add_vertex(u)
        if v-1 > len(self.adjMatrix):
            self.add_vertex(v)
        self.adjMatrix[u-1][v-1] = weight  # we then add one's in the respective positons
        self.adjMatrix[v-1][u-1] = weight

    def deleteEdge(self, u, v):
        '''

        :param u: a vertex that may or may not be in the graph
        :param v: a vertex that may or may not be in the graph
        :return: will break the edge between u and v if they exist, if they dont then we return an error statement
        '''
        if u-1 > len(self.adjMatrix): # if the vertex is not found then we return error statement
            return "Vertex " + str(u) + " does not exist"
        if v-1 > len(self.adjMatrix):
            return "Vertex " + str(v) + " does not exist"
        self.adjMatrix[u-1][v-1] = 0 # set it to 0 to signify a deleted connection
        self.adjMatrix[v-1][u-1] = 0

        # these two sections check if the row of elements is all 0 because if they are this is just
        # an unconnected vertex so we would delete the vertex from the matrix
        vertexEdgeFoundU = False
        for element in self.adjMatrix[u]:
            if element == 1:
                vertexEdgeFoundU = True
        if vertexEdgeFoundU == False:
            self.delete_vertex(u-1)

        vertexEdgeFoundV = False
        for element in self.adjMatrix[v]:
            if element == 1:
                vertexEdgeFoundV = True
        if vertexEdgeFoundV == False:
            self.delete_vertex(v-1)


    def getNeighbors(self, u):
        '''

        :param u: the vertex for which we find the adjacent nodes
        :return: the list of vertices that are adjacent to the starting vertex
        '''
        if u-1 > len(self.adjMatrix): # if the vertex is not found then we return error statement
            return "Vertex " + str(u) + " does not exist"
        else:
            adjacencyList = []
            vertex = 1
            for element in self.adjMatrix[u-1]:
                if element == 1: # if the row has a 1 then we just check the index which represents the vertix at which it is adjacent
                    adjacencyList.append(vertex)
                vertex = vertex + 1
            return adjacencyList

    def isAdjacent(self, u, v):
        if self.adjMatrix[u-1][v-1] == 1:
            return True
        else:
            return False

    def getMatrix(self):
        '''

        :return: prints the matrix
        '''
        return self.adjMatrix

def TestDrive():
    test = GraphAdjMatrix()
    test.add_vertex(1)
    test.add_vertex(2)
    test.add_vertex(3)
    test.add_vertex(4)
    test.addEdge(1, 2, 5)
    test.addEdge(1, 3, 3)
    print(test.getNeighbors(1))
    test.deleteEdge(1,3)
    print(test.getNeighbors(1))
    print(test.isAdjacent(1,2))

TestDrive()


