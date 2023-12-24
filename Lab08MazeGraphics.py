'''
Name: Written by Marie Anne
Program Description: We create a window that has two buttons: play again and quit. Moreover, on the window we print
the colored maze. When play again is pressed we create a new maze in a new window. When we press quit the windows close.
'''

from graphics import *
from Lab08MazeButton import Button


class MazeGUI:

    def __init__(self, column, rows):
        '''

        :param column: the width of the matrix
        :param rows: the height of the matrix
        '''
        # creates the window that will appropriatly hold the maze
        self.window = GraphWin("Maze", 25 * rows, 25 * column + 150)


        # creates a quit button, activates it so that the user can quit at any time
        self.quit = Button(self.window, Point(25 * column // 4, 75), 75, 50, 'white', 'Quit')
        self.quit.activate()

        # the play-again button is created
        self.newMaze = Button(self.window, Point(75 * column // 4, 75), 75, 50, 'white', 'New Maze')

    def getWin(self):
        return self.window

    def getMouse(self):
        return self.window.getMouse()

    def quitClicked(self, pt):
        """Returns whether or not the Quit button is clicked."""
        return self.quit.clicked(pt)

    def newMazeClicked(self, pt):
        """Returns whether or not the New Maze button is clicked."""
        return self.newMaze.clicked(pt)

    def quitWindow(self):
        """Quits the program, closes the window."""
        self.window.close()
        sys.exit()

    def fillCell(self, row, col, color):
        # we fill cell with either green or red with green as a room or possible pathway as well as red for the walls
        square = Rectangle(Point(col * 25, row * 25 + 150), Point((col + 1) * 25, (row + 1) * 25 + 150))
        square.setFill(color)
        square.draw(self.window)