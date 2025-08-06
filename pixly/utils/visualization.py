import cv2
import numpy as np

def overlay_contours(original: np.ndarray, binary: np.ndarray, color=(0, 255, 0), thickness=2) -> np.ndarray:
    """
    Dibuja los contornos de la imagen binaria sobre la imagen original.
    
    :param original: Imagen original en escala de grises o BGR.
    :param binary: Imagen segmentada (binaria).
    :param color: Color de los contornos (BGR).
    :param thickness: Grosor de la línea de contorno.
    :return: Imagen con contornos dibujados.
    """

    if len(original.shape) == 2:
        overlay = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)
    else:
        overlay = original.copy()
    

    # Encontrar contornos en la imagen binaria
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar contornos
    cv2.drawContours(overlay, contours, -1, color, thickness)
    return overlay