"""Main module."""
import sys

import pygame
from pygame.constants import K_ESCAPE, KEYDOWN


def main():
    """Run the main function of the game."""
    pygame.init()
    pygame.display.set_caption("Bordertale 3D")
    screen = pygame.display.set_mode((900, 900), 0, 32)
    display = pygame.Surface((300, 300))

    with open("map.txt") as f:
        map_data = [
            [int(c) for c in row] for row in f.read().split("\n")
        ]  # Read Binary Map File

    while True:
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.update()
