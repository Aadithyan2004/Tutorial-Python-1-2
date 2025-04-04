import turtle


screen = turtle.Screen()
screen.bgcolor("white")


star_turtle = turtle.Turtle()
star_turtle.color("blue")
star_turtle.pensize(2)


def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)  


draw_star(100)


star_turtle.hideturtle()
turtle.done()