import turtle
from automata import go
from point import Points

def draw_points(points):
    t.up()
    t.shape(name="circle")
    labels = points.points
    i = 0
    for x, y in zip(points.x, points.y):
        t.goto(x, y+10)
        t.down()
        t.write(labels[i], font=("Verdana",
                                 15, "normal"))
        i += 1
        t.goto(x, y)
        t.stamp()

        t.up()

def connect(x1, x2, state):
    c = "purple" if state == "a" else "green"
    t.up()
    t.width(3)
    t.goto(x1, 0)
    t.color(c)
    t.down()
    if x1 > x2:
        t.left(90)
        t.circle(radius=abs(x2 - x1) / 2, extent=45)
        t.write(state, font=("Verdana",
                                    15, "normal"))
        t.circle(radius=abs(x2 - x1) / 2, extent=135)
        t.left(90)
    elif x1 < x2:
        t.right(90)
        t.circle(radius=abs(x2 - x1) / 2, extent=45)
        t.write(state, font=("Verdana",
                                    15, "normal"))
        t.circle(radius=abs(x2 - x1) / 2, extent=135)
        t.right(90)
    else:
        t.right(90)
        t.circle(radius=15, extent=90)
        t.write(state, font=("Verdana",
                                    15, "normal"))
        t.circle(radius=15, extent=270)
        t.left(90)


global t
t = turtle.Turtle()
n = 3
p = Points(n)

draw_points(p)
for el in p.points:
    na, nb = go(el)
    print(f"\lambda(a, {el}) = {na}")
    print(f"\lambda(b,{el}) = {nb}")
    connect(p.find_point(el), p.find_point(na), "a")
    connect(p.find_point(el), p.find_point(nb), "b")

t.up()
t.goto(1000,1000)
turtle.mainloop()
