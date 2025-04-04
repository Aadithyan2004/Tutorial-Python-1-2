import turtle

def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)


turtle.speed(0) 


for _ in range(10):
    draw_hexagon(50)  
    turtle.right(36)  


turtle.done()