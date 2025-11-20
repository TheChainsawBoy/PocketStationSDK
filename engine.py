"""
engine.py - Core game engine for PocketStation-style games
Simple 2D engine with 32x32 pixel monochrome display (like PocketStation)
"""
import pygame
import os
import sys

#PocketStation colors - only black and white!
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = ""
    return os.path.join(base_path, relative_path)

class GameObject:
    """Base class for all game objects"""
    def __init__(self, x=0, y=0, width=8, height=8):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.active = True
        self.solid = False  #Can other objects collide with this?

    def update(self, dt):
        #Override this in subclasses
        pass

    def draw(self, screen):
        #Override this in subclasses
        pass

    def get_rect(self):
        #Get bounding box as pygame Rect
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides_with(self, other):
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

    def on_collision(self, other):
        #Called when this object collides with another - override in subclasses
        pass

class Scene:
    #Container for game objects and scene logic
    def __init__(self, name="Scene"):
        self.name = name
        self.objects = []
        self.background_color = WHITE
        self.camera = None  #Optional camera for scrolling

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def get_objects_by_type(self, obj_type):
        return [obj for obj in self.objects if isinstance(obj, obj_type)]

    def check_collisions(self):
        for i, obj1 in enumerate(self.objects):
            if not obj1.active:
                continue
            for obj2 in self.objects[i+1:]:
                if not obj2.active:
                    continue
                if obj1.collides_with(obj2):
                    obj1.on_collision(obj2)
                    obj2.on_collision(obj1)

    def update(self, dt):
        #Update camera if present
        if self.camera:
            self.camera.update(dt)

        for obj in self.objects[:]:  #Copy list to allow removal during iteration
            if obj.active:
                obj.update(dt)
        self.check_collisions()

        #Remove inactive objects
        self.objects = [obj for obj in self.objects if obj.active or obj.visible]

    def draw(self, screen):
        screen.fill(self.background_color)

        for obj in self.objects:
            if obj.visible:
                #If camera exists, only draw visible objects with camera offset
                if self.camera:
                    if self.camera.is_visible(obj):
                        obj.draw(screen, self.camera)
                else:
                    #No camera, draw normally
                    obj.draw(screen)

    def set_camera(self, camera):
        #ttach a camera to this scene
        self.camera = camera

class GameEngine:
    #Main engine class - handles window, scenes, and game loop
    def __init__(self, title="PocketEngine Game", scale=10):
        pygame.init()

        #PocketStation resolution: 32x32 pixels, MONOCHROME
        self.base_width = 32
        self.base_height = 32
        self.scale = scale

        #Create window with scaled resolution
        self.screen = pygame.display.set_mode(
            (self.base_width * scale, self.base_height * scale)
        )
        pygame.display.set_caption(title)

        #Load an icon image (must be a small image, like 32x32 or 64x64)
        icon = pygame.image.load(resource_path("icon.ico"))  #Make sure the path is correct
        pygame.display.set_icon(icon)  #Set window icon

        #Virtual screen for rendering at base resolution
        self.virtual_screen = pygame.Surface((self.base_width, self.base_height))

        self.clock = pygame.time.Clock()
        self.running = False
        self.current_scene = None
        self.fps = 20

    def set_scene(self, scene):
        self.current_scene = scene

    def run(self):
        if not self.current_scene:
            print("Error: No scene set!")
            return

        self.running = True

        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #Update current scene
            self.current_scene.update(dt)

            #Draw to virtual screen
            self.current_scene.draw(self.virtual_screen)

            #Scale to actual window
            scaled = pygame.transform.scale(
                self.virtual_screen,
                (self.base_width * self.scale, self.base_height * self.scale)
            )
            self.screen.blit(scaled, (0, 0))

            pygame.display.flip()

        pygame.quit()
        sys.exit()