# import and init pygame
import pygame
pygame.init()

# define window width and height
win = pygame.display.set_mode((500, 500))

# set window title
pygame.display.set_caption("First Game")

screen_width = 500

# define variables for character
x = 50  # x coordinate
y = 50  # y coordinate
width = 40  # width
height = 60  # height
vel = 15  # movement "speed"

is_jump = False
jump_count = 10

run = True
while run:  # game loop
    pygame.time.delay(100)

    for event in pygame.event.get():  # get event

        # event click X on the window
        if event.type == pygame.QUIT:
            run = False
    # get pressed keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:  # move left and check for borders
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:  # move right and check for borders
        x += vel

    if not(is_jump):
        if keys[pygame.K_UP] and y > vel:  # move up and check for borders
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_width - height - vel:  # move down and check for borders
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    win.fill((0, 0, 0))  # fill up former position of the character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # draw character
    pygame.display.update()  # update window

pygame.quit()  # quit program
    