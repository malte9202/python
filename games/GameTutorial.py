# import and init pygame
import pygame
pygame.init()

# define window width and height
win = pygame.display.set_mode((500, 500))

# set window title
pygame.display.set_caption("First Game")

# define variables for character
x = 50  # x coordinate
y = 50  # y coordinate
width = 40  # width
height = 60  # height
vel = 5  # movement "speed"

# game loop
run = True
while run:
    pygame.time.delay(100)

    # get event
    for event in pygame.event.get():

        # event click X on the window
        if event.type == pygame.QUIT:
            run = False
    # get pressed keys
    keys = pygame.key.get_pressed()

    # move left
    if keys[pygame.K_LEFT]:
        x -= vel

    # move right
    if keys[pygame.K_RIGHT]:
        x += vel

    # move up
    if keys[pygame.K_UP]:
        y -= vel

    # move down
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
    