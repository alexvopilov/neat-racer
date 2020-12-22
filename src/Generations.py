import neat
import sys

from . import Car
from .Car import pygame


def run_generation(genomes, config):
    nets = []
    cars = []
    for i, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0  # every genome is not successful at the start

        # init cars
        cars.append(Car())
