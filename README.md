# Pixly

Pixly es un paquete de **procesamiento de imágenes biomédicas** diseñado para trabajar con **mastografías** y otras imágenes en formato **PGM**.  
El proyecto sigue **principios SOLID**, implementa un **pipeline modular**, y permite aplicar **operaciones morfológicas** para preparar imágenes para análisis y segmentación.

---

## Características

- Lectura de imágenes `.pgm` en escala de grises mediante OpenCV.
- Visualización de dimensiones de la imagen cargada.
- **Procesamiento morfológico básico**:
  - **Erosión (`erode`)** → Reduce puntos brillantes/ruido.
  - **Dilatación (`dilate`)** → Expande regiones brillantes.
  - **Apertura (`open`)** → Erosión seguida de dilatación (elimina ruido).
  - **Cierre (`close`)** → Dilatación seguida de erosión (cierra huecos).
- **Pipeline modular** para encadenar múltiples pasos de procesamiento.
- **CLI avanzada** con `argparse` para ejecutar comandos desde la terminal.

---

## Estructura del proyecto

<pre>
├── main.py
├── pixly
│   ├── pipeline.py
│   ├── processors
│   │   ├── base_processor.py
│   │   ├── morphological_processor.py
│   │   └── __pycache__
│   │       ├── base_processor.cpython-313.pyc
│   │       └── morphological_processor.cpython-313.pyc
│   ├── __pycache__
│   │   ├── pipeline.cpython-313.pyc
│   │   └── reader.cpython-313.pyc
│   └── reader.py
├── README.md
└── setup.py
</pre>

## Dependencias y el paquete en modo dev

```
pip install -e .
```

## Dependencias principales
- Opencv-python
- numpy

# Uso

### Lectura de una imagen
```
python3 main.py archive/<nombre_image>.pgm
```

### Aplicar operaciones morfologicas
```
python3 main.py archive/<nombre_image>.py --morph erode --iterations 2 --show
```

- --morph -> Tipo de operacion morfologica
- --iterations 2 -> Repite la operacion dos veces.
- --show -> Muestra la imagen procesada en una ventana de OpenCv.
- --kernel 5 -> Usa un kernel de 5x5 para la operacion ideal para eliminar ruido y suavizar bordes.



