from OpenGL.GL import *
class Objects2D: # base class for 2D-objects
    def __init__(self, xPos, yPos, color):
        self.xPos = xPos # store center x-position
        self.yPos = yPos # store center y-position
        self.R, self.G, self.B = color # unfold color tuple
        self.alpha = 1 # set transparency to none
        self._edges = list() # create list for edges
        self._vertices = list() # create list for vertices
    def update(self): # update drawing of 2D-object
        glBegin(GL_LINES) # draw lines, only
        for edge in self._edges: # iterate all edges
            for vertex in edge: # iterate all vertices to draw
                glColor4f(self.R, self.G, self.B, self.alpha) # red,green,blue,alpha
                glVertex3fv(self._vertices[vertex])
        glEnd() # End of definition

class Square(Objects2D): # subclass to define 2D-squares
    def __init__(self, xPos = 0, yPos = 0, color = (1, 1, 1), size = 1):
        Objects2D.__init__(self, xPos, yPos, color) # call base class constructor
        self.__size = size # store size (for later use!?)
        dx = dy = size / 2 # to set square to the center
        self._vertices = [(xPos - dx, yPos - dy, 0), (xPos + dx, yPos - dy, 0),
        (xPos + dx, yPos + dy, 0), (xPos - dx, yPos + dy, 0)]
        self._edges = [(0, 1), (1, 2), (2, 3), (3, 0)]