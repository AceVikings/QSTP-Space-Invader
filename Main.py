import pygame

pygame.init()

win = pygame.display.set_mode((1200,600))

pygame.display.set_caption("Space Invaders")
# position for our space ship
x = 50
y = 380

clock = pygame.time.Clock()

spaceS = pygame.image.load("ss.png")
spaceS = pygame.transform.scale(spaceS,(80,80))
enemy_5 = pygame.image.load('1.png')
enemy_5 = pygame.transform.scale(enemy_5,(80,80))
enemy_5 = pygame.transform.flip(enemy_5,False,True)
enemy_10 = pygame.image.load('2.png')
enemy_10 = pygame.transform.scale(enemy_10,(80,80))
enemy_10 = pygame.transform.flip(enemy_10,False,True)
enemy_15 = pygame.image.load('3.png')
enemy_15 = pygame.transform.scale(enemy_15,(80,80))
enemy_15 = pygame.transform.flip(enemy_15,False,True)
background = pygame.image.load('bg1.jpeg')
sprites = []    # List of sprites
i_flip = False      # Flag to reverse invader direction
i_count = 0         # Invader count
i_miss_count = 0 # Invader missile count
class spaceShip(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.vel_ss = 25
        self.left = False
        self.right = False
    def draw(self,win):
        win.blit(spaceS,(self.x,self.y))

class shots(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 5
        self.color = color
        self.vel_b = 40
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
def redrawWindow():

    win.blit(background,(0,0))

    ss .draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run = True

ss = spaceShip(200,500,80,80)

bullets = []
while run:
    clock.tick(20)
    for bullet in bullets:
        if bullet.y > 0:
            bullet.y -= bullet.vel_b
        else:
            bullets.pop(bullets.index(bullet))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #Making Enemy Spaceships appear



    #bullet shoot
    if keys[pygame.K_SPACE]:

        if len(bullets) < 500:
            bullets.append(shots(round(ss.x + 40),round(ss.y +40),(128,128,128)))
    #bullet collision check
    for bullet in bullets:
        for i in range(5,20,5):
            if pygame.sprite.collide_rect(bullet,'enemy_'+str(i)):
                bullet.kill()
                'enemy_'+str(i).kill()
    #movements
    if keys[pygame.K_LEFT]:
        if ss.x > 0:
            ss.x -= ss.vel_ss
            left = True
            right = False
    elif keys[pygame.K_RIGHT]:
        if ss.x < 1200 - ss.width:
            ss.x += ss.vel_ss
            right = True
            left = False
    redrawWindow()

pygame.quit()
