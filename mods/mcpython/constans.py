print("[INFO] setting constants")

import config

from moduls import *

TICKS_PER_SEC = 60

# Size of sectors used to ease block loading.
SECTOR_SIZE = config.CONFIGS["SECTOR_SIZE"]

WALKING_SPEED = config.CONFIGS["WALKING_SPEED"]
FLYING_SPEED = config.CONFIGS["FLYING_SPEED"]

GRAVITY = config.CONFIGS["GRAVITY"]
MAX_JUMP_HEIGHT = config.CONFIGS["MAX_JUMP_HEIGHT"] # About the height of a block.
# To derive the formula for calculating jump speed, first solve
#    v_t = v_0 + a * t
# for the time at which you achieve maximum height, where a is the acceleration
# due to gravity and v_t = 0. This gives:
#    t = - v_0 / a
# Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
#    s = s_0 + v_0 * t + (a * t^2) / 2
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 50

PLAYER_HEIGHT = config.CONFIGS["PLAYER_HEIGHT"]

FACES = [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (-1, -1, 1), (1, 1, -1), (-1, 1, -1), (1, -1, -1), (-1, -1, -1)]
