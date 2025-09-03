from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override draw method of CircleShape
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, 2)
    
    def update(self, dt):
        self.move(dt)
    
    def move(self, dt):
        self.position += self.velocity * dt