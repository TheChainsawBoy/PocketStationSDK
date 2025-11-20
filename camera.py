"""
camera.py - Camera system for scrolling maps
Allows larger maps than the 32x32 screen with camera following
"""
class Camera:
    """Camera that follows the player and handles map scrolling"""

    def __init__(self, screen_width=32, screen_height=32, map_width=64, map_height=64):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height

        #Camera position (top-left corner)
        self.x = 0
        self.y = 0

        #Target to follow (usually the player)
        self.target = None

        #Camera following settings
        self.follow_smoothness = 1.0  #1.0 = instant, lower = smoother
        self.offset_x = 0  #Offset from center
        self.offset_y = 0

    def set_target(self, target):
        self.target = target

    def set_map_size(self, width, height):
        self.map_width = width
        self.map_height = height

    def update(self, dt):
        if not self.target:
            return

        #Calculate desired camera position (center target on screen)
        desired_x = self.target.x + self.target.width / 2 - self.screen_width / 2 + self.offset_x
        desired_y = self.target.y + self.target.height / 2 - self.screen_height / 2 + self.offset_y

        #Smooth following (lerp)
        self.x += (desired_x - self.x) * self.follow_smoothness
        self.y += (desired_y - self.y) * self.follow_smoothness

        #Clamp camera to map boundaries
        self.x = max(0, min(self.map_width - self.screen_width, self.x))
        self.y = max(0, min(self.map_height - self.screen_height, self.y))

    def apply(self, obj_x, obj_y):
        """
        Convert world coordinates to screen coordinates
        Returns (screen_x, screen_y)
        """
        return (obj_x - self.x, obj_y - self.y)

    def world_to_screen(self, world_x, world_y):
        return self.apply(world_x, world_y)

    def screen_to_world(self, screen_x, screen_y):
        return (screen_x + self.x, screen_y + self.y)

    def is_visible(self, obj):
        screen_x, screen_y = self.apply(obj.x, obj.y)

        return (screen_x + obj.width >= 0 and
                screen_x < self.screen_width and
                screen_y + obj.height >= 0 and
                screen_y < self.screen_height)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        #Clamp to boundaries
        self.x = max(0, min(self.map_width - self.screen_width, self.x))
        self.y = max(0, min(self.map_height - self.screen_height, self.y))

    def center_on(self, obj):
        self.x = obj.x + obj.width / 2 - self.screen_width / 2
        self.y = obj.y + obj.height / 2 - self.screen_height / 2
        #Clamp to boundaries
        self.x = max(0, min(self.map_width - self.screen_width, self.x))
        self.y = max(0, min(self.map_height - self.screen_height, self.y))