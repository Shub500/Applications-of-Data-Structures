from graphics import *
class Button:

    def __init__(self, win, center, width, height, color, label):

        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label

        # if there is a piece on the Button
        self.hasPiece = None

        # make lower left & upper right points of Rectangle, then construct it
        self.ptll = Point((center.getX() - self.width / 2), (center.getY() + self.height / 2))
        self.ptur = Point((center.getX() + self.width / 2), (center.getY() - self.height / 2))

        self.button_rectangle = Rectangle(self.ptll, self.ptur)
        self.button_rectangle.draw(win)
        self.button_rectangle.setFill(color)

        # make text on Button
        self.button_label = Text(self.center, self.label)
        self.button_label.draw(win)

        self.deactivate()

    def highlight(self):
        self.button_rectangle.setFill('LightGoldenrod1')

    def unhighlight(self):
        self.button_rectangle.setFill('gray75')

    def getCenter(self):
        return self.center

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
        Parameters: newText (string)
        Changes the label on the button to newText.
        """

        self.label = newLabel
        if isinstance(newLabel, str) == True:
            self.button_label.undraw()
            self.button_label = Text(self.center, self.label)
            self.button_label.draw(self.win)
        else:  # label is a Circle object
            self.button_label.undraw()
            self.button_label = self.label
            self.button_label.draw(self.win)

    def clicked(self, pt):

        """
        Parameters: pt (Point)
        Returns True if the button is active & pt is on the button; False otherwise.
        """

        return (self.active == True and
                self.ptll.getX() <= pt.getX() <= self.ptur.getX() and
                self.ptur.getY() <= pt.getY() <= self.ptll.getY())

    def draw(self):

        """
        Draws the button (to be used after an undraw())
        """
        self.button_rectangle.draw(self.win)
        self.button_label.draw(self.win)

    def undraw(self):

        """
        Undraws the button from the graphics window.
        """

        self.button_rectangle.undraw()
        self.button_label.undraw()
