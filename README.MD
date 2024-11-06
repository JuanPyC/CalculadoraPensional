  # CalculadoraPensional

## ¿Quién hizo esto?
Este proyecto fue desarrollado y modificado por los estudiantes de Código Limpio: Juan Diego Gomez y Santiago Cano

## ¿Qué es y para qué es?
'CalculadoraPensional' es una herramienta diseñada para calcular pensiones con base en diferentes criterios definidos en su lógica interna. El propósito de este proyecto es facilitar el cálculo de pensiones de acuerdo con las normativas y reglas especificadas, permitiendo realizar simulaciones y proyecciones para los usuarios finales.

## ¿Cómo lo hago funcionar?
Prerrequisitos
- Python 3.8 o superior: Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org.

- Instalar dependencias: Si hay dependencias adicionales necesarias, puedes instalarlas utilizando un archivo requirements.txt (si existe) o ejecutando:
```
pip install -r requirements.txt
```
- También necesitas tener instalado psycopg2 

 ## Ejecución desde la terminal

### ¿Cómo ejecutar el programa?
1. Presiona la tecla `Windows` y busca en la barra "Command Prompt" o "cmd".
2. Ubicate en la carpeta donde clonaste el repositorio 
3. Para ejecutar el programa desde la consola, utiliza el siguiente comando:

    ```bash
    py src/View/console.py
    ```

4. Presiona `Enter` para iniciar el programa.
5. Para ejecutar la interfaz gráfica GUI, utiliza el siguiente comando:                          `py src/GUI/CalculatorGUI.py`
6. Asegurate de tener instalado Kivy para ejecutar la interfaz gráfica, puedes instalarlo con el siguiente comando: `pip install kivy[base]`

### Ejecutar las pruebas unitarias:
1. Para ejecutar las pruebas unitarias, navega a la carpeta raíz del proyecto.
2. Escribe el siguiente comando y presiona `Enter`:

    ```bash
    py Test/CalculatorTest.py
    ```

## ¿Cómo ejecutar las bases de datos?
1. Para ejecutar las bases de datos, navega a la carpeta raíz del proyecto 
2. Escribe el siguiente comando y presiona `Enter`
3. 


## ¿Cómo está hecho?
- ## Arquitectura del proyecto
El proyecto sigue una arquitectura modular, con la lógica de negocio separada de la interfaz de usuario de consola. Se utiliza Python como lenguaje de programación y se organizan las diferentes capas de la aplicación en subcarpetas dentro de src.

- ## Bibliotecas y dependencias
Actualmente, el proyecto no especifica ninguna dependencia externa, por lo que sólo requiere Python y sus bibliotecas estándar. Si se agregan dependencias futuras, estas se documentarán en un archivo requirements.txt.

## Organización de los módulos
- Carpeta src: Contiene el código fuente de la aplicación.
- View: Incluye la lógica de la interfaz de consola, donde el usuario puede interactuar con la calculadora pensional.
- GUI: Incluye la lógica de la interfaz gráfica 
- Model: Contiene las clases y funciones que implementan la lógica de los cálculos de pensión.
- Test: Contiene las pruebas unitarias para validar el comportamiento del sistema.
- Controller: Se encarga de conectarse a la base de datos y realizar 4 funcionalidad conocidas como CRUD 

## Como configurar el SecretConfig.py


Datos secretos que no deben publicarse en el repositorio

Diligencie estos datos y guarde este archivo como SecretConfig.py en el modulo src
para poder ejecutar la aplicación



PGDATABASE = "ESCRIBA EL NOMBRE DE LA BASE DE DATOS"
PGUSER = "ESCRIBA EL USUARIO DE LA DB"
PGPASSWORD = "ESCRIBA LA CONSTRASEÑA"
PGHOST = "ESCRIBA LA DIRECCION DNS O DIRECCION IP DEL SERVIDOR"
PGPORT = 5432 # POR DEFECTO ES 5432, PERO PUEDE CAMBIAR EN SU DB

## Como ejecutar
1. Clonar el repositorio de la ultima practica de codigo limpio:
```mardown
git clone https://github.com/JuanPyC/CalculadoraPensional CalculadoraPensional
```

2. Ejecutar el comando para instalar la libreria flask
  ```markdown
  pip install flask
  ``` 
3. Ejecutar el modulo app.py
```mardown 
py app.py
```
## ¿Quién hizo esto?
Este proyecto fue desarrollado y modificado por los estudiantes de Código Limpio: Juan Diego Gomez y Santiago Cano