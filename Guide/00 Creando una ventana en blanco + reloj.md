<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Email: danielperezdev@proton.me -->
# ***Documentacion***

- *El reloj (clock) en Pygame se utiliza para controlar la velocidad del juego al limitar el número de cuadros por segundo (FPS). Si no se utilizara el reloj y no se limitara la velocidad de cuadros, el juego podría ejecutarse tan rápido como lo permita el hardware, lo que puede causar que consuma una gran cantidad de recursos del sistema y que sea difícil de controlar para los jugadores, ya que la velocidad de juego sería inconsistente en diferentes sistemas.*

**En cuanto a los elementos utilizados:**

- **`pygame.init()`:** *Inicializa todas las submódulos de Pygame necesarios para su correcto funcionamiento.*

- **`screen: pygame.surface.Surface = pygame.display.set_mode(size= tuple((800, 400)))`:** *Crea una ventana de tamaño 800x400 píxeles en la que se mostrarán los gráficos del juego.*

- **`pygame.display.set_caption(title="Window Pygame")`:** *Establece el título de la ventana.*

- **`pygame.event.get()`:** *Obtiene todos los eventos ocurridos desde la última vez que se llamó a esta función, como presionar teclas, mover el mouse, etc.*

- **`pygame.quit()`:** *Detiene todos los módulos de Pygame y libera los recursos utilizados por ellos.*

- **`exit(0)`:** *Sale del programa con un código de salida de 0, indicando que no hubo errores.*

- **`pygame.display.update()`:** *Actualiza la pantalla con los cambios realizados desde la última llamada a esta función.*

- **`clock.tick(60)`:** *Limita la velocidad de cuadros a 60 por segundo, lo que ayuda a controlar la velocidad del juego y a ahorrar recursos del sistema.*

- **`QUIT`:** *Este evento se genera cuando el usuario intenta cerrar la ventana del juego.*

- **`ACTIVEEVENT`:** *Se genera cuando la ventana del juego pierde o gana el foco.*

- **`KEYDOWN`:** *Se genera cuando se presiona una tecla del teclado.*

- **`KEYUP`:** *Se genera cuando se suelta una tecla del teclado.*

- **`MOUSEMOTION`:** *Se genera cuando se mueve el ratón.*

- **`MOUSEBUTTONUP`:** *Se genera cuando se suelta un botón del ratón.*

- **`MOUSEBUTTONDOWN`:** *Se genera cuando se presiona un botón del ratón.*

- **`JOYAXISMOTION`:** *Se genera cuando se mueve un eje del joystick.*

- **`JOYBALLMOTION`:** *Se genera cuando se mueve un joystick con bola.*

- **`JOYHATMOTION`:** *Se genera cuando se mueve un joystick con un sombrero (hat).*

- **`JOYBUTTONUP`:** *Se genera cuando se suelta un botón del joystick.*

- **`JOYBUTTONDOWN`:** *Se genera cuando se presiona un botón del joystick.*

- **`VIDEORESIZE`:** *Se genera cuando se cambia el tamaño de la ventana del juego.*

- **`VIDEOEXPOSE`:** *Se genera cuando una parte de la ventana del juego necesita ser actualizada.*

- **`USEREVENT`:** *Este evento puede ser utilizado por el usuario para generar eventos personalizados.*

*Estos eventos son fundamentales para crear interactividad en un juego, ya que permiten que el programa reaccione a las acciones del usuario, como presionar teclas, mover el ratón o interactuar con un joystick. En el bucle principal del juego, se recorren todos estos eventos para manejarlos adecuadamente y responder de manera apropiada a las acciones del jugador.*
