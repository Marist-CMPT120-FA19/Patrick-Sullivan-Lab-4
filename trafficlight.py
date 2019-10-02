from graphics import*
def main():
	win= GraphWin()
	shape= Rectangle(Point(2,20), Point(40,100))
	shape.setOutline("black")
	shape.setFill("white")
	shape.draw(win)
	red=Circle(Point(20,40),8)
	red.setOutline("black")
	red.setFill("red")
	red.draw(win)
	yellow=Circle(Point(20,60), 8)
	yellow.setOutline("black")
	yellow.setFill("yellow")
	yellow.draw(win)
	green=Circle(Point(20,80),8)
	green.setOutline("black")
	green.setFill("green")
	green.draw(win)
	win.getMouse()
	win.close()

	
main()
