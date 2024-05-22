#!/usr/bin/env python3
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me
import pygame, sys

def main() -> None:
    """
    Esta parte crea una instancia de la clase Clock. Cuando se crea un objeto Clock, se utiliza para controlar la velocidad de fotogramas del juego. Más específicamente, se utiliza para limitar la velocidad de fotogramas del juego, lo que significa que se puede especificar cuántos fotogramas por segundo (FPS) se desea que tenga el juego. Esto es útil para hacer que el juego se ejecute a una velocidad constante en diferentes sistemas y evitar que el juego funcione demasiado rápido en hardware más rápido.
    """
    clock: pygame.time.Clock =  pygame.time.Clock()
    ancho_ventana: int = 1280
    alto_ventana: int = 460

    """
    Esta parte crea la ventana de visualización con el tamaño especificado. La función set_mode() toma un argumento de tamaño como una tupla (ancho_ventana, alto_ventana) que define las dimensiones de la ventana en píxeles. En este caso, ancho_ventana y alto_ventana son variables que deben contener el ancho y el alto de la ventana respectivamente. La función devuelve una superficie (Surface) que representa la ventana de visualización recién creada.
    """
    pantalla: pygame.surface.Surface = pygame.display.set_mode(size=(ancho_ventana,alto_ventana))

    """
    Esta parte establece el título de la ventana de visualización. La función set_caption() toma un argumento title que especifica el título de la ventana. En este caso, el título de la ventana se establece en "Ping pong".
    """
    pygame.display.set_caption(title="Ping pong")
    while True:
        """
        Este fragmento de código recorre todos los eventos en la cola de eventos de Pygame. Para cada evento, comprueba si es de tipo pygame.QUIT, lo que significa que el usuario ha intentado cerrar la ventana. Si se detecta este evento, se llama a pygame.quit() para cerrar Pygame correctamente y luego sys.exit(0) para salir del programa.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        """
        Después de manejar los eventos, este comando actualiza la pantalla. En Pygame, pygame.display.flip() actualiza toda la ventana de visualización con los cambios realizados desde la última actualización. Es importante llamar a esta función para que los cambios se muestren en la ventana.
        """
        pygame.display.flip()

        """
        Esta línea controla la velocidad de fotogramas del juego. clock.tick(60) limita la ejecución del bucle principal a 60 fotogramas por segundo. Esto asegura que el juego se ejecute a una velocidad constante y evita que funcione demasiado rápido en hardware más rápido. La clase Clock de Pygame se utiliza para controlar el tiempo, y el método tick() se utiliza para establecer el límite de velocidad de fotogramas.
        """
        clock.tick(60)

if __name__ == "__main__":
    main()
