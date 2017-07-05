# game options/settings
TITLE = "Jump Jump"
WIDTH = 650 #480
HEIGHT = 880 #600
FPS = 60
FONT_NAME = 'arial'
import os
#Set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
bg = os.path.join(img_folder, "background.png")

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 25 #20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = (BLACK)

