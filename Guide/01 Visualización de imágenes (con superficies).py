#!/usr/bin/env python3
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

import pygame
from sys import exit

def firstVersion() -> None:
    pygame.init()

    # Método display.set_mode() de Pygame para crear una ventana de 800x400 píxeles.
    screen: pygame.surface.Surface = pygame.display.set_mode(size = tuple((800,400)))
    pygame.display.set_caption(title = "Runner")

    # Creación de una superficie con un color sólido rojo para representar el cielo.
    sky_surface: pygame.surface.Surface = pygame.Surface(size = tuple((100,200)))
    sky_surface.fill(color = "red")
    
    # Clock es un objeto para rastrear el tiempo. Se inicializa con un tickrate de 60 fps.
    clock: pygame.time.Clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get(): 
            # Sentencia if para verificar si el evento actual es el de cerrar la ventana.
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        # Método blit() de Pygame para dibujar una superficie sobre otra.
        screen.blit(source = sky_surface, dest = tuple((200,100)))
        pygame.display.update()
        clock.tick(60.0)
    return None

def secondVersion() -> None:
    pygame.init()
    # Creación de una ventana de 800x400 píxeles.
    screen: pygame.surface.Surface = pygame.display.set_mode(size = tuple((800,400)))
    pygame.display.set_caption(title = "Runner")

    # Cargar imágenes para el cielo y el suelo desde archivos.
    sky_surface: pygame.surface.Surface = pygame.image.load("./graphics/Sky.png")
    ground_surface: pygame.surface.Surface = pygame.image.load("./graphics/ground.png")

    clock: pygame.time.Clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        screen.blit(source = sky_surface, dest = tuple((0,0)))
        screen.blit(source = ground_surface,dest = tuple((0,300)))
        pygame.display.update()
        clock.tick(60.0)
    return None

def threeVersion() -> None:
    pygame.init()
    # Creación de una ventana de 800x400 píxeles.
    screen: pygame.surface.Surface = pygame.display.set_mode(size = tuple((800,400)))
    # Cargar una fuente desde un archivo.
    test_font: pygame.font.Font = pygame.font.Font("./font/Pixeltype.ttf", size = 50)

    # Crear superficies para el cielo, el suelo y el texto.
    sky_surface: pygame.surface.Surface = pygame.image.load("./graphics/Sky.png")
    ground_surface: pygame.surface.Surface = pygame.image.load("./graphics/ground.png")
    # Renderizar el texto "My Game" con la fuente cargada.
    text_surface: pygame.surface.Surface = test_font.render("My Game", False, "Green", "Black")
    
    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption(title = "Runner")

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        # Dibujar las superficies en la pantalla.
        screen.blit(source = sky_surface, dest = tuple((0,0)))
        screen.blit(source = ground_surface,dest = tuple((0,300)))
        screen.blit(source = text_surface, dest = tuple((300,50)))
        pygame.display.update()
        clock.tick(60.0)
    return None

if __name__ == "__main__":
    firstVersion()
    # secondVersion()
    # threeVersion()

# Lista de colores de Pygame: https://www.pygame.org/docs/ref/color_list.html
