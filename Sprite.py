#coding=utf-8
from __future__ import division
import pygame
import numpy as np


class Sprite(object):
    def __init__(self,
                 sprite_image_filename,
                 position = np.array([0., 0.]),
                 movement_speed = 300.,
                 rotation = 0.,
                 rotation_speed = 360.,
                 clock = pygame.time.Clock()
                 ):
        self.sprite_ori = pygame.image.load(sprite_image_filename).convert_alpha()
        self.sprite = self.sprite_ori
        self.position = position
        self.rotation = rotation
        self.movement_direction = 0.
        self.rotation_direction = 0.
        self.movement_speed = movement_speed  # movement pixels per sec
        self.rotation_speed = rotation_speed  # rotation angles per sec
        self.sprite_draw_pos = position
        self.turn_direction = 0.
        self.velocity = np.array([1., 0.])
        self.clock = clock
        self.time_passed = 0.
        self.time = 0.
        self.track_function = lambda t: np.array([0., 0.])

    def move(self, movement_direction = 0.):
        #movement_direction: 2d_array
        self.movement_direction = movement_direction

    def _move(self):
        self.position += self.velocity * self.movement_direction * self.movement_speed * self.time_passed /1000
        self.movement_direction = 0.

    def rotate(self, rotation_direction):
        self.rotation_direction = rotation_direction
        self.velocity = np.array([
            np.cos(self.rotation * np.pi / 180.),
            - np.sin(self.rotation * np.pi / 180.)
        ])

    def _rotate(self):
        self.rotation += self.rotation_direction * self.rotation_speed * self.time_passed / 1000
        self.sprite = pygame.transform.rotate(self.sprite_ori, self.rotation)
        self.rotation_direction = 0.

    def update(self, time_passed):
        #screen: pygame.screen
        self.time_passed = time_passed
        print(time_passed/1000)
        self.time += time_passed
        self._rotate()
        self._move()
        self._track()
        w, h = self.sprite.get_size()
        self.sprite_draw_pos = np.array([self.position[0] - w / 2, self.position[1] - h / 2])
        #print('r=%d,v=(%f,%f)' %(self.rotation, self.velocity[0], self.velocity[1]))

    def track(self, ft = lambda t: np.array([t/10, t * (600. -t/10) / 30000.])):
        ft = lambda t: np.array([])
        self.track_function = ft

    def _track(self):
        t = self.time
        self.position = self.track_function(t)
        print('t=%d,x=(%f,%f)' % (self.time, self.position[0], self.position[1]))
