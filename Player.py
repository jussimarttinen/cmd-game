class Player:

    def __init__(self, x, y, symbol, colour="white", weapon_sprites=["", ""]):
        # Location of player character
        self.x = x
        self.y = y
        # the player symbol for reference
        # this one should ONLY be changed if e.g. player skin changes 
        self._player_symbol = symbol
        self._weapon_sprites = weapon_sprites
        # how the player looks when holding a gun
        self.weapon_sprites = [
        weapon_sprites[0] + self._player_symbol, 
        self._player_symbol + weapon_sprites[1]]

        # initialises the player characters visuals
        self.change_symbol(symbol, colour)
    
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
            self._player_symbol = new_symbol
        self.symbol = new_symbol
        self.colour = colour
        self.weapon_sprites = [
        self._weapon_sprites[0] + self._player_symbol, 
        self._player_symbol + self._weapon_sprites[1]]
    
    def turn_character(self, direction):
        """'Turns' the character symbol to the chosen direction"""
        if direction == "left":
            direction = 0
        elif direction == "right":
            direction = 1
        self.change_symbol(self.weapon_sprites[direction])