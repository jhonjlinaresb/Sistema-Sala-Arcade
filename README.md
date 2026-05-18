# Sistema de Gestión de una Sala de Juegos y Videojuegos estilo Arcade

### Objetivo:

Crear un **Sistema de gestión de un sala de juegos estilo Arcade** Inspirado en [Ilusiona Castellón](https://ilusiona.com/) me enfocaré principalmente en las características y acciones que conozco y he vivido en este Centro de Ocio Familiar (Juegos y Videojuegos), debido a que tiene muchos servicios, este programa no va a abarcar todo lo que tiene el Centro.

Tampoco crearé una versión exacta de como realizan los procedimientos en el salón de juegos, pero será de inspiración para este trabajo .

## Tecnologías
- Python -> Código fuente
- Markdown -> Documentar información
- Git -> Control de versiones
- Github -> Guardar toda la información

# *Autor:*

- *Jhon Jairo Linares B.*
- *Ingeniería de Sistemas y Telecomunicaciones.*
- *Universidad de Manizales.*
- **2026**

# Funcionalidades del sistema

### 1. Usuarios:

*   **Registro y Acceso**: Los jugadores pueden registrarse con un nombre y un PIN. También hay usuarios especiales (operadores) para la gestión.
*   **Acumulación**: Los usuarios acumulan tickets (puntos) y fichas para jugar.

### 2. Máquinas de Juego:

*   **Variedad**: Hay máquinas que dan tickets (puntos) al jugar, como la máquina de payasos, y otras que son solo para diversión (no dan tickets).
*   **Flexibilidad**: Es fácil añadir nuevos tipos de juegos con sus propias reglas.

### 3. Premios:

*   **Canje de Puntos**: Los tickets acumulados se pueden usar para canjear premios de un catálogo.
*   **Control**: El sistema verifica si tienes suficientes tickets y si el premio está disponible antes de entregarlo.

### 4. Gestión de Monedas (representadas como Fichas):

*   **Monedas de 1€**: En el mundo real, los usuarios insertan monedas de 1€ para jugar. En el sistema, estas monedas se representan internamente como "fichas" digitales.
*   **Uso Digital**: Los usuarios comunes poseen un saldo de estas "fichas" digitales que pueden usar para activar las máquinas de juego.
*   **Máquina de Cambio**: Hay una máquina virtual que simula la conversión de dinero real (monedas de 1€) en estas fichas digitales, facilitando la interacción del usuario con el sistema.
