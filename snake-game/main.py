import curses
import time
import random

window = curses.initscr()
curses.curs_set(0)
window.nodelay(True)
#window.refresh()

window.addstr("Welcome!\nPress enter to start...")
while window.getch() != ord('\n'):
    pass

def createApple(window):
    position = random.randint(0, 50), random.randint(0, 50)
    window.addstr(random.randint(0, 50), random.randint(0, 50), "Q")

def move(window):

    window.clear()

    x, y = 1, 1
    dir = 0
    window.addstr(y, x, "*")
    window.refresh()

    #Snake body length and position array
    lenBody = 2
    body_position = [(y, x)]

    while True:
        #Watch the key pressed
        key = window.getch()
        #Clear everything at the window
        window.clear()

        #Change snake direction
        if key == curses.KEY_UP and dir != 2:
            dir = 1
        elif key == curses.KEY_DOWN and dir != 1:   
            dir = 2
        elif key == curses.KEY_RIGHT and dir != 4:     
            dir = 3
        elif key == curses.KEY_LEFT and dir != 3:     
            dir = 4

        #Change asterisk positions based on directions
        if dir == 1:
            y = max(1, y - 1)
        elif dir == 2:
            y += 1
        elif dir == 3:
            x += 1
        elif dir == 4:
            x = max(0, x - 1)

        #Add the new positions in the body position
        body_position.insert(0, (y, x))

        #If the body position surpasses the body length, the last asterisk will be erased
        if len(body_position) > lenBody:
            tail_y, tail_x = body_position.pop()
            window.addstr(tail_y, tail_x, " ")

        #Positions the asterisk for the snake head
        window.addstr(y, x, "*")

        #Positions the asterisks to make the snake move
        for segment_y, segment_x in body_position[1:]:
            window.addstr(segment_y, segment_x, "*")

        window.refresh()
        time.sleep(0.1)

curses.wrapper(move)