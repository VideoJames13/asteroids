import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initial game loop
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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
        

        



if __name__ == "__main__":
    main()