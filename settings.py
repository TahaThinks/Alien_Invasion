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
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien Settings:
        self.alien_speed = 7.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 0.25

        #Ship Settings:
        self.ship_speed = 1.5
        self.ship_limit = 3
        