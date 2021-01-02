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

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					start=True

		if not start:
			continue

		for i,car in enumerate(cars):
			output=nets[i].activate(car.get_data())
			i=output.index(max(output))

			if i == 0:
				car.angle+=5
			elif i == 1:
				car.angle=car.angle
			elif i == 2:
				car.angle-=5

		cars_left=0
		for i,car in enumerate(cars):
			if car.is_alive:
				cars_left+=1
				car.update(road)
				genomes[i][1].fitness+=car.get_reward()

		if not cars_left:
			break

		screen.blit(road,(0,0))

		for car in cars:
			if car.is_alive:
				car.draw(screen)

		label=heading_font.render("Поколение: "+str(generation),True,(73,168,70))
		label_rect=label.get_rect()
		label_rect.center=(width / 1.5,300)
		screen.blit(label,label_rect)

		pygame.display.flip()
		clock.tick(0)

config_path="config-feedforward.txt"
config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

p=neat.Population(config)
p.run(run_generation,1000)