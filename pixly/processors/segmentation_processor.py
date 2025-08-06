"""
pixly/processors/segmentation_processor.py
Procesador de segmentación de imágenes en escala de grises.
Implementa métodos básicos como umbral fijo, Otsu y adaptativo.
"""

"""
pixly/processors/segmentation_processor.py
Procesador de segmentación de imágenes en escala de grises.
"""

import cv2
import numpy as np


class SegmentationProcessor:
    """Aplica técnicas básicas de segmentación a imágenes en escala de grises."""

    def __init__(self, method: str = 'otsu', thresh: int = 128):
        """
        Inicializa el procesador de segmentación.
        
        :param method: 'threshold', 'otsu', 'adaptive'
        :param thresh: Umbral fijo para el método 'threshold'
        """
        self.method = method
        self.thresh = thresh

    def process(self, image: np.ndarray) -> np.ndarray:
        """Aplica el método de segmentación seleccionado."""
        if self.method == 'threshold':
            return self.threshold(image, self.thresh)
        elif self.method == 'otsu':
            return self.otsu(image)
        elif self.method == 'adaptive':
            return self.adaptive(image)
        else:
            raise ValueError(f"Segmentation method '{self.method}' not supported.")

    __call__ = process  # Alias opcional para usarlo como función

    def threshold(self, image: np.ndarray, thresh: int = 128) -> np.ndarray:
        """Segmentación binaria por umbral fijo."""
        _, binary = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
        return binary
    
    def otsu(self, image: np.ndarray) -> np.ndarray:
        """Segmentación automática usando el método de Otsu."""
        _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary
    
    def adaptive(self, image: np.ndarray) -> np.ndarray:
        """Segmentación adaptativa por bloques locales."""
        binary = cv2.adaptiveThreshold(
            image, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY,
            blockSize=11,
            C=2  
        )
        return binary
