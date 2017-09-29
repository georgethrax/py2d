#coding=utf-8
# Game object
from __future__ import division
import numpy as np
import pygame
from pygame.locals import *
from sys import exit

from Sprite import Sprite


class Game(object):
    def __init__(self):
        self.count = 0
        print('Game object init')
        self.background_image_filename = 'resources/sushiplate.jpg'
        self.sprite_image_filename = 'resources/fugu.png'

        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.background = pygame.image.load(self.background_image_filename).convert()

        self.sprite = Sprite(sprite_image_filename = self.sprite_image_filename,
                             position=np.array([200., 150.]),
                             movement_speed=300.,
                             rotation=0.,
                             rotation_speed=360.,
                             clock=self.clock
                             )




        #pygame.mouse.set_visible(True)
        #pygame.event.set_grab(True)

    def run(self):
        while True:
            #print(self.count)
            #self.count += 1
            self.processEvent()
            self.update()


    def processEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            # 按Esc则退出游戏
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
        pressed_keys = pygame.key.get_pressed()
        # 这里获取鼠标的按键情况
        #pressed_mouse = pygame.mouse.get_pressed()

        # 通过移动偏移量计算转动
        movement_direction = 0.
        rotation_direction = 0. #pygame.mouse.get_rel()[0] / 5.0

        if pressed_keys[K_LEFT]:
            rotation_direction = +1.
        if pressed_keys[K_RIGHT]:
            rotation_direction = -1.
        # 多了一个鼠标左键按下的判断
        if pressed_keys[K_UP]:# or pressed_mouse[0]:
            movement_direction = +1.
        # 多了一个鼠标右键按下的判断
        if pressed_keys[K_DOWN]:# or pressed_mouse[2]:
            movement_direction = -1.

        if pressed_keys[K_1]:
            self.sprite.track()

        self.sprite.move(movement_direction)
        self.sprite.rotate(rotation_direction)

    def update(self):
        self.screen.blit(self.background, (0, 0))

        time_passed = self.clock.tick(30)
        time_passed_seconds = time_passed / 1000.0
        #self.sprite.update(time_passed_seconds)
        self.sprite.update(time_passed)
        self.screen.blit(self.sprite.sprite, self.sprite.sprite_draw_pos)
        pygame.display.update()

