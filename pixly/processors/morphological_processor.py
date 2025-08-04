"""
Morphological image processor for Pixly.
Supports operations: 'erode', 'dilate', 'open', 'close'.
Follows Single Responsibility Principle: only morphological operations.
"""

import cv2
import numpy as np
from .base_processor import BaseProcessor

class MorphologicalProcessor(BaseProcessor):

    """Processor for morphological operations on images."""

    def __init__(self, operation: str, kernel_size: int = 3, iterations: int = 1):
        """
        Initialize the morphological processor.

        :param operation: Type of operation: 'erode', 'dilate', 'open', 'close'
        :param kernel_size: Size of the structuring element (odd number recommended)
        :param iterations: Number of times to apply the operation
        """

        self.operation = operation.lower()
        self.kernel_size = kernel_size
        self.iterations = iterations

        # Validate operation
        valid_ops = ['erode', 'dilate', 'open', 'close']
        if self.operation not in valid_ops:
            raise ValueError(f"Invalid operations '{operation}'. Must be one of {valid_ops}.")
    
    def process(self, image: np.ndarray) -> np.ndarray:
        """Apply the morphological operation to the input image"""

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (self.kernel_size, self.kernel_size))

        if self.operation == 'erode':
            return cv2.erode(image, kernel, iterations=self.iterations)
        elif self.operation == 'dilate':
            return cv2.dilate(image, kernel, iterations=self.iterations)
        elif self.operation == 'open':
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=self.iterations)
        elif self.operation == 'close':
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=self.iterations)