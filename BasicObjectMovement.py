import pygame
pygame.init()
#Intialization
win = pygame.display.set_mode((500, 500))#Width,Height
#Window Name
pygame.display.set_caption("First Game")
#Attributes of rectangle
#X axis
x = 50
#Y axis
y = 50
width = 40
height = 60
#For movement
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)
    #For closing window without error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    #To catch what key is pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2)/2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    #To fill black color
    win.fill((0, 0, 0))
    #To draw rectangle(where, (RGB), (attributes))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #To update display every time we move
    pygame.display.update()
#To Quit
pygame.quit()
