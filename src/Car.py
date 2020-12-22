import math
import pygame

class Car:
    def __init__(self):
        self.angle = 0
        self.speed = 5
        self.radars = []
        self.collision_points = []
        self.is_alive = True
        self.goal = False
        self.distance = 0
        self.time_spent = 0
        self.car_sprite = ""
        self.car = ""

        self.random_sprite()

    def random_sprite(self):
        self.car_sprite = pygame.image.load('../res/car.png')
        self.car_sprite = pygame.transform.scale(self.car_sprite,
                                                 (math.floor(self.car_sprite.get_size()[0] / 2),
                                                  math.floor(self.car_sprite.get_size()[1] / 2)))
        self.car = self.car_sprite
        self.pos = [650, 930]
        self.find_pivot()
