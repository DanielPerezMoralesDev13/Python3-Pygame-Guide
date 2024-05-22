<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Installing Python3 and Pygame on Linux (Debian and Arch)***

*This repository provides a step-by-step guide to install Python3 and Pygame on Debian and Arch-based Linux systems.*

## ***Author***

- **Name:** *Daniel Benjamin Perez Morales*
- **GitHub:** *[DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13)*
- **Email:** *<danielperezdev@proton.me>*

## ***Table of Contents***

- [***Installing Python3 and Pygame on Linux (Debian and Arch)***](#installing-python3-and-pygame-on-linux-debian-and-arch)
  - [***Author***](#author)
  - [***Table of Contents***](#table-of-contents)
  - [***Introduction***](#introduction)
  - [***Installation on Debian***](#installation-on-debian)
    - [***Update the System***](#update-the-system)
    - [***Install Python3***](#install-python3)
    - [***Install Pygame***](#install-pygame)
  - [***Installation on Arch***](#installation-on-arch)
    - [***Update the Arch Linux System***](#update-the-arch-linux-system)
    - [***Install Python3 Debian Ubuntu***](#install-python3-debian-ubuntu)
    - [***Install Pygame Arch Linux***](#install-pygame-arch-linux)
  - [***Verify Installation***](#verify-installation)
    - [***Common Examples List***](#common-examples-list)
    - [***Running Examples***](#running-examples)
    - [***Complete Steps to View and Run Examples***](#complete-steps-to-view-and-run-examples)
    - [***Additional Resources***](#additional-resources)
  - [***Contributions***](#contributions)
  - [***License***](#license)

## ***Introduction***

*Pygame is a Python library designed for game development. It simplifies the creation of games and interactive multimedia in Python. Below are the steps to install Python3 and Pygame on Debian and Arch-based Linux distributions.*

## ***Installation on Debian***

### ***Update the System***

1. **Update the package list:**

    ```bash
    sudo apt-get update
    ```

2. **Upgrade the installed packages:**

    ```bash
    sudo apt-get upgrade
    ```

### ***Install Python3***

1. **Install Python3:**

    ```bash
    sudo apt-get install python3
    ```

2. **Verify the installation of Python3:**

    ```bash
    python3 --version
    ```

### ***Install Pygame***

1. **Install pip3 (if not installed):**

    ```bash
    sudo apt-get install python3-pip
    ```

2. **Install Pygame using pip3:**

    ```bash
    pip3 install pygame
    ```

3. **Verify the installation of Pygame:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

## ***Installation on Arch***

### ***Update the Arch Linux System***

1. **Update the package list and installed packages:**

    ```bash
    sudo pacman -Syu
    ```

### ***Install Python3 Debian Ubuntu***

1. **Install Python3:**

    ```bash
    sudo pacman -Syu python3
    ```

    ```bash
    sudo pacman -Syu python-pygame
    ```

2. **Verify the installation of Python3:**

    ```bash
    python3 --version
    ```

### ***Install Pygame Arch Linux***

1. **Install pip3 (if not installed):**

    ```bash
    sudo pacman -Syu python-pip
    ```

2. **Install Pygame using pip:**

    ```bash
    pip3 install pygame
    ```

3. **Verify the installation of Pygame:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

## ***Verify Installation***

*To ensure Pygame is installed correctly, you can run the following command which starts a sample game included in the Pygame library:*

```bash
python3 -m pygame.examples.aliens  # On Debian
python -m pygame.examples.aliens   # On Arch
```

*You should see a game window with a Pygame example.*

- *To view and run all Pygame examples, you cannot use the command `python3 -m pygame.examples` directly as `pygame.examples` is a package and cannot be executed this way. Instead, you need to specify each example individually. Here is a list of some examples you can run and how to do it:*

### ***Common Examples List***

1. **aliens:** *A simple shooting game.*
2. **chimp:** *A game where you hit a chimp.*
3. **stars:** *A star animation.*
4. **freetype_misc:** *Various demonstrations of the freetype module.*

### ***Running Examples***

*You can run each example using the following format:*

```bash
python3 -m pygame.examples.example_name
```

*Below are some specific examples:*

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

### ***Complete Steps to View and Run Examples***

1. **Verify that Python and Pygame are installed correctly:**

    ```bash
    python3 --version
    python3 -m pygame --version
    ```

2. **Run a specific Pygame example:**

    ```bash
    python3 -m pygame.examples.aliens
    ```

*If you want to see more examples, you can check the source code of Pygame examples in the official Pygame repository or the documentation on their website.*

### ***Additional Resources***

- *[Pygame Documentation](https://www.pygame.org/docs/)*
- *[Pygame GitHub Repository](https://github.com/pygame/pygame/tree/main/examples)*

*These resources will help you find and run more Pygame examples.*

## ***Contributions***

*Contributions are welcome! If you have suggestions, corrections, or improvements for this guide, feel free to open an issue or submit a pull request.*

## ***License***

> *This repository is published under the MIT License. Feel free to use, modify, and distribute the content according to the terms of this license.*
