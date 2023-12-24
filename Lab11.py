'''
Name: Shubham Mohole
Program Description:
We have a graph class that will store the number of vertices, the actual adjacency matrix,
and three important data structure, which are the current weight of the vertices, a list that
stores where a node has been already added to the MST and finally a dictionary that stores the actual MST
We want to do a cut for each vertex with respect to the rest of the graph so we will have
one overarching loop to iterate through all vertices. In each iteration we want to find
which vertex is the minimum vertex (the vertex that has the least weight currently)
so that we are continuing the path with the minimum edges. This will require a for loop.
 Once we have this vertex we put it into the MST. We then have another for loop to explore
 the adjacent vertices. We go through each element in the row and see if there is a non-zero value
 which will represent if there is an edge and the weight of the edge. For each of these adjacent vertices
 we will update their node weights, if the path we are going through is more optimal than the current path,
 and we update the MST.
'''



import math


class Graph:
    def __init__(self, graph):
        self.length = len(graph) # we keep track of the length of the graph so that
        # we know how many vertices there are
        self.adjMatrix = graph # we have the actual adj Matrix
        self.MST = {} # stores the actual min spanning tree
        self.MST[0] = 0 # will set the first one to 0 because we will start from the 0 index
        self.weightofNodes = [math.inf] * self.length  # this will store the weight of the nodes
        # which is the equivalent of the keys of each node
        self.weightofNodes[0] = 0
        # we will set first one to 0 because again we are starting from 0 index
        self.visitedMST =(1, G.length [False] * self.length # will store the vertices already in the MST
        # which is the equivalent of the keys of each node


def PrimMST(G):
    G = Graph(G) # create a graph from the matrix given
    MSTsum = 0 # the sum of the MST
    for i in range(G.length): # we want our MST to have all vertices as per the definition so we
        # will be iterating through all vertices and their adjacency nodes to make sure that the weights are minimized
        min = math.inf # we set the min weight to be infinite
        for j in range(G.length):  # extracts the min vertex to branch our tree from
            if G.weightofNodes[j] < min and G.visitedMST[j] == False:
                # each time, if our current vertex has a smaller weight than that of min then
                # we update min and set the vertex that we start and do a cut of to u
                min = G.weightofNodes[j]
                u = j
        G.visitedMST[u] = True # now we have found the min vertex in the graph
        # so we add into our MST and label as visited
        for v in range(G.length):
            # now we will do our "cut"
            # if there exists an edge and the destination vertex is
            # not a vertex in the same set as u (i.e is not part of the MST)
            # and the current weight of that edge is larger than the edge we go through then we update
            # the weight
            # as we go through the adjacency matrix we might have edges that are self edges (i.e (u,u) )
            # but for MST we would never go through this edge as we want to explore unvisited nodes
            if u != v and G.adjMatrix[u][v] > 0 and G.visitedMST[v] == False\
                    and G.weightofNodes[v] > G.adjMatrix[u][v]:
                    weight = G.adjMatrix[u][v]
                    G.weightofNodes[v] = weight # update the current weight of the vertex
                    # this is important because we could find a better route that leads to a better weight
                    G.MST[v] = [ [u,v], weight]
                    # similar logic as above we keep overwriting what the previous spanning tree was since we have found
                    # a better edge that could lead to the MST

    print("Edge \t Weight")
    for i in range):
        # we start at 1 because at 0 index there is nothing since we start at 0
        print("(" + str(G.MST[i][0]) + ")", "\t", G.MST[i][1])
        # we print the edge pair and the weight
        MSTsum = MSTsum + G.MST[i][1]
        # we add the weights to get the total sum
    print("MST Weight: " + str(MSTsum))



graph = [[0, 3, 5, 0, 0, 0],
         [3, 0, 0, 6, 7, 0],
         [5, 0, 0, 4, 5, 0],
        [0, 6, 4, 0, 0, 3],
        [0, 7, 5, 0, 0, 2],
         [0, 0, 0, 3, 2, 0] ]


PrimMST(graph)



