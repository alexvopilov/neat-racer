import pygame
import random
import sys
import math
import neat

width=1300
height=1100
bg=(213,193,154,255)

generation=0

class Car:
	def __init__(self):
		self.random_sprite()

		self.angle=0
		self.speed=5

		self.radars=[]
		self.collision_points=[]

		self.is_alive=True
		self.goal=False
		self.distance=0
		self.time_spent=0
