import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()

    Clock = pygame.time.Clock()
    dt = 0

    #Sprite Groups defined
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Group assignments
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return
            
        screen.fill("black")

        # Loops over all objects in the drawable group and runs the draw method
        for obj in drawable:
            obj.draw(screen)
        
        #Runs all update methods for all in updatable group
        updatable.update(dt) 

        pygame.display.flip()

        dt = Clock.tick(60) / 1000 #keep at end of loop       


if __name__ == "__main__":
    main()
