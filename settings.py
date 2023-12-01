class Settings:
    """A class to store all settings for Alien Invasion"""
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.alien_speed = 0.5
        self.bullet_speed = 1.5
            
        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 0.25

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings:
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (155,190,200)
        
        #Ship Settings:
        self.ship_limit = 3

        #Bullet Settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings:
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()


        