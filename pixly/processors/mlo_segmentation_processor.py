import cv2
import numpy as np

class MLOSegmentationProcessor:
    """Segmenta automáticamente la región mamaria en proyecciones MLO."""

    def __init__(self, blur_ksize=5):
        self.blur_ksize = blur_ksize

    def process(self, image: np.ndarray) -> np.ndarray:
        # 1 procesamiento
        img_blur = cv2.GaussianBlur(image, (self.blur_ksize, self.blur_ksize), 0)


        # Umbralizacion
        _, binary = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Operaciones morfologicas
        kernel = np.ones((7,7), np.uint8)
        clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)

        # Conservar solo el contorno mas grande
        contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return np.zeros_like(image)
        
        largest_contour = max(contours, key=cv2.contourArea)
        mask = np.zeros_like(image)
        cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

        segmented = cv2.bitwise_and(image, image, mask=mask)

        return segmented
