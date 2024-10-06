import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0,1))
        pygame.display.flip()
    print("Starting asteroids!")
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")

if __name__=="__main__":
    main()
