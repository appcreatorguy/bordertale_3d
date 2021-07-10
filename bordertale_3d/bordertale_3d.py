"""Main module."""
import sys
import time
from random import randint

import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, RESIZABLE


def main():
    """Run the main function of the game."""
    pygame.init()
    pygame.display.set_caption("Bordertale 3D")
    screen = pygame.display.set_mode((600, 600), 0, 32)
    display = pygame.Surface((300, 300))
    FPSCLOCK = pygame.time.Clock()
    FPS = 60

    grass_img = pygame.image.load("resources/grass.png").convert()
    grass_img.set_colorkey((0, 0, 0))

    with open("data/map copy.txt") as f:
        map_data = [[int(c) for c in row] for row in f.read().split("\n")]
    f.close()  # * Read Binary Map File

    while True:
        display.fill((0, 0, 0))

        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(
                        display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1
                    )
                    display.blit(
                        grass_img,
                        (
                            125
                            + x * (grass_img.get_width() / 2)
                            - y * (grass_img.get_width() / 2),
                            100
                            + x * (grass_img.get_width() / 4)
                            + y * (grass_img.get_width() / 4),
                        ),
                    )
                    double_height_chance = True if randint(0, 1) == 1 else False
                    display.blit(
                        grass_img,
                        (
                            125
                            + x * (grass_img.get_width() / 2)
                            - y * (grass_img.get_width() / 2),
                            100
                            + x * (grass_img.get_width() / 4)
                            + y * (grass_img.get_width() / 4)
                            - grass_img.get_height() / 2
                            + 1,
                        ),
                    ) if double_height_chance else None
                    pygame.draw.rect(
                        display, (135, 135, 135), pygame.Rect(x * 10, y * 10, 10, 10), 1
                    ) if double_height_chance else None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(
            pygame.transform.scale(display, screen.get_size()), (0, 0)
        )  # * Screen Scaling
        pygame.display.update()
        # FPSCLOCK.tick(FPS)
        time.sleep(2)
