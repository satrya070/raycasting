import math

WIDTH, HEIGHT = 640, 480  
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
RESOLUTION = (WIDTH, HEIGHT)

PLAYER_POSITION = (0, 0)
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.001
PLAYER_ROTATION = 0.002

FPS = 30
FOV = math.pi / 3  # 60 degrees
HALF_FOV = FOV / 2  # 30 degrees
NUM_RAYS = WIDTH // 2  # 320 rays
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # 60 / 320 = 0.1875 degrees
MAX_DEPTH = 20  # the max amount of map tiles to check for every ray 

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)  # 320 / tan(30) = 554.26 pixels
SCALE = WIDTH // NUM_RAYS  # 640 / 320 = 2 pixels per ray on the projection plane