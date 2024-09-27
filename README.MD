  # CalculadoraPensional

## Quién hizo esto
Este proyecto fue desarrollado por el equipo de desarrollo Esteban parra, Edison ospina

## ¿Qué es y para qué es?
'CalculadoraPensional' es una herramienta diseñada para calcular pensiones con base en diferentes criterios definidos en su lógica interna. El propósito de este proyecto es facilitar el cálculo de pensiones de acuerdo con las normativas y reglas especificadas, permitiendo realizar simulaciones y proyecciones para los usuarios finales.

## ¿Cómo lo hago funcionar?
Prerrequisitos
- Python 3.8 o superior: Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org.

- Instalar dependencias: Si hay dependencias adicionales necesarias, puedes instalarlas utilizando un archivo requirements.txt (si existe) o ejecutando:
```
pip install -r requirements.txt
```
 ## Ejecución desde la terminal

### Abrir el programa:
1. Presiona la tecla `Windows` y busca en la barra "Command Prompt" o "cmd".
2. Escribe el siguiente comando para navegar a la carpeta del proyecto:

    ```bash
    cd CalculadoraPensional
    ```

3. Para ejecutar el programa desde la consola, utiliza el siguiente comando:

    ```bash
    python src/Console/CalculatorConsole.py
    ```

4. Presiona `Enter` para iniciar el programa.

### Ejecutar las pruebas unitarias:
1. Para ejecutar las pruebas unitarias, navega a la carpeta raíz del proyecto.
2. Escribe el siguiente comando y presiona `Enter`:

    ```bash
    python Test/CalculatorTest.py
    ```



## ¿Cómo está hecho?
- ## Arquitectura del proyecto
El proyecto sigue una arquitectura modular, con la lógica de negocio separada de la interfaz de usuario de consola. Se utiliza Python como lenguaje de programación y se organizan las diferentes capas de la aplicación en subcarpetas dentro de src.

- ## Bibliotecas y dependencias
Actualmente, el proyecto no especifica ninguna dependencia externa, por lo que sólo requiere Python y sus bibliotecas estándar. Si se agregan dependencias futuras, estas se documentarán en un archivo requirements.txt.

## Organización de los módulos
 - Carpeta src: Contiene el código fuente de la aplicación.
- consola: Incluye la lógica de la interfaz de consola, donde el usuario puede interactuar con la calculadora pensional.
- logica: Contiene las clases y funciones que implementan la lógica de los cálculos de pensión.
- Carpeta Test: Contiene las pruebas unitarias para validar el comportamiento del sistema.
