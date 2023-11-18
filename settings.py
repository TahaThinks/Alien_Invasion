class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings:
        self.ship_speed = 1.5        
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (155,190,200)

        #Bullet Settings:
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3