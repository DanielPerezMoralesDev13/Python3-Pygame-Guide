<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***Instalación de Python3 y Pygame en Linux (Debian y Arch)***

*Este repositorio proporciona una guía paso a paso para instalar Python3 y Pygame en sistemas Linux basados en Debian y Arch.*

## ***Autor***

- **Nombre:** *Daniel Benjamin Perez Morales*
- **GitHub:** *[DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13)*
- **Correo Electrónico:** *<danielperezdev@proton.me>*

## ***Índice***

- [***Instalación de Python3 y Pygame en Linux (Debian y Arch)***](#instalación-de-python3-y-pygame-en-linux-debian-y-arch)
  - [***Autor***](#autor)
  - [***Índice***](#índice)
  - [***Introducción***](#introducción)
  - [***Instalación en Debian***](#instalación-en-debian)
    - [***Actualizar el Sistema***](#actualizar-el-sistema)
    - [***Instalar Python3***](#instalar-python3)
    - [***Instalar Pygame***](#instalar-pygame)
  - [***Instalación en Arch***](#instalación-en-arch)
    - [***Actualizar el Sistema Arch Linux***](#actualizar-el-sistema-arch-linux)
    - [***Instalar Python3 Debian Ubuntu***](#instalar-python3-debian-ubuntu)
    - [***Instalar Pygame Arch Linux***](#instalar-pygame-arch-linux)
  - [***Verificación de la Instalación***](#verificación-de-la-instalación)
    - [***Lista de Ejemplos Comunes***](#lista-de-ejemplos-comunes)
    - [***Ejecución de Ejemplos***](#ejecución-de-ejemplos)
    - [***Pasos Completos para Ver y Ejecutar Ejemplos***](#pasos-completos-para-ver-y-ejecutar-ejemplos)
    - [***Recursos Adicionales***](#recursos-adicionales)
  - [***Contribuciones***](#contribuciones)
  - [***Licencia***](#licencia)

## ***Introducción***

*Pygame es una biblioteca de Python diseñada para el desarrollo de videojuegos. Facilita la creación de juegos y multimedia interactiva en Python. A continuación, se detallan los pasos para instalar Python3 y Pygame en distribuciones Linux basadas en Debian y Arch.*

## ***Instalación en Debian***

### ***Actualizar el Sistema***

1. **Actualizar la lista de paquetes:**

    ```bash
    sudo apt-get update
    ```

2. **Actualizar los paquetes instalados:**

    ```bash
    sudo apt-get upgrade
    ```

### ***Instalar Python3***

1. **Instalar Python3:**

    ```bash
    sudo apt-get install python3
    ```

2. **Verificar la instalación de Python3:**

    ```bash
    python3 --version
    ```

### ***Instalar Pygame***

1. **Instalar pip3 (si no está instalado):**

    ```bash
    sudo apt-get install python3-pip
    ```

2. **Instalar Pygame usando pip3:**

    ```bash
    pip3 install pygame
    ```

3. **Verificar la instalación de Pygame:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

## ***Instalación en Arch***

### ***Actualizar el Sistema Arch Linux***

1. **Actualizar la lista de paquetes y los paquetes instalados:**

    ```bash
    sudo pacman -Syu
    ```

### ***Instalar Python3 Debian Ubuntu***

1. **Instalar Python3:**

    ```bash
    sudo pacman -Syu python3
    ```

2. **Verificar la instalación de Python3:**

    ```bash
    python3 --version
    ```

### ***Instalar Pygame Arch Linux***

1. **Instalar pip3 (si no está instalado):**

    ```bash
    sudo pacman -Syu python-pip
    ```

    ```bash
    sudo pacman -Syu python-pygame
    ```

2. **Instalar Pygame usando pip3:**

    ```bash
    pip3 install pygame
    ```

3. **Verificar la instalación de Pygame:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

## ***Verificación de la Instalación***

*Para asegurarte de que Pygame se ha instalado correctamente, puedes ejecutar el siguiente comando que inicia un ejemplo de juego incluido en la biblioteca de Pygame:*

```bash
python3 -m pygame.examples.aliens  # En Debian
python -m pygame.examples.aliens   # En Arch
```

*Deberías ver una ventana de juego con un ejemplo de Pygame.*

- *Para ver y ejecutar todos los ejemplos de Pygame, no se puede usar el comando `python3 -m pygame.examples` directamente ya que `pygame.examples` es un paquete y no se puede ejecutar de esa manera. En su lugar, debes especificar cada ejemplo individualmente. Aquí tienes una lista de algunos ejemplos que puedes ejecutar y cómo hacerlo:*

### ***Lista de Ejemplos Comunes***

1. **aliens:** *Un juego simple de disparos.*
2. **chimp:** *Un juego donde se golpea a un chimpancé.*
3. **stars:** *Una animación de estrellas.*
4. **freetype_misc:** *Demostraciones varias del módulo freetype.*

### ***Ejecución de Ejemplos***

*Puedes ejecutar cada ejemplo usando el siguiente formato:*

```bash
python3 -m pygame.examples.nombre_del_ejemplo
```

*A continuación, se muestran algunos ejemplos específicos:*

1. **Aliens:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

2. **Chimp:**

    ```bash
    python3 -m pygame.examples.chimp
    ```

3. **Stars:**

    ```bash
    python3 -m pygame.examples.stars
    ```

4. **Freetype Misc:**

    ```bash
    python3 -m pygame.examples.freetype_misc
    ```

### ***Pasos Completos para Ver y Ejecutar Ejemplos***

1. **Verifica que Python y Pygame están instalados correctamente:**

    ```bash
    python3 --version
    python3 -m pygame --version
    ```

2. **Ejecuta un ejemplo específico de Pygame:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

*Si deseas ver más ejemplos, puedes consultar el código fuente de los ejemplos de Pygame en el repositorio oficial de Pygame o la documentación en su sitio web.*

### ***Recursos Adicionales***

- *[Pygame Documentation](https://www.pygame.org/docs/)*
- *[Pygame GitHub Repository](https://github.com/pygame/pygame/tree/main/examples)*

*Estos recursos te ayudarán a encontrar y ejecutar más ejemplos de Pygame.*

## ***Contribuciones***

*¡Las contribuciones son bienvenidas! Si tienes sugerencias, correcciones o mejoras para esta guía, siéntete libre de abrir un problema o enviar una solicitud de extracción.*

## ***Licencia***

> *Este repositorio se publica bajo la Licencia MIT. Siéntete libre de utilizar, modificar y distribuir el contenido de acuerdo con los términos de esta licencia.*
