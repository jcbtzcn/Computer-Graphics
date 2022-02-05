import operator
import numpy as np
from PIL import Image
from matrix import matrix

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    __moduleName__ = "graphicsWindow.py"
    __author__ = "Yakup Tezcan"
    __date__ = "2022.01.26"
    __purpose__ = "CS3388 Assignment1"
    def drawLine(self,point1,point2,color):
        self.color = color
        #Accesses the cordinates of point1 and point2 by using the get method from matrix class.
        x1 = point1.get(0,0)
        y1 = point1.get(1,0)
        x2 = point2.get(0,0)
        y2 = point2.get(1,0)
        #Calculates the distance between the x and y coordinates.
        dx = x2 - x1
        dy = y2 - y1
        #In the below algorithm, I have used 4 cases:
        #The main idea behind these cases are to use the four sides of the shapes.
        #1st case is when dy is smaller than dx, and x1 is larger than x2.
        #2nd case is when dy is smaller than dx, and x2 is larger than or equal to x1.
        #First two cases(1st and 2nd) draw the lower and upper-sides of the shapes.
        #3rd case is when dy is larger than dx, and y1 is larger than y2.
        #4the case is when dy is larger than dx, and y2 is larger than or equal to y1.
        #Last two cases(3rd and 4th) draw the right and left side of the shapes.
        if(abs(dy) < abs(dx)):
            #Lower-side of the shapes.
            if(x1 > x2):
                #When x1 is larger than x2, we need to reverse the points, so we need to calculate the distances again.
                yi = 1
                ddx = x1 - x2
                ddy = y1 - y2
                #if ddy is smaller than 0, we make it positive with abs method, and we start from -1(yi).
                if(ddy < 0):
                    yi = -1
                    ddy = abs(ddy)
                p = (2*ddy) - ddx
                #Using the y coordinate of second point after reverse.
                y = y2
                # Using the x coordinate of second point after reverse.
                x = int(x2)
                #Until x2 gets larger than x1, we keep going.
                while(x <= x1):
                    self.drawPoint((x,y),color)
                    #From this point, we calculate x and y for the next drawings.
                    if(p > 0):
                        y += yi
                        p -= 2 * ddx
                    p += 2 * ddy
                    x += 1
            #Upper-side of the shapes.
            else:
                #x1 is not larger than x2, so we don't need to reverse the points.
                yi = 1
                # if dy is smaller than 0, we make it positive with abs method, and we start from -1(yi).
                if (dy < 0):
                    yi = -1
                    dy = abs(dy)
                p = (2 * dy) - dx
                y = y1
                x = int(x1)
                # Until x1 gets larger than x2, we keep going.
                while (x <= x2):
                    self.drawPoint((x, y), color)
                    #From this point, we calculate x and y for the next drawings.
                    if (p > 0):
                        y += yi
                        p -= 2 * dx
                    p += 2 * dy
                    x += 1
        else:
            #Left-side of the shapes.
            if(y1 > y2):
                ##When y1 is larger than y2, we need to reverse the points, so we need to calculate the distances again.
                xi = 1
                ddx = x1 - x2
                ddy = y1 - y2
                # if ddx is smaller than 0, we make it positive with abs method, and we start from -1(yi)
                if(ddx < 0):
                    xi = -1
                    ddx = abs(ddx)
                p = 2 * ddx - ddy
                x = x2
                y = int(y2)
                #Until y2 gets larger than y1, we keep going.
                while(y <= y1):
                    self.drawPoint((x, y), color)
                    #From this point, we calculate x and y for the next drawings.
                    if(p > 0):
                        x += xi
                        p -= 2 * ddy
                    p += 2 * ddx
                    y += 1
            #Right-side of the shapes
            else:
                xi = 1
                # if dx is smaller than 0, we make it positive with abs method, and we start from -1(yi)
                if (dx < 0):
                    xi = -1
                    dx = abs(dx)
                p = 2 * dx - dy
                x = x1
                y = int(y1)
                #Until y1 gets larger than y2, we keep going.
                while (y <= y2):
                    self.drawPoint((x, y), color)
                    if (p > 0):
                        x += xi
                        p -= 2 * dy
                    p += 2 * dx
                    y += 1

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height