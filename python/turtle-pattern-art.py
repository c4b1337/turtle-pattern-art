import turtle as tr


def setup_screen():
    """
    The setup_screen function creates a screen
    object with a black background.
    """
    screen = tr.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#262626")
    return screen


def setup_turtle():
    """
    The setup_turtle function sets the turtle's pen color, 
    speed, tracer, and pensize.
    """
    tr.pencolor('#540D6E')
    tr.speed(0)
    tr.tracer(100)
    tr.pensize(1)

def draw_pattern():
    """
    The draw_pattern function creates a pattern
    art using the turtle module.
    """
    colors = ['#FF7F3F', '#FBDF07', '#89CFFD', '#F94892']
    # The outer loop creates the pattern art by drawing circles and turning the turtle.
    for i in range(3):
        for n in range(400):
            color = colors[n % 4]
            tr.color(color)
            tr.circle(190 - n / 2, 90)
            tr.left(90)
            tr.circle(190 - n / 2, 90)
        tr.left(30)

def main():
    """
    The main function sets up the screen, 
    turtle, and draws the pattern art.
    """
    screen = setup_screen()
    setup_turtle()
    draw_pattern()
    screen.exitonclick()

if __name__ == "__main__":
    main()
