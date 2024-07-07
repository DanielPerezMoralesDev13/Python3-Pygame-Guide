# ***Instalacion***

1. **`sudo apt install python3-pip`:**

   - **Descripción:** *Este comando utiliza el sistema de gestión de paquetes APT (Advanced Package Tool) para instalar el paquete `python3-pip`, que es necesario para instalar paquetes de Python.*

   - **Uso:**

     ```bash
     sudo apt install python3-pip
     ```

   - **Notas:** *`sudo` se utiliza para ejecutar el comando con privilegios de superusuario, lo que permite la instalación de paquetes en el sistema.*

2. **`pip install pygame`:**

   - **Descripción:** *Utiliza `pip`, el gestor de paquetes de Python, para instalar el paquete Pygame, que proporciona funcionalidades para el desarrollo de videojuegos en Python.*

   - **Uso:**

     ```bash
     pip install pygame
     ```

   - **Notas:** *`pip` es el gestor de paquetes estándar para Python, y se utiliza para instalar paquetes adicionales no incluidos en la biblioteca estándar de Python.*

3. **`pip install mypy`:**

   - **Descripción:** *Utiliza `pip` para instalar el paquete `mypy`, que es una herramienta de verificación estática de tipos para Python.*

   - **Uso:**

     ```bash
     pip install mypy
     ```

   - **Notas:** *`mypy` se utiliza para realizar análisis estático del código Python en busca de errores de tipo y para proporcionar una mayor seguridad y claridad en el código.*

4. **`export PATH="/home/user/.local/bin:$PATH"`:**

   - **Descripción:** *Este comando exporta un directorio al `PATH` del sistema, lo que permite que los ejecutables instalados en ese directorio se puedan ejecutar desde cualquier lugar en la línea de comandos.*

   - **Uso:**

     ```bash
     export PATH="/home/d4nitrix13/.local/bin:$PATH"
     ```

   - **Notas:** *En este caso, se está agregando el directorio `/home/d4nitrix13/.local/bin` al `PATH`, lo que permite ejecutar scripts y comandos instalados localmente en ese directorio sin especificar la ruta completa.*

5. **`mypy main.py`:**

   - **Descripción:** *Este comando utiliza `mypy` para realizar un análisis estático del fichero `main.py`, en busca de posibles errores de tipo en el código Python.*

   - **Uso:**

     ```bash
     mypy main.py
     ```

   - **Notas:** *`main.py` es el fichero Python que se desea analizar estáticamente en busca de errores de tipo. Este comando es útil para mejorar la calidad y la robustez del código Python.*
