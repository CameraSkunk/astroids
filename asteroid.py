import pygame
import random

from circleshape import CircleShape
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)                                      #Random angle of departure
            v1 = self.velocity.rotate(angle)                                    #Angle of departure one
            v2 = self.velocity.rotate(-angle)                                   #Inverse of Angle of departure for two
            new_radius = self.radius - ASTEROID_MIN_RADIUS                      #Computes new radius of astroids
            
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)   #Creates Astroid 1
            asteroid.velocity = v1 * 1.2                                        #Sets departure for Astroid 1

            asteroid = Asteroid(self.position.x, self.position.y, new_radius)   #Creates Astroid 2
            asteroid.velocity = v2 * 1.2                                        #Sets departure for Astroid 2
