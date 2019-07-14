import pygame

pygame.init()

win = pygame.display.set_mode((680,480))
counter = 0
pygame.display.set_caption("Space Invader")
ss = []
for i in range(1,3):
    ss.append(pygame.image.load('ss'+str(i)+'.png'))
    ss[i-1] = pygame.transform.scale(ss[i-1],(80,80))
def redraw():
    global counter
    win.fill((0,0,0))
    for i in range(2):
        if counter == i:
            win.blit(ss[i],(200,200))
    win.blit(ss[1], (300, 200))
    pygame.display.update()
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if counter < 2:
            counter += 1
    elif keys[pygame.K_LEFT]:
        if counter > 0:
            counter -= 1
    redraw()
pygame.quit()