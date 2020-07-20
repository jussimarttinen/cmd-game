from Entities import Entity

class Player(Entity):

    def __init__(self, x, y, sprite, colour="white", weapon_sprites=["", ""]):
        # Location of player character
        super().__init__(x, y, sprite, colour)
        self._weapon_sprites = weapon_sprites
        # how the player looks when holding a gun
        self.weapon_sprites = [
        weapon_sprites[0] + self.sprite, 
        self.sprite + weapon_sprites[1]]
        self._default_sprite = self.sprite

        # initialises the player characters visuals
        self.update_position(0,0)
    
    def update_position(self, dx, dy):
        self.x += dx
        self.y += dy
        # character has moven to the right
        if dx > 0:
            self.turn_character("right")
        # character has moven to the left
        elif dx < 0:
            self.turn_character("left")

    def change_symbol(self, new_symbol, colour="white", ovrwrte_plr_smbl=False):
        """Changes the player symbol to another one
        If ovrwrte_plr_symbol is True, the reference player symbol will be changed."""
        if ovrwrte_plr_smbl:
            self._default_sprite = new_symbol
        self.sprite = new_symbol
        self.colour = colour
        self.weapon_sprites = [
        self._weapon_sprites[0] + self._default_sprite, 
        self._default_sprite + self._weapon_sprites[1]]
    
    def turn_character(self, direction):
        """'Turns' the character symbol to the chosen direction"""
        if direction == "left":
            direction = 0
        elif direction == "right":
            direction = 1
        self.change_symbol(self.weapon_sprites[direction])