import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for sprite in updateable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        
        screen.fill((0,0,0,1))
        
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000

        
    print("Starting asteroids!")
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")

if __name__=="__main__":
    main()
