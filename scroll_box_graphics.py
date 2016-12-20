import graphics
from graphics import update

window1 = graphics.GraphWin("rectangles", 600, 600)
scroll = []

for i in range(1):

    rectangle1 = graphics.Rectangle(graphics.Point(0, 0), graphics.Point(600, 30))
    rectangle1.setFill('purple')
    rectangle1.draw(window1)
    scroll.append(rectangle1)

    rectangle2 = graphics.Rectangle(graphics.Point(0, -100), graphics.Point(600, -50))
    rectangle2.setFill('green')
    rectangle2.draw(window1)
    scroll.append(rectangle2)

while True:

    for r in scroll:

        r.move(0,1)
        update(100)

        if r.getP2().getY() > 599:
             r.move(0,-500)





