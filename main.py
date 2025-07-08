import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")

    # initialize game
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, drawables, updatables)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    newfield = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        
        for drawable in drawables:
            drawable.draw(screen)
      
                        
        pygame.display.flip()
        
        #limit framerate to 60fps
        dt = (clock.tick(60)/1000)

        updatables.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.kill()


        for asteroid in asteroids:
            if player1.collision(asteroid):
                print("Game over!")
                sys.exit()
        

        



if __name__ == "__main__":
    main()