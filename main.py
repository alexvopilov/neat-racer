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

	def random_sprite(self):
		self.car_sprite=pygame.image.load('res/car.png')
		self.car_sprite=pygame.transform.scale(self.car_sprite,
			(math.floor(self.car_sprite.get_size()[0]/2),math.floor(self.car_sprite.get_size()[1]/2)))
		self.car=self.car_sprite
		self.pos=[650,930]
		self.compute_center()

	def compute_center(self):
		self.center=(self.pos[0]+(self.car.get_size()[0]/2),self.pos[1]+(self.car.get_size()[1] / 2))

	def draw(self,screen):
		screen.blit(self.car,self.pos)
		self.draw_radars(screen)

	def draw_center(self,screen):
		pygame.draw.circle(screen,(0,72,186),(math.floor(self.center[0]),math.floor(self.center[1])),5)

	def draw_radars(self,screen):
		for r in self.radars:
			p,d=r
			pygame.draw.line(screen,(183,235,70),self.center,p,1)
			pygame.draw.circle(screen,(183,235,70),p,5)

start=False
def run_generation(genomes,config):
	nets=[]
	cars=[]

	for i,g in genomes:
		net=neat.nn.FeedForwardNetwork.create(g,config)
		nets.append(net)
		g.fitness=0
		cars.append(Car())

	pygame.init()
	screen=pygame.display.set_mode((width,height))
	clock=pygame.time.Clock()
	road=pygame.image.load('res/road.png')

	font=pygame.font.SysFont("Roboto",40)
	heading_font=pygame.font.SysFont("Roboto",80)

	global generation
	global start
	generation+=1
