import neat
import sys

from car import *

def run_generation(genomes, config):
    nets = []
    cars = []

    # init genomes
    for i, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0  # every genome is not successful at the start

        # init cars
        cars.append(Car())

    # init the game
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    road = pygame.image.load('res/road.png')

    font = pygame.font.SysFont("Roboto", 40)
    heading_font = pygame.font.SysFont("Roboto", 80)

    # the LOOP
    global generation
    global start
    generation += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True

        if not start:
            continue

        # input each car data
        for i, car in enumerate(cars):
            output = nets[i].activate(car.get_data())
            i = output.index(max(output))

            if i == 0:
                car.angle += 5
            elif i == 1:
                car.angle = car.angle
            elif i == 2:
                car.angle -= 5

        # now, update car and set fitness (for alive cars only)
        cars_left = 0
        for i, car in enumerate(cars):
            if car.is_alive:
                cars_left += 1
                car.update(road)
                # new fitness (aka car instance success)
                genomes[i][1].fitness += car.get_reward()

        # check if cars left
        if not cars_left:
            break

        # display stuff
        screen.blit(road, (0, 0))

        for car in cars:
            if car.is_alive:
                car.draw(screen)
            # car.draw_center(screen)
            # car.draw_collision_points(road, screen)

        label = heading_font.render("Поколение: " + str(generation), True, (73, 168, 70))
        label_rect = label.get_rect()
        label_rect.center = (width / 1.5, 300)
        screen.blit(label, label_rect)

        label = font.render("Машин осталось: " + str(cars_left), True, (51, 59, 70))
        label_rect = label.get_rect()
        label_rect.center = (width / 1.5, 375)
        screen.blit(label, label_rect)

        pygame.display.flip()
        clock.tick(0)