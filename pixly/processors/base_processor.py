"""
Base class for all Pixly processors.
Follows the Liskov Substitution Principle (LSP) and Open/Closed Principle (OCP).
"""

from abc import ABC, abstractclassmethod
import numpy as np

class BaseProcessor(ABC):
    """
    Abstract base class for all image processors.
    """

    @abstractclassmethod
    def process(self, image: np.ndarray) -> np.ndarray:
        """
        Applies the processor's transformation to an image.

        :param image: Input image as a Numpy array
        :return: Processed image as a Numpy array.
        """

        pass
    