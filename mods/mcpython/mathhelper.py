from moduls import *

from constans import *
print("[INFO] creating funks")

def cube_vertices(x, y, z, n):
    """ Return the vertices of the cube at position x, y, z with size 2*n.

    """
    return [
        x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
        x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
        x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
        x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
        x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
        x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
    ]


def tex_coord(x, y, n=16):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side, n=16):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = tex_coord(*top, n=n)
    bottom = tex_coord(*bottom, n=n)
    side = tex_coord(*side, n=n)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result

def total_tex_coords(top, bottom, N, O, S, W, n=16):
    top = tex_coord(*top, n=n)
    bottom = tex_coord(*bottom, n=n)
    nord = tex_coord(*N, n=n)
    ost = tex_coord(*O, n=n)
    sued = tex_coord(*S, n=n)
    west = tex_coord(*W, n=n)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(nord)
    result.extend(ost)
    result.extend(sued)
    result.extend(west)
    return result
    
print("[INFO] definiting vector-functions")

def normalize(position):
    """ Accepts `position` of arbitrary precision and returns the block
    containing that position.

    Parameters
    ----------
    position : tuple of len 3

    Returns
    -------
    block_position : tuple of ints of len 3

    """
    x, y, z = position
    x, y, z = (int(round(x)), int(round(y)), int(round(z)))
    return (x, y, z)


def sectorize(position):
    """ Returns a tuple representing the sector for the given `position`.

    Parameters
    ----------
    position : tuple of len 3

    Returns
    -------
    sector : tuple of len 3

    """
    x, y, z = normalize(position)
    x, y, z = x // SECTOR_SIZE, y // SECTOR_SIZE, z // SECTOR_SIZE
    return (x, 0, z)

def get_texture_coordinates(x, y, height, width, texture_height, texture_width):
    if x == -1 and y == -1:
        return ()
    x /= float(texture_width)
    y /= float(texture_height)
    height /= float(texture_height)
    width /= float(texture_width)
    return x, y, x + width, y, x + width, y + height, x, y + height

def load_image(path):
    return pyglet.image.load(path)

def round_down(int):
    return round(int) if round(int) < int else round(int) - 1

def betrag(int):
    return int if int >= 0 else -int