from moduls import *
from mathhelper import *
from math import *
import texturGroups

class BoxModel(object):
    # top bottom left right front back
    textures = [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]
    texture_data = None
    display = None
    position = (0,0,0)
    rotate_angle = (0, 0, 0)

    def __init__(self, length, width, height, texture, pixel_length, pixel_width, pixel_height):
        self.image = texture

        self.length, self.width, self.height = length, width, height
        self.pixel_length, self.pixel_width, self.pixel_height = pixel_length, pixel_width, pixel_height
        self.texture_height = self.image.height
        self.texture_width = self.image.width

    def get_texture_data(self):
        texture_data = []
        texture_data += get_texture_coordinates(self.textures[0][0], self.textures[0][-1], self.pixel_width, self.pixel_length, self.texture_height, self.texture_width)
        texture_data += get_texture_coordinates(self.textures[1][0], self.textures[1][-1], self.pixel_width, self.pixel_length, self.texture_height, self.texture_width)
        texture_data += get_texture_coordinates(self.textures[2][0], self.textures[2][-1], self.pixel_height, self.pixel_width, self.texture_height, self.texture_width)
        texture_data += get_texture_coordinates(self.textures[3][0], self.textures[3][-1], self.pixel_height, self.pixel_width, self.texture_height, self.texture_width)
        texture_data += get_texture_coordinates(self.textures[4][0], self.textures[4][-1], self.pixel_height, self.pixel_length, self.texture_height, self.texture_width)
        texture_data += get_texture_coordinates(self.textures[-1][0], self.textures[-1][-1], self.pixel_height, self.pixel_length, self.texture_height, self.texture_width)
        return texture_data

    def update_texture_data(self, textures):
        self.textures = textures
        self.texture_data = self.get_texture_data()

        self.display = pyglet.graphics.vertex_list(24,
            ('v3f/static', self.get_vertices()),
            ('t2f/static', self.texture_data),
        )

    def get_vertices(self):
        xm = 0
        xp = self.length
        ym = 0
        yp = self.height
        zm = 0
        zp = self.width

        vertices = (
            xm, yp, zm,   xm, yp, zp,   xp, yp, zp,   xp, yp, zm,  # top
            xm, ym, zm,   xp, ym, zm,   xp, ym, zp,   xm, ym, zp,  # bottom
            xm, ym, zm,   xm, ym, zp,   xm, yp, zp,   xm, yp, zm,  # left
            xp, ym, zp,   xp, ym, zm,   xp, yp, zm,   xp, yp, zp,  # right
            xm, ym, zp,   xp, ym, zp,   xp, yp, zp,   xm, yp, zp,  # front
            xp, ym, zm,   xm, ym, zm,   xm, yp, zm,   xp, yp, zm,  # back
        )
        return vertices

    def draw(self):
        glPushMatrix()
        glBindTexture(self.image.texture.target, self.image.texture.id)
        glEnable(self.image.texture.target)
        glTranslatef(*self.position)
        glRotatef(self.rotate_angle[0] * (180 / float(pi)), 1.0, 0.0, 0.0)
        glRotatef(self.rotate_angle[1] * (180 / float(pi)), 0.0, 1.0, 0.0)
        glRotatef(self.rotate_angle[-1] * (180 / float(pi)), 0.0, 0.0, 1.0)
        if self.display:
            self.display.draw(GL_QUADS)
        glPopMatrix()
