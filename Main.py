import pygame

pygame.init()

win = pygame.display.set_mode((640,480))

pygame.display.set_caption("Space Invaders")
# position for our space ship
x = 50
y = 380
#velocity for space ship
clock = pygame.time.Clock()
vel_ss = 5
left = False
right = False
spaceShip = pygame.image.load("ss.png")
spaceShip = pygame.transform.scale(spaceShip,(80,80))
def redrawWindow():
    global x,y,vel_ss,spaceShip
    win.fill((0,0,0))
    win.blit(spaceShip,(x,y))
    pygame.display.update()
run = True

while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel_ss
            left = True
            right = False
    elif keys[pygame.K_RIGHT]:
        if x < 500 :
            x += vel_ss
            right = True
            left = False
    redrawWindow()

pygame.quit()