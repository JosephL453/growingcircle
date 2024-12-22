import pygame
pygame.init

WIDTH = 600
HEIGHT = 800
radius = 50
screen = pygame.display.set_mode((WIDTH,HEIGHT))
blue = (0,0,255)
screen.fill((255,255,255))
pygame.display.update()

class Circle():
    
    def __init__(self,color,position,radius,width):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.width)
    
    def grow(self,r):
        self.radius = self.radius + r
        pygame.draw.circle(self.screen,self.color,self.position,self.width)

circle1 = Circle(screen,blue,(300,400),50,0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle1.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle1.grow(20)
            pygame.display.update()
        elif event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()