import random
import Lab08MazeGraphics



class CellNode():
    def __init__(self, x, y, maze):

        self.i = x
        self.j = y
        self.previousCell = None

        self.maze = maze
        # is
        if x % 2 == 1 and y % 2 == 1:
            self.type = "room"
            self.visitedRoomList = [False, False, False, False, False]
            # so the the 0 index = the source room, 1 index = top room, 2 index = bottom room, 3 index = right room
            # 4 index = left room
        else:
            self.type = "corridor"
            self.walkable = None


    def assignNeighRooms(self):
        if self.isIndexPossible(self.i - 2, self.j):
            self.topRoom = self.maze[self.i - 2][self.j]
        else:
            self.topRoom = False
        # both bottom and right rooms are not being created since they are pointing to none even though
        # there are cells

        if self.isIndexPossible(self.i + 2, self.j):
            self.bottomRoom = self.maze[self.i + 2][self.j]
        else:
            self.bottomRoom = False

        if self.isIndexPossible(self.i, self.j + 2):
            self.rightRoom = self.maze[self.i][self.j + 2]
        else:
            self.rightRoom = False

        if self.isIndexPossible(self.i, self.j - 2):
            self.leftRoom = self.maze[self.i][self.j - 2]
        else:
            self.leftRoom = False

    def isIndexPossible(self, x, y):
        if x > len(self.maze) - 1 or y > len(self.maze[x]) - 1 or x < 0 or y < 0:
            return False
        else:
            return True



    def getPossibleNeighbor(self):
        '''

        :param sourceRoom: type Cell Node that will have the x and y coordinates
        :return: returns a room that we will walk to
        '''

        movableAdjacentCells = []

        # the idea is that we check if the room exists and if it is not visited then we add to the possible neighbors

        if self.topRoom != False and self.visitedRoomList[1] == False and self.maze[self.i - 1][self.j].walkable != False:
                pair = []
                pair.append(self.topRoom)
                pair.append("top")
                pair.append(self.i - 1)
                pair.append(self.j)
                movableAdjacentCells.append(pair)

        if self.bottomRoom != False and self.visitedRoomList[2] == False and self.maze[self.i + 1][self.j].walkable != False:
                pair = []
                pair.append(self.bottomRoom)
                pair.append("bottom")
                pair.append(self.i + 1)
                pair.append(self.j)
                movableAdjacentCells.append(pair)


        if self.rightRoom != False and self.visitedRoomList[3] == False and self.maze[self.i][self.j + 1].walkable != False:
                pair = []
                pair.append(self.rightRoom)
                pair.append("right")
                pair.append(self.i)
                pair.append(self.j + 1)
                movableAdjacentCells.append(pair)

        if  self.leftRoom != False and self.visitedRoomList[4] == False and self.maze[self.i][self.j - 1].walkable != False:
                pair = []
                pair.append(self.leftRoom)
                pair.append("left")
                pair.append(self.i)
                pair.append(self.j - 1)
                movableAdjacentCells.append(pair)

        if len(movableAdjacentCells) == 0:
                return -1
        else:
                randomIndex = random.randint(0, len(movableAdjacentCells)-1)
                return movableAdjacentCells[randomIndex]
        # will return three elements 1) the neighbor cell and the coordinates for the corridor cell being moved through
        # works

    def getNPWCorridors(self, visitedRooms):
        '''

        :param sourceRoom: for all the rooms that have been visited we are going add their leading corridor to a
        list in which we will mark them as walls
        :return:
        '''

        corridorCellWallList = []

        if self.topRoom:
            if visitedRooms[self.topRoom] == True and self.maze[self.i - 1][self.j].walkable == None:
                self.maze[self.i - 1][self.j].walkable = False
                #wallIndxI = self.i - 1
                #wallIndxJ = self.j
                #leftNodeOfWall =
                #topNodeOfWall =
                #bottomNodeOfWall
                #rightNodeOfWall =

                #if(leftNodeOfWall != NONE)
                   # print (leftNodeOfWall)

                print("Wall Created:" + str(self.i-1) + " " + str(
                    self.j))

        if self.bottomRoom:
            if visitedRooms[self.bottomRoom] == True and self.maze[self.i + 1][self.j].walkable == None:
                self.maze[self.i + 1][self.j].walkable = False
                print("Wall Created:" + str(self.i+1) + " " + str(
                    self.j))

        if self.rightRoom:
            if visitedRooms[self.rightRoom] == True and self.maze[self.i][self.j + 1].walkable == None:
                self.maze[self.i][self.j + 1].walkable = False
                print("Wall Created:" + str(self.i) + " " + str(
                    self.j+1))

        if self.leftRoom:
            if visitedRooms[self.leftRoom] == True and self.maze[self.i][self.j - 1].walkable == None:
                self.maze[self.i][self.j - 1].walkable = False
                print("Wall Created:" + str(self.i) + " " + str(
                    self.j-1))

        # returns the corridor cells that are going to be marked as walls



class Maze():
    def __init__(self, length, width):
        self.mazeMatrix = [[None] * (2*length+1) for i in range(2*width + 1)]
        self.currentCell = None
        self.end = None
        self.visitedCells = {}
        #self.stack = []

    def fillMaze(self):
        for r in range(len(self.mazeMatrix)):
            for c in range(len(self.mazeMatrix[r])):
                    newCell = CellNode(r, c, None)
                    self.mazeMatrix[r][c] = newCell
                    self.visitedCells[self.mazeMatrix[r][c]] = False

        self.currentCell = self.mazeMatrix[1][1]

        for r in range(len(self.mazeMatrix)):
            for c in range(len(self.mazeMatrix[r])):
                self.mazeMatrix[r][c].maze = self.mazeMatrix
                self.mazeMatrix[r][c].assignNeighRooms()

        #self.stack.append(self.currentCell)

        if len(self.mazeMatrix) % 2 == 0:
            if len(self.mazeMatrix[0]) % 2 == 0:
                end = self.mazeMatrix[len(self.mazeMatrix)-1][len(self.mazeMatrix[0])-1]
            else:
                end = self.mazeMatrix[len(self.mazeMatrix) - 1][len(self.mazeMatrix[0]) - 2]
        else:
            if len(self.mazeMatrix[0]) % 2 == 0:
                end = self.mazeMatrix[len(self.mazeMatrix)- 2][len(self.mazeMatrix[0]) -1 ]
            else:
                end = self.mazeMatrix[len(self.mazeMatrix) - 2][len(self.mazeMatrix[0]) - 2]

            self.end = end
            self.moveCellDFS()


    def moveCellDFS(self):
        sourceCell = self.currentCell
        print("------")
        print("Current Cell:" + str(self.currentCell.i) + " " + str(self.currentCell.j))
        print("------")
        sourceCell.visitedRoomList[0] = True
        self.visitedCells[sourceCell] = True

        nextInfo = sourceCell.getPossibleNeighbor()

        if nextInfo == -1:
            self.currentCell = sourceCell.previousCell
            if self.currentCell == None:
                self.printMaze()
                exit(1)

        else:
            nextRoom = nextInfo[0]
            nextRoom.previousCell = sourceCell
            print("Next Cell:" + str(nextRoom.i) + " " + str(nextRoom.j))
            print("------")
            if nextInfo[1] == "top":
                sourceCell.visitedRoomList[1] = True
                nextRoom.visitedRoomList[2] = True
            elif nextInfo[1] == "bottom":
                sourceCell.visitedRoomList[2] = True
                nextRoom.visitedRoomList[1] = True
            elif nextInfo[1] == "right":
                sourceCell.visitedRoomList[3] = True
                nextRoom.visitedRoomList[4] = True
            elif nextInfo[1] == "left":
                sourceCell.visitedRoomList[4] = True
                nextRoom.visitedRoomList[3] = True

            corridorBetweenRoom = self.mazeMatrix[nextInfo[2]][nextInfo[3]]
            corridorBetweenRoom.walkable = True
            print("Corridor Between Current and Next:" + str(corridorBetweenRoom.i) + " " + str(corridorBetweenRoom.j))


            nextRoom.getNPWCorridors(self.visitedCells)


            self.currentCell = nextRoom


        self.moveCellDFS()


# at each cell we check if it has a visited neighbor (through a global list) and the corridor is None mark it as False



    def printMaze(self):
        for row in self.mazeMatrix:
            for element in row:
                if element.type == "corridor":
                    if element.walkable == False or element.walkable == None:
                        print("|", end=" ")
                    else:
                        print("-", end=" ")
                else:
                    print("*", end=" ")
            print()

        maze = Lab08MazeGraphics.MazeGUI(len(self.mazeMatrix), len(self.mazeMatrix[0]))
        for row in range(len(self.mazeMatrix)):
            for col in range(len(self.mazeMatrix[row])):

                # values are cellNodes, rooms are self.type = 'room'
                # walls are self.type = 'corridor', self.walkable

                if self.mazeMatrix[row][col].type == "corridor":
                    if self.mazeMatrix[row][col].walkable == False or self.mazeMatrix[row][col].walkable == None:
                        maze.fillCell(row, col, 'red')
                    else:
                        maze.fillCell(row, col, 'green')
                else:
                    maze.fillCell(row, col, 'green')

        maze.window.getMouse()






playGame = True

while playGame:

    N = input("Enter the length of the maze")
    M = input("Enter the width of the maze")

    Maze = Maze(N, M)

    gui.gameOver()
    pt = gui.getMouse()
    while True:
        if gui.quitClicked(pt) == True:
            gui.quitGame()
        elif gui.playAgainClicked(pt) == True:
            gui.reset()
            break
        else:
            pt = gui.getMouse()



