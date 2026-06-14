# Trabajo Práctico Integrador - Programación I

## Gestión de Datos de Países en Python

### Integrantes

- Joel Cordero
- Marcos Peralta

---

## Descripción

Este proyecto es una aplicación de consola desarrollada en **Python 3** para gestionar información de países guardada en un archivo CSV.

El programa permite agregar y modificar países, buscar por nombre, filtrar por distintos criterios, ordenar los datos y obtener estadísticas. Lo hicimos aplicando lo que vimos en **Programación I**: listas, diccionarios, funciones, condicionales, ciclos y manejo de archivos.

Los cambios que se hacen en el programa (agregar o actualizar un país) se guardan automáticamente en el CSV.

---

## Requisitos

- Python 3.x

No usamos librerías externas, solo el módulo `csv` que viene con Python.

---

## Ejecución

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

En Windows también se puede usar:

```bash
py main.py
```

El programa carga los datos de `dataset-paises.csv` al iniciar.

---

## Archivos del proyecto

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Código principal del sistema |
| `dataset-paises.csv` | Datos de los países |
| `README.md` | Este archivo |

---

## Formato del CSV

El archivo `dataset-paises.csv` tiene las siguientes columnas:

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| nombre | texto | Argentina |
| poblacion | entero | 45376763 |
| superficie | entero | 2780400 |
| continente | texto | América |

Los continentes válidos al agregar un país son: **América**, **Europa**, **Asia**, **África** y **Oceanía**.

---

## Funcionalidades

### Menú principal

1. Agregar país
2. Actualizar país (población y superficie)
3. Buscar país por nombre (coincidencia parcial)
4. Filtros
5. Ordenamientos
6. Estadísticas

### Filtros

- Por continente
- Por rango de población (mínimo y máximo)
- Por rango de superficie (mínimo y máximo)

### Ordenamientos

- Por nombre (ascendente)
- Por población (ascendente)
- Por superficie (ascendente o descendente)

### Estadísticas

- País con mayor población
- País con menor población
- Promedio de población
- Promedio de superficie
- Cantidad de países por continente

---

## Ejemplo de uso

Al iniciar el programa aparece el menú principal. Para buscar un país:

```
=== GESTIÓN DE PAÍSES ===
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtros
5. Ordenamientos
6. Estadísticas
0. Salir
Opción: 3
Ingrese el nombre del país a buscar: Argentina
```

Salida:

```
------------------
Nombre: Argentina
Población: 50000000
Superficie: 3761000
Continente: América
```

La búsqueda no distingue mayúsculas/minúsculas y también funciona con partes del nombre (por ejemplo, "Arg" encuentra "Argentina").

---

## Participación de los integrantes

El trabajo lo hicimos entre los dos de forma colaborativa:

- **Joel Cordero:** diseño general del menú, funciones de carga/guardado del CSV, ABM (agregar y actualizar) y búsqueda.
- **Marcos Peralta:** filtros, ordenamientos con Selection Sort, estadísticas y pruebas del sistema.

Ambos participamos en la corrección de errores, la documentación y la preparación de la entrega.

---

## Video demostrativo

https://youtu.be/p1CvTRYOe5U

---

## Repositorio

https://github.com/joelC16/TPI-Programacion
