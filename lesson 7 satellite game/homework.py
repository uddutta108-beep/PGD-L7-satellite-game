import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 600

stars = []
number_of_star = 8
next_star = 0

lines = []

start_time = 0
total_time = 0
end_time = 0

def create_star():
    global start_time
    for i in range (number_of_star):
        star = Actor("star")
        star.pos = random.randint(50,750),random.randint(50,550)
        stars.append (star)

    start_time = time.time()

create_star()

def draw():
    global total_time
    screen.blit("space",(0,0))

    number = 1

    for star in stars:
        star.draw()
        screen.draw.text(str(number),(star.pos[0], star.pos[1]+20))
        number = number + 1 

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_star < number_of_star:
        total_time = time.time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30 ) 

    if next_star == number_of_star:
        screen.draw.text("Good job", (300,300), fontsize = 50)  

def update():
    pass

pgzrun.go()
