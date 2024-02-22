from turtle import *
speed(2)

def polygon(side):
    for i in range(side):
        fd(size)
        lt(360/side)

# calling
polygon(3, 150)
polygon(4, 100)
polygon(5, 75)
polygon(side=6, size=50)
mainloop()
