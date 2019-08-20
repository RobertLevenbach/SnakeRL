import pygame

## initiliaze all modules of pygame (import) > NEEDED
pygame.init()

##Variables
    # settings
displayWidth = 800
displayHeight = 600
fps=60
    #starting position snake
x = (displayWidth*0.45)
x_right = 0
x_left = 0
y = (displayHeight *0.8)
y_up = 0
y_down = 0

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
            if event.key == pygame.K_RIGHT: #when arrow left is pressed
                x_left = 5
                x_right = 0
                y_up = 0
                y_down = 0
            if event.key == pygame.K_LEFT: #when arrow right is pressed
                x_right = -5
                x_left = 0
                y_up = 0
                y_down = 0
            if event.key == pygame.K_DOWN: #when arrow right is pressed
                y_up = 5
                y_down = 0
                x_right = 0
                x_left = 0
            if event.key == pygame.K_UP: #when arrow right is pressed
                y_up = 0
                y_down = -5
                x_right = 0
                x_left = 0


            
            # x will adjust to event
            x = x + x_right + x_left
            y = y + y_up + y_down
        x=x
        y=y

        #if button is released
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #when arrow left is pressed
        #        x_change = 0



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

        
