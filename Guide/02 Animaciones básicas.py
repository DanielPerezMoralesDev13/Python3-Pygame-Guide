#!/usr/bin/env python3
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me
import pygame
from sys import exit

# Se importa el módulo locals de Pygame para acceder a las constantes definidas.
import pygame.locals

# Inicialización de Pygame.
pygame.init()

# Creación de la ventana de 800x400 píxeles.
screen: pygame.surface.Surface = pygame.display.set_mode(size = tuple((800,400)))

# Carga de una fuente desde un archivo.
test_font = pygame.font.Font("./font/Pixeltype.ttf", size = 50)

# Carga de imágenes para el cielo, el suelo y el texto, y conversión a formato adecuado.
sky_surface: pygame.surface.Surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface: pygame.surface.Surface = pygame.image.load("./graphics/ground.png").convert()
text_surface: pygame.surface.Surface = test_font.render("My Game", False, "Green", "Black")

# Carga de una imagen para el caracol y conversión al formato adecuado.
snail_surface: pygame.surface.Surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()

# Posición inicial del caracol en el eje x.
snail_x_position: int = 600

# Objeto Clock para rastrear el tiempo.
clock: pygame.time.Clock = pygame.time.Clock()

# Bucle principal del juego.
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    
    # Dibujo de las superficies en la pantalla.
    screen.blit(source = sky_surface, dest = tuple((0,0)))
    screen.blit(source = ground_surface,dest = tuple((0,300)))
    screen.blit(source = text_surface, dest = tuple((300,50)))
    
    # Actualización de la posición del caracol.
    snail_x_position -= 4
    if (snail_x_position <= -100): snail_x_position = 800
    screen.blit(source = snail_surface, dest = tuple((snail_x_position,250)))

    # Actualización de la pantalla.
    pygame.display.update()
    clock.tick(60.0)
