#
# Name: Marie-Anne
#
# Button: a Rectangle object with a Text object label displayed in a window;
# made clickable/unclickable with activate() and deactivate(), respectively
# actual parameters: win, center, width, height, label
# methods: activate, deactivate, getLabel, setLabel, clicked, undraw

from graphics import *

class Button:

    def __init__(self, win, center, width, height, color, label):

        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label

        # if there is a piece on the Button
        # self.hasPiece = None

        # make lower left & upper right points of Rectangle, then construct it
        self.ptll = Point((center.getX() - self.width/2), (center.getY() + self.height/2))
        self.ptur = Point((center.getX() + self.width/2), (center.getY() - self.height/2))

        self.button_rectangle = Rectangle(self.ptll, self.ptur)
        self.button_rectangle.draw(win)
        self.button_rectangle.setFill(color)

        # make text on Button
        self.button_label = Text(self.center, self.label)
        self.button_label.draw(win)
        
        self.activate()

        # 0 is 'white' in CLRS, 1 is 'gray', 2 is 'black'
        self.status = 0

    def setStatus(self):
        self.status += 1

    def checkStatus(self):
        return self.status

    def highlight(self):
        self.button_rectangle.setFill('LightGoldenrod1')

    def unhighlight(self):
        self.button_rectangle.setFill('gray75')

    def getCenter(self):
        return self.center

    def isActive(self):
        return self.active

    def activate(self):
        """
        Sets the button to 'active' (clickable).
        """
        self.button_rectangle.setFill("white")
        self.button_rectangle.setWidth(3)
        self.active = True

    def deactivate(self):
        """
        Sets the button to 'not active' (clicks have no effect on the program).
        """
        self.button_rectangle.setFill("gray75")
        self.button_rectangle.setWidth(1)
        self.active = False


    def getLabel(self):
        """
        Returns the current button label.
        """
        return self.label

    def setLabel(self, newLabel):
        """
        Parameters: newLabel (int)
        Changes the label on the button to newText.
        """

        self.button_label.setSize(24)
        self.button_label.setStyle('bold')

        if newLabel == 0:
            self.button_label.setText('')

        elif newLabel == 1:
            self.button_label.setText('1')
            self.button_label.setFill('blue')

        elif newLabel == 2:
            self.button_label.setText('2')
            self.button_label.setFill('green')
        
        elif newLabel == 3:
            self.button_label.setText('3')
            self.button_label.setFill('red')

        elif newLabel == 4:
            self.button_label.setText('4')
            self.button_label.setFill('purple')

        elif newLabel == 5:
            self.button_label.setText('5')
            self.button_label.setFill('black')
        
        elif newLabel == 6:
            self.button_label.setText('6')
            self.button_label.setFill('orange')
    
        elif newLabel == -1:
            # TODO: change to mine icon
            self.button_label.setText('m')


    def clicked(self, pt):

        """
        Parameters: pt (Point)
        Returns True if the button is active & pt is on the button; False otherwise.
        """

        return (self.active == True and
                self.ptll.getX() <= pt.getX() <= self.ptur.getX() and
                self.ptur.getY() <= pt.getY() <= self.ptll.getY())


    def showClue(self, clue):
        """
        Draws the clue number on the button and deactivates the cell.
        """
        self.deactivate()
        self.setLabel(clue)

    def flag(self):
        self.deactivate()
        self.status = 2
        # self.button_label = Image(self.center, '/Users/marie-annexu/Desktop/ATCS/Lab08/flag.gif')
        self.button_label = Polygon(Point(self.center.getX() - 20, self.center.getY() - 20),
                                    Point(self.center.getX() - 20, self.center.getY() + 20),
                                    Point(self.center.getX() + 20, self.center.getY()))
        self.button_label.setFill('red')
        self.button_label.draw(self.win)

    def reset(self):
        self.button_label.undraw()
        self.button_label = Text(self.center, '')
        self.button_label.draw(self.win)
        self.activate()
