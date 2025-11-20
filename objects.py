"""
objects.py - Pre-built game objects for quick prototyping
BLACK AND WHITE ONLY - PocketStation style!
"""
import pygame
from engine import GameObject, BLACK, WHITE
from input import Input

class Sprite(GameObject):
    #Simple rectangular sprite - BLACK or WHITE only
    def __init__(self, x, y, width, height, color=BLACK):
        super().__init__(x, y, width, height)
        #Force color to be black or white
        self.color = WHITE if color == WHITE else BLACK

    def draw(self, screen, camera=None):
        #Apply camera offset if camera exists
        if camera:
            screen_x, screen_y = camera.apply(self.x, self.y)
        else:
            screen_x, screen_y = self.x, self.y

        pygame.draw.rect(screen, self.color,
                        (self.x, self.y, self.width, self.height))

class Player(Sprite):
    #Player-controlled sprite with WASD movement and KL action buttons
    def __init__(self, x, y, width=4, height=4, speed=20):
        super().__init__(x, y, width, height, BLACK)
        self.speed = speed
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, dt):
        #Get direction from input
        dx, dy = Input.get_direction()

        #Update velocity
        self.velocity_x = dx * self.speed
        self.velocity_y = dy * self.speed

        #Move
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        #Keep player in bounds (32x32)
        self.x = max(0, min(32 - self.width, self.x))
        self.y = max(0, min(32 - self.height, self.y))

        #Check action buttons (override this for custom behavior)
        if Input.action1_pressed():
            self.on_action1()

    def on_action1(self):
        #Override this for ENTER button action
        pass

    def draw(self, screen, camera=None):
        #Apply camera offset if camera exists
        if camera:
            screen_x, screen_y = camera.apply(self.x, self.y)
        else:
            screen_x, screen_y = self.x, self.y

        #Draw player as filled white rectangle
        pygame.draw.rect(screen, BLACK,
                        (int(self.x), int(self.y), self.width, self.height))

class Enemy(Sprite):
    def __init__(self, x, y, width=3, height=3):
        super().__init__(x, y, width, height, BLACK)
        self.speed = 10
        self.direction = 1
        self.solid = True

    def update(self, dt):
        self.x += self.speed * self.direction * dt

        #Bounce at edges
        if self.x <= 0 or self.x >= 32 - self.width:
            self.direction *= -1

    def draw(self, screen, camera=None):
        #Apply camera offset if camera exists
        if camera:
            screen_x, screen_y = camera.apply(self.x, self.y)
        else:
            screen_x, screen_y = self.x, self.y

        #Draw as filled white square
        pygame.draw.rect(screen, BLACK,
                        (int(self.x), int(self.y), self.width, self.height))

class Wall(Sprite):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, BLACK)
        self.solid = True

    def draw(self, screen, camera=None):
        #Apply camera offset if camera exists
        if camera:
            screen_x, screen_y = camera.apply(self.x, self.y)
        else:
            screen_x, screen_y = self.x, self.y

        pygame.draw.rect(screen, BLACK,
                        (int(self.x), int(self.y), self.width, self.height))

class Particle(Sprite):
    def __init__(self, x, y, vx, vy, lifetime=1.0):
        super().__init__(x, y, 1, 1, BLACK)
        self.vx = vx
        self.vy = vy
        self.lifetime = lifetime
        self.age = 0

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.age += dt

        if self.age >= self.lifetime:
            self.active = False
            self.visible = False

class Bullet(Sprite):
    def __init__(self, x, y, vx, vy, width=1, height=1):
        super().__init__(x, y, width, height, BLACK)
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        #Remove if out of bounds
        if self.x < 0 or self.x > 32 or self.y < 0 or self.y > 32:
            self.active = False
            self.visible = False

    def on_collision(self, other):
        if other is not self:
            self.active = False
            self.visible = False

class PixelSprite(GameObject):
    #Custom sprite defined by pixel data - for custom shapes
    def __init__(self, x, y, pixel_data):
        """
        pixel_data should be a 2D list like:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
        Where 1 = WHITE pixel, 0 = no pixel
        """
        self.pixel_data = pixel_data
        height = len(pixel_data)
        width = len(pixel_data[0]) if height > 0 else 0
        super().__init__(x, y, width, height)

    def draw(self, screen, camera=None):
        #Apply camera offset if camera exists
        if camera:
            screen_x, screen_y = camera.apply(self.x, self.y)
        else:
            screen_x, screen_y = self.x, self.y

        for row in range(len(self.pixel_data)):
            for col in range(len(self.pixel_data[row])):
                if self.pixel_data[row][col]:
                    screen.set_at((int(self.x) + col, int(self.y) + row), BLACK)

    def update_data(self, data):
        self.pixel_data = data