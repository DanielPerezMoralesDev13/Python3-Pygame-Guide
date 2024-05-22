#!/usr/bin/env python3
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

# Daniel Perez Morales
import pygame, sys, random

# Función para animar la pelota y manejar su comportamiento
def ball_animation() -> None:
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Revisa si la pelota choca con los bordes superior o inferior de la pantalla
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Revisa si la pelota sale por los lados izquierdo o derecho de la pantalla
    if ball.left <= 0 or ball.right >= screen_width:
        ball_start()

    # Revisa si la pelota colisiona con el jugador o el oponente
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    return None

# Función para animar al jugador y controlar su movimiento
def player_animation() -> None:
    player.y += player_speed

    # Evita que el jugador salga de los límites superior o inferior de la pantalla
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    return None

# Función para controlar el movimiento del oponente
def opponent_ai() -> None:
    # Mueve al oponente hacia la posición y de la pelota
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed


    # Evita que el oponente salga de los límites superior o inferior de la pantalla
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    return None

# Función para iniciar la posición y velocidad de la pelota
def ball_start() -> None:
    global ball_speed_x, ball_speed_y

    ball.center = (int(screen_width / 2), int(screen_height / 2))
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
    return None

# Configuración general de Pygame
pygame.init()
clock: pygame.time.Clock = pygame.time.Clock()

# Ventana principal del juego
screen_width: int = 1280
screen_height: int = 460
screen: pygame.surface.Surface = pygame.display.set_mode(size=(screen_width, screen_height))
pygame.display.set_caption(title="Ping pong")

# Colores
light_grey: tuple[int,int,int] = (200, 200, 200)
bg_color: pygame.color.Color = pygame.Color('grey12')

# Rectángulos del juego
ball: pygame.rect.Rect = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player: pygame.rect.Rect = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent: pygame.rect.Rect = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Variables del juego
ball_speed_x: int = 7 * random.choice((1, -1))
ball_speed_y: int = 7 * random.choice((1, -1))
player_speed: int = 0
opponent_speed: int = 7

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    # Lógica del juego
    ball_animation()
    player_animation()
    opponent_ai()

    # Renderizado visual
    screen.fill(color=bg_color)
    pygame.draw.rect(surface=screen,color=light_grey,rect=player)
    pygame.draw.rect(surface=screen,color=light_grey,rect=opponent)
    pygame.draw.ellipse(surface=screen,color=light_grey,rect= ball)
    pygame.draw.aaline(surface=screen,color= light_grey,start_pos= (screen_width / 2, 0),end_pos= (screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
