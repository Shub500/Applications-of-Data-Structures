'''
Name: Shubham Mohole
Code Description: Exercise 1: Get a random x,y coordinate pair for a Node object. Then add the Node into our graph adjacency
list which is a dictionary where the keys are vertices and the values are the adjacent nodes. Then we check the distance
of this node to all other nodes using Pythag and then add the edge is it is less than the distance parameter. Then we draw
the graph with drawing ovals for vertices and lines between ovals which are our edges. Exercise 2: We use a standard Dijkstra's
algorithm but just modify the relax function with three cases and each Node object has two attributes: the miles travelled and the day number.
Then we do Dijkstra's just trying to the get the smallest day value. Exercise 4: The iterative deepening piece of it is just doing a binary search on
the upper and lower bound as keep checking if a path exists. The check path uses DFS and keeps searching until target is reached
and checks if we are still less than L. Returns true if it finds the target in the depth or False.
'''
from GraphAdjList import *
import random
from graphics import *
import math


# ===== Exercise 1 ======
class Node:
    def __init__(self,x,y):
        '''
        This class of nodes will be used in the functions below
        :param x: the x cordinate of the node in an x-y plane
        :param y: the y cordinate of the node in an x-y plane
        '''
        self.x = x
        self.y = y
        self.cordsList = [self.x, self,y] # the cord list to be accessed
        self.hasNeighbors = True
        self.d = 0 # the day number going from v.p
        self.p = None # the predecessor node
        self.c = 0 # the miles that have been travelled


def randGeoGraph(A,B,N,D):
    '''

    :param A: The UB of the x cord
    :param B: The UB of the y cord
    :param N: the number of the nodes that will be created
    :param D: if the the distance between two nodes is less or equal than D then we have a edge
    :return: it will return a list of all vertices, and the adjacency list that has all the edge connections
    '''
    if type(A) != int or A < 0 or type(B) != int or B < 0 or type(N) != int or type(D) != int or D < 0:
        return "Invalid Input: Please check that A, B, N, and D are intergers and postive numbers"

    graph = GraphAdjList()
    allVertices = [] # intialize two arrays that will store a) the list of vertices b) a list that contains a sub list that
    # holds an edge in a form of [A,B]
    vertexDictionary = {}
    allEdges = []
    for i in range(N):
        randomX = random.randint(0,A) # get random x cord
        randomY = random.randint(0,B) # get random y cord
        newVertex = Node(randomX, randomY) # create a Node object based on the cords


        while (str(randomX)+"a"+str(randomY) in vertexDictionary.keys()): # this is to make sure we do not get duplicate vertices
            randomX = random.randint(0, A)
            randomY = random.randint(0, B)
            newVertex = Node(randomX, randomY)


        allVertices.append([newVertex, newVertex.x, newVertex.y]) # add the vertex node and its x,y cords into the vertex list
        vertexDictionary[str(randomX)+"a"+str(randomY)] = "exists"
        graph.addVertex(newVertex) # in our adjacency list we are going to add this vertex node
        for i in range(len(allVertices)-1): # looking at all previous vertices just not the latest addition
            distance = math.sqrt((allVertices[len(allVertices)-1][1] - allVertices[i][1]) ** 2 + (allVertices[len(allVertices)-1][2] - allVertices[i][2])**2)
            # uses Pythag to calculate the distance from the vertex to vertex
            if distance <= D:
                graph.addEdge(allVertices[i][0], allVertices[len(allVertices)-1][0]) # if under the D, then we will add the edge
                allEdges.append([allVertices[i][0], allVertices[len(allVertices)-1][0], distance]) # this edge will be add into our
                # all edges list
    for vertex in allVertices:
        if len(graph.getNeighbors(vertex[0])) == 0: # for Question 2 we do not want our start node or target node to be an island node
            # so we mark any nodes that do not have any edges
            vertex[0].hasNeighbors = False
    return allVertices, graph.verticesAdjacencyList # return a list of vertices and an adjacency dictionary


def drawGraph(V,E):
    '''

    :param V: will take in the list of vertices
    :param E: will take in edge list
    :return: show a graph
    '''
    window = GraphWin("Maze", 800, 800) # creates a window
    vertexList = V
    for i in range(len(vertexList)): # will go through the list and scale the vertex cords and have the vertex as an circle
        vertex = Circle(Point(vertexList[i][1] * 15, vertexList[i][2] * 15), 5)
        vertex.draw(window) # will draw the circle in the window
        list = E[vertexList[i][0]].storageArray  # gets the list of adjacent values
        listofAdjacentNodes = []
        for element in list:
            if element in E.keys():  # as long the elements are the keys and not the pointers
                # we just add that to the neighbors list
                listofAdjacentNodes.append(element)
        for element in listofAdjacentNodes:
            line = Line(Point(vertexList[i][0].x * 15, vertexList[i][0].y * 15), Point(element.x * 15, element.y * 15))
            line.draw(window) # will draw the line between the two points
    window.getMouse()
    window.close()



# ===== Exercise 2 ======

class minQueueCreate():
    def __init__(self):
        self.minQueue = [] # intialize a queue that when we pop will take out the min
    def add(self, item):
        self.minQueue.append(item)
    def extractMin(self):
        minD = math.inf # since in our algorithim we are comparing both the days and the distance travelled depeding
        # on the situation we also want to that into consideration when extracting a node.
        # There are two cases: 1) the day is the smallest where in then we would just pick that node to be u
                    # 2) where there are multiple nodes with the same smallest days then we would compare the distances
                        # travelled
        minC = math.inf
        index = 0
        for i in range(len(self.minQueue)):
            if self.minQueue[i].d <= minD: # if the day number is smaller than current min then update min's reference to
                # vertex object
                if self.minQueue[i].d == minD:
                    if self.minQueue[i].c < minC: # this reflects Case 2
                        minC = self.minQueue[i].c
                        index = i
                else:
                    minD = self.minQueue[i].d # this reflects Case 1
                    minC = self.minQueue[i].c
                    index = i
        vertex = self.minQueue[index]
        if vertex.d == math.inf: # if all vertices are inf then we know none of the following vertices are reachable from the
            # the start
            return None
        else:
            self.minQueue.remove(vertex) # if we do find a valid vertex, we remove it and return it
            return vertex

def relax(u,v,w,D):
    '''

    :param u: the source vertex
    :param v: the end vertex
    :param w: the weight between the vertices
    :param D: the miles that can be travelled in a day
    :return: will update the v.c, u.c, v.d, or u.d
    '''
    if u.d > v.d: # if the destination is reached by a better path then do nothing
        pass
    elif u.d == v.d: # if the day is the same at the destination then we could still get a more optimal result as the miles travelled can be
        # minimized.
        if u.c + w < D and u.c + w < v.c: # as long as the w(u,v) + the current miles driven is less than D and less than
            # v.c we will update since we want to able to drive further and having less current miles driven is better
            v.c = u.c + w
            v.p = u
    elif u.d < v.d: # if we are getting a better path in terms of days
        if u.c + w < D: # this means that we can still travel to this next vertex in the current day
            v.c = u.c + w
            v.d = u.d
            v.p = u
        if u.c + w == D: # this means we have reached the D limit so we travel and then will need to rest and we add a day
            v.c = 0
            v.d = u.d + 1
            v.p = u
        if u.c + w > D: # this means that the next leg of the journey is too long so we rest at the current vertex
            if(v.d == u.d + 1): # if the days are just one apart then in this condition we are just incrementing days
                # so we should also just minimize the miles travelled if possible
                if (w < v.c): # if the distance travelling from u to v after a rest at u (=w) is less than v.c then update
                   v.c = w
                   v.p = u
                else:
                    pass
            else:
                v.c = w # if we are a case where we have a comparison between 1 day and 3 day for example we would
                # have to go through (u,v) since then at worst we would have 2 days D-1 miles
                v.d = u.d + 1
                v.p = u    # set the previous to the source node


def roadtrip(V,E, start, target, D):
    '''

    :param V: from the graph created graph[0] will be referring to the list of vertices
    :param E: from the graph created graph[1] will be referring to a dictionary that contains the adjacency lists
    :param start: the start vertex will be the first vertex in the vertexList from graph[0]
    :param target: the target vertex will be a random vertex selected from graph[0]
    :param D: D will refer to maximum distance that can be travelled in a day
    :return:
    '''
    if D < 0:
        return "The limit of how many miles that can be driven in day cannot be negative"
    verticesList = V
    # we will have the first vertex be the start vertex so intialize all its instances to 0
    start[0].d = 0
    start[0].c = 0
    for vertex in verticesList[1:]: # for all other vertices we will have its distance as infinte and have no predeccesors
        vertex[0].d = math.inf
        vertex[0].c = math.inf
        vertex[0].p = None
    Q = minQueueCreate() # we create min-priority queue
    for i in range(len(verticesList)):
        Q.add(verticesList[i][0]) # we add all the vertices in that queue


    while len(Q.minQueue) != 0: # as long as our queue is not empty we will go through and relax all the neighboring edges
        # of u with the smallest distance from our start vertex
        u = Q.extractMin()
        if u == None:
            return "Unreachable Vertex"
        if u == target[0]: # to be efficient once we have extracted target due to the algorithim logic
            # the weight will not change so we have finished
            return u.d
        neighbors = []
        list = E[u].storageArray  # gets the list of adjacent values
        for element in list:
            if element in E.keys():  # as long the elements are the keys and not the pointers
                # we just add that to the neighbors list
                if element not in Q.minQueue: # if it has been already extracted we do not need to go through it again
                    pass

                else:
                    distance = math.sqrt((u.x - element.x) ** 2 + ( # because our adjacency list does not store the edge weight we will calculate it
                                u.y - element.y) ** 2)
                    if distance < D:
                        neighbors.append([element, distance]) # if the distance is > D then we do not want that edge
                        # since we will not be able to go through this path since our car will break down in the middle
                        # of it
        for i in range(len(neighbors)):
            relax(u,neighbors[i][0], neighbors[i][1], D) # call the relax function for all the neighbor vertices of u



# ===== Exercise 4 ======

class NodeID:
    def __init__(self,value):
        self.value = value
        self.visited = False
        self.p = None # the predecessor node

def createGraph(V,E):
    if len(V) == 0 or len(E) == 0:
        return "Invalid Input: Please enter some vertices and edges"
    graph = GraphAdjList()  # create graph adjacency list
    for i in range(len(V)):  # for each vertex we create a Node object and add the vertex
        newNode = NodeID(V[i])
        graph.addVertex(newNode)

    for connection in E:  # we check if the vertices are in the graph already and if not then we add the vertex to
        # the dictionary
        vertex1 = None
        vertex2 = None
        for node in graph.verticesAdjacencyList.keys(): # if the node is in the keys then we find corresponding Node object
            # using the string value we have
            if node.value == connection[0]:
                vertex1 = node
                break
        for node in graph.verticesAdjacencyList.keys():
            if node.value == connection[1] and node.value != connection[0]:
                vertex2 = node
                break
        graph.addEdge(vertex1, vertex2)  # we then add the connection between the vertices
    return V, graph.verticesAdjacencyList

def checkPath(V, E, S, T, L):
    currentVertex = None
    for node in E.keys(): # we get our start node by checking if the node has a value that is equal to S
        if node.value == S:
            currentVertex = node
            break
    if currentVertex.value == T: # if we have gotten to our target value and or L is positive we are good
        return True
    if L == 0: # if our L is 0 then we have not found a path that gets to T under L length
        return False
    neighborsList = [] # if neither case then we are going to go to another vertex
    list = E[currentVertex].storageArray  # gets the list of adjacent values
    for element in list:
        if element in E.keys():  # as long the elements are the keys and not the pointers
            # we just add that to the neighbors list
            neighborsList.append(element)
    for vertex in neighborsList: # for each vertex we are going to check if we can reach T under L length
        if checkPath(V,E,vertex.value,T,L-1): # if one of those paths returns True then we are good
            return True
    return False

possiblePath = 0

def iterativeDeepening(V,E,S,T,LB,UB):
    '''

    :param V: the list of vertices
    :param E: the list of edges
    :param S: the start vertex
    :param T: the target vertex
    :param LB: the LB of the shortest path
    :param UB: the UB of the longest path
    :return: will return the shortest path
    '''
    global possiblePath
    if (UB >= LB):  # our recursion will stop once when our LB is greater than UB since that means that a shorter path is not
        # within this section of the bounds so we will refer back to the most recent possible path made
        middle = (LB + UB)// 2 # since our LB and UB are going to be lower and higher respectively to the actual answer
        # we will just find the middle each time of those two bounds
        if checkPath(V, E, S, T, middle): # then with this middle you check if it works. If yes then we decrease middle
            # by making our UB = middle - 1 since we already checked middle
            possiblePath = middle
            iterativeDeepening(V, E, S, T, LB, middle - 1)
        else: # if not then we look at the higher segment from middle + 1 to UB
            iterativeDeepening(V, E, S, T, middle + 1, UB)
    return possiblePath
# Testing

#Exercise 1

# Note: If you test Exercise 1 then the only output is the drawn graph
graphInfo = randGeoGraph(50,50,50,13)
#drawGraph(graphInfo[0], graphInfo[1])


# Exercise 2

graph = randGeoGraph(50, 50, 50, 13)
start = graph[0][0] # the start will be the first vertex added
#counter1 = 0
#counter2 = 0
for i in range(10,50):
    target = graph[0][i] # the target will be a random index
    result = roadtrip(graph[0], graph[1], start, target, 20)
    #result2 = roadtrip(graph[0], graph[1], start, target, 50)
    if result != "Unreachable Vertex":
        #counter1 = counter1 + 1
        #print("Reachable target at index " + str(i))
        print(result)
    #if result2 != "Unreachable Vertex":
        #counter2 = counter2 + 1
        #print("Reachable target at index " + str(i))
        #print(result2)
#print(counter1)
#print(counter2)


# Exercise 4

# I decided to hardcode in vertices and a list of edges to test the function. However, in my createGraph helper I do use
# a list of vertices and a dictionary of vertices as keys and respective adjacency lists

V = ["A", "B", "C", "D", "E", "F"]
E = [["A", "B"], ["B", "C"], ["D", "B"], ["A", "C"], ["E", "C"], ["C", "D"], ["D", "E"], ["E", "F"]]
graph = createGraph(V,E)
print(checkPath(graph[0],graph[1],"A", "F", 3))
print(checkPath(graph[0],graph[1],"A", "F", 4))
print(iterativeDeepening(graph[0],graph[1], "A", "F", 1, 5))
print(iterativeDeepening(graph[0],graph[1], "A", "C", 1, 3))
print(iterativeDeepening(graph[0],graph[1], "A", "D", 1, 5))
print(iterativeDeepening(graph[0],graph[1], "A", "A", 0, 5))






