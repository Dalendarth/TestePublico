import tcod as libtcod

# Janela
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# Mapa
MAP_WIDTH = 80
MAP_HEIGHT = 45

# Cores
color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

# Bloco do Mapa
class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        self.explored = False

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

# Define a classe GameMap para representar o mapa
class GameMap:
    def __init__(self):
        self.tiles = [[Tile(True) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

    def create_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def make_map(self):
        # Criação de dois quartos simples
        room1 = Rect(20, 15, 10, 15)
        room2 = Rect(50, 15, 10, 15)
        self.create_room(room1)
        self.create_room(room2)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False

# Define a classe Rect para representar retângulos
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return (center_x, center_y)

# Define a classe Fighter para representar personagens que podem lutar
class Fighter:
    def __init__(self, hp, defense, power):
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        self.power = power

# Define a classe BasicMonster para representar monstros simples
class BasicMonster:
    def take_turn(self):
        pass

# Define a classe Object para representar objetos no jogo
class Object:
    def __init__(self, x, y, char, name, color, blocks=False, fighter=None, ai=None):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocks = blocks

        self.fighter = fighter
        if self.fighter:
            self.fighter.owner = self

        self.ai = ai
        if self.ai:
            self.ai.owner = self
