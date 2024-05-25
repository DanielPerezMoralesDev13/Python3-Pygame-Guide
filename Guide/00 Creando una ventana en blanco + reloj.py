#!/usr/bin/env python3
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

# Importamos dependencias
import pygame
from sys import exit

# Inicializar pygame
pygame.init()

# Crear una ventana de tamaño 800x400 píxeles
screen: pygame.surface.Surface = pygame.display.set_mode(size= tuple((800, 400)))

# Crear un objeto Clock para gestionar el tiempop
clock: pygame.time.Clock = pygame.time.Clock()

# Establecer el título de la ventana
pygame.display.set_caption(title = "Window Pygame")

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si se presiona el botón de cerrar la ventana
            pygame.quit()  # Cerrar pygame
            exit(0)  # Salir del programa

    # Actualizar la pantalla
    pygame.display.update()

    # Limitar la velocidad de cuadros a 60 por segundo
    clock.tick(60)