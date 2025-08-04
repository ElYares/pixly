"""
pixly/reader.py
Módulo responsable de la lectura de imágenes (.pgm inicialmente).
Cumple con SRP del principio SOLID.
"""

import cv2
import numpy as np


class ImageReader:
    """Clase para lectura de imágenes médicas en diferentes formatos."""

    def read(self, image_path: str) -> np.ndarray:
        """
        Lee una imagen desde la ruta especificada.
        Actualmente soporta .pgm usando OpenCV.

        :param image_path: Ruta del archivo de imagen.
        :return: Imagen como arreglo NumPy o None si falla la lectura.
        """
        try:
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            return image
        except Exception as e:
            print(f"Error al leer la imagen: {e}")
            return None
