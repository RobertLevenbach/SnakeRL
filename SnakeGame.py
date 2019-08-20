import pygame

## initiliaze all modules of pygame (import) > NEEDED
pygame.init()

##Variables
    # settings
displayWidth = 800
displayHeight = 600
fps=100
    #starting position snake
x = (displayWidth*0.45)
x_change = 0
y = (displayHeight *0.8)

    #colour definition
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

## Define stuff
    #clock> will time things (frames per second)
clock=pygame.time.Clock()
    #snake image
snakeImg = pygame.image.load('snake.png')


## setup display
    #set resolution
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
    #set titel of window
pygame.display.set_caption('Snakarel')

## functions
def car(x,y):
    #blit draws stuff to background
    # x,y is where you will blit the image
    # y starts top, gets more when go down, x starts left goes right more
    gameDisplay.blit(snakeImg,(x,y))



##set game loop > stops when quit or when snake crashes (wall)
crashed = False #start it is not crashed

while not crashed:
    #start loop with event handling> all input happens in here!
    for event in pygame.event.get(): #gets every event (mouse movement, button movement> makes list per frame)
        #crash event> here when user does quit button
        if event.type == pygame.QUIT:
            crashed=True
        #if a button is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #when arrow left is pressed
                x_change=-5
            
        

        gameDisplay.fill(white) # set background > DOES ALL SO AFTER THIS THE REST
        car(x,y) #> blits car

        ##print the events to console
        #print(event)

    #update display (we made everything above, now display it)> no parameters updates everything
        pygame.display.update()

        clock.tick(fps)

# uninitiate pygame
pygame.quit()
quit()

        
