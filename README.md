# CONTROL-CENTER

Este proyecto es una terminal interactiva construida en Python que simula un sistema operativo ficticio.
La idea principal es crear un entorno estilo centro de control donde pueda interactuar mediante comandos, visualizar información del sistema y añadir módulos progresivamente.
No pretende ser una aplicación empresarial tradicional ni una API CRUD, sino un laboratorio técnico personal para aprender programación, arquitectura y diseño de software de forma práctica y motivadora.


 ## Objetivo del proyecto

El objetivo de este proyecto es aprender a construir software de manera progresiva, entendiendo cada decisión técnica y evitando limitarme a copiar soluciones.

Con este proyecto quiero practicar:
- pensamiento técnico
- arquitectura de programación
- separación de responsabilidades
- diseño modular
- debugging
- evolución progresiva de un proyecto real


## Filosofía

Este proyecto se desarrollará poco a poco, empezando por una versión simple y ampliándola con nuevas funcionalidades cuando la base esté clara.
La prioridad no es terminar rápido, sino entender cómo se organiza un proyecto, cómo se dividen las responsabilidades y cómo se construye sistemas que puedan verse difíciles de mantener.
La idea es evitar la sobreingeniería al principio, pero construir desde el inicio con una mentalidad ordenada y preparada para evolucionar.

## Fase actual

La primera fase consiste en crear una terminal CLI mínima que permita al usuario escribir y recibir respuestas del sistema.

En esta fase se trabajará sobre:

- un punto de entrada para inicializar la aplicación
- un bucle principal de ejecución
- lectura de comandos desde la terminal
- comandos básicos del sistema
- un estado compartido inicial
- una estructura separada por responsabilidades

## Estructura prevista
nexus-control-center/
├─ main.py
├─ control_center/
│  ├─ __init__.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ app.py
│  │  ├─ command_registry.py
│  │  └─ context.py
│  └─ commands/
│     ├─ __init__.py
│     ├─ help.py
│     ├─ status.py
│     └─ system.py
└─ README.md

## RESPONSABILIDADES INICIALES

- main.py: será el punto de entrada del proyecto. Su responsabilidad será iniciar la aplicación y delegar el funcionamiento principal en el núcleo del sistema.

- core/: contendrá las piezas centrales de la aplicación, como el bucle principal, el contexto compartido y el registro de comandos.

- commands/: contendrá los comandos disponibles en la terminal. Cada comando tendrá una responsabilidad concreta y podrá evolucionar de forma independiente.

README.md servirá como documentación viva del proyecto, explicando su propósito, evolución y decisiones técnicas importantes.

## Comandos iniciales previstos

- help: mostrará los comandos disponibles.
- status: mostrará el estado general del sistema.
- clear: limpiará visualmente la terminal.
- exit: cerrará la aplicación de forma controlada.

## Cómo ejecutar

python main.py

## Roadmap

Ideas futuras para evolucionar el proyecto:

- añadir nuevos comandos interactivos
- crear un sistema de módulos
- mostrar logs simulados del sistema
- añadir monitorización básica del equipo
- crear paneles visuales en consola
- mejorar la estética de la terminal
- añadir comandos con argumentos
- integrar simulaciones internas
- explorar una interfaz gráfica estilo terminal
- integrar IA en algún módulo del sistema

## NOTAS IMPORTANTES

En esta sección se irán anotando decisiones técnicas, errores encontrados, conceptos aprendidos y cambios importantes en la arquitectura del proyecto.

Algunas preguntas que pueden guiar esta parte:

¿Por qué separar el núcleo de los comandos?
¿Qué problema resuelve un registro de comandos?
¿Qué información debería vivir en el contexto del sistema?
¿Cuándo merece la pena crear una nueva abstracción?
¿Cómo puedo añadir funcionalidades sin romper lo existente?