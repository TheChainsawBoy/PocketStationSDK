"""
input.py - Input handling for PocketStation 5-button layout
Buttons: W, A, S, D (D-pad), K (Action 1)
"""
import pygame

class Input:
    #Button mapping
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
    ACTION1 = pygame.K_RETURN
    _keys = None
    _prev_keys = None

    @classmethod
    def update(cls):
        #Call this once per frame to update input state
        cls._prev_keys = cls._keys
        cls._keys = pygame.key.get_pressed()
        if cls._prev_keys is None:
            cls._prev_keys = cls._keys

    @classmethod
    def is_held(cls, key):
        #Check if a button is currently held down
        if cls._keys is None:
            return False
        return cls._keys[key]

    @classmethod
    def is_pressed(cls, key):
        #Check if a button was just pressed this frame
        if cls._keys is None or cls._prev_keys is None:
            return False
        return cls._keys[key] and not cls._prev_keys[key]

    @classmethod
    def is_released(cls, key):
        #Check if a button was just released this frame
        if cls._keys is None or cls._prev_keys is None:
            return False
        return not cls._keys[key] and cls._prev_keys[key]

    @classmethod
    def up_held(cls):
        return cls.is_held(cls.UP)

    @classmethod
    def down_held(cls):
        return cls.is_held(cls.DOWN)

    @classmethod
    def left_held(cls):
        return cls.is_held(cls.LEFT)

    @classmethod
    def right_held(cls):
        return cls.is_held(cls.RIGHT)

    @classmethod
    def action1_held(cls):
        return cls.is_held(cls.ACTION1)

    @classmethod
    def up_pressed(cls):
        return cls.is_pressed(cls.UP)

    @classmethod
    def down_pressed(cls):
        return cls.is_pressed(cls.DOWN)

    @classmethod
    def left_pressed(cls):
        return cls.is_pressed(cls.LEFT)

    @classmethod
    def right_pressed(cls):
        return cls.is_pressed(cls.RIGHT)

    @classmethod
    def action1_pressed(cls):
        return cls.is_pressed(cls.ACTION1)

    @classmethod
    def get_direction(cls):
        #Get direction as (x, y) tuple, normalized
        dx = 0
        dy = 0

        if cls.left_held():
            dx -= 1
        if cls.right_held():
            dx += 1
        if cls.up_held():
            dy -= 1
        if cls.down_held():
            dy += 1

        #Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.707  #1/sqrt(2)
            dy *= 0.707

        return (dx, dy)

#Helper function for backward compatibility
def get_keys():
    return pygame.key.get_pressed()