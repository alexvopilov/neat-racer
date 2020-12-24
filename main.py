from run import *


if __name__ == "__main__":
    config_path = "res/config.txt"
    config = neat.config.Config(filename=config_path,
                                genome_type=neat.DefaultGenome,
                                reproduction_type=neat.DefaultReproduction,
                                species_set_type=neat.DefaultSpeciesSet,
                                stagnation_type=neat.DefaultStagnation)
    p = neat.Population(config)
    p.run(run_generation, 1000)