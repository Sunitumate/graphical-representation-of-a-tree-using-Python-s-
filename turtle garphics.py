import turtle as t
import colorsys

# Set up screen
t.bgcolor('black')
t.speed(0)         # Fastest speed for instant drawing
t.tracer(10)       # Lower tracer to make the drawing visible in real-time

def draw():
    h = 0
    n = 36           # Number of color variations (higher creates a smoother gradient)
    t.width(2)       # Set pen size for visible lines
    
    for i in range(100):   # Increase range for a longer, more intricate pattern
        # Set color using HSV to RGB for a rainbow effect
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        h += 1 / n
        
        t.forward(i * 2)   # Move forward by an increasing amount
        t.left(59)         # Slight turn to create the spiral pattern

draw()
t.done()
