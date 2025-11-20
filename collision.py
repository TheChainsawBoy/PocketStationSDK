"""
collision.py - Advanced collision detection and response
"""
import pygame
from engine import GameObject

class CollisionHelper:
    @staticmethod
    def check_collision(obj1, obj2):
        #Check if two objects collide - returns True/False
        return obj1.collides_with(obj2)

    @staticmethod
    def get_overlap(obj1, obj2):
        #Get the overlap amount between two objects as (x, y) tuple
        if not obj1.collides_with(obj2):
            return (0, 0)

        #Calculate overlap on each axis
        left = obj1.x + obj1.width - obj2.x
        right = obj2.x + obj2.width - obj1.x
        top = obj1.y + obj1.height - obj2.y
        bottom = obj2.y + obj2.height - obj1.y

        #Get smallest overlap
        x_overlap = min(left, right)
        y_overlap = min(top, bottom)

        return (x_overlap, y_overlap)

    @staticmethod
    def push_out(obj1, obj2):
        #Push obj1 out of obj2 using smallest overlap
        if not obj1.collides_with(obj2):
            return

        x_overlap, y_overlap = CollisionHelper.get_overlap(obj1, obj2)

        #Push along smallest axis
        if x_overlap < y_overlap:
            #Push horizontally
            if obj1.x < obj2.x:
                obj1.x -= x_overlap
            else:
                obj1.x += x_overlap
        else:
            #Push vertically
            if obj1.y < obj2.y:
                obj1.y -= y_overlap
            else:
                obj1.y += y_overlap

    @staticmethod
    def can_move_to(obj, new_x, new_y, solid_objects):
        #Check if object can move to position without hitting solid objects
        old_x, old_y = obj.x, obj.y
        obj.x = new_x
        obj.y = new_y

        for solid in solid_objects:
            if solid is obj:
                continue
            if obj.collides_with(solid):
                obj.x = old_x
                obj.y = old_y
                return False

        obj.x = old_x
        obj.y = old_y
        return True

    @staticmethod
    def move_and_collide(obj, dx, dy, solid_objects):
        """
        Move object and handle collision with solid objects
        Returns True if moved successfully, False if blocked
        """
        if dx == 0 and dy == 0:
            return True

        old_x, old_y = obj.x, obj.y

        #Try moving on X axis
        obj.x += dx
        hit_x = False
        for solid in solid_objects:
            if solid is obj or not solid.solid:
                continue
            if obj.collides_with(solid):
                obj.x = old_x
                hit_x = True
                break

        #Try moving on Y axis
        obj.y += dy
        hit_y = False
        for solid in solid_objects:
            if solid is obj or not solid.solid:
                continue
            if obj.collides_with(solid):
                obj.y = old_y
                hit_y = True
                break

        return not (hit_x and hit_y)

class Hitbox(GameObject):
    #Invisible collision box that can be attached to objects
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height)
        self.parent = parent
        self.offset_x = 0
        self.offset_y = 0
        self.visible = False  #Hitboxes are invisible by default

    def update(self, dt):
        #Follow parent if attached
        if self.parent:
            self.x = self.parent.x + self.offset_x
            self.y = self.parent.y + self.offset_y

    def draw(self, screen):
        #Draw hitbox outline for debugging (if visible)
        if self.visible:
            from engine import WHITE
            pygame.draw.rect(screen, WHITE,
                           (self.x, self.y, self.width, self.height), 1)

class Trigger(GameObject):
    #Invisible trigger zone that detects when objects enter it
    def __init__(self, x, y, width, height, on_trigger=None):
        super().__init__(x, y, width, height)
        self.on_trigger_callback = on_trigger
        self.triggered_by = []
        self.visible = False

    def on_collision(self, other):
        #Called when something enters the trigger
        if other not in self.triggered_by:
            self.triggered_by.append(other)
            if self.on_trigger_callback:
                self.on_trigger_callback(other)

    def update(self, dt):
        #Clear triggered list each frame
        self.triggered_by.clear()

    def draw(self, screen):
        #Draw trigger outline for debugging (if visible)
        if self.visible:
            from engine import WHITE
            pygame.draw.rect(screen, WHITE,
                           (self.x, self.y, self.width, self.height), 1)