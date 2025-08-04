"""
Image processing pipeline for Pixly.
Follows Dependency Inversion Principle: depends on abstract processors, not implementations.
"""

from typing import List
import numpy as np
from pixly.processors.base_processor import BaseProcessor

class ImagePipeline:
    """Pipeline to apply multiple processors sequentially."""

    def __init__(self, processors: List[BaseProcessor]):
        """
        Initialize the pipeline with a list of processors.
        :param processors: List of processors that inherit from BaseProcessor
        """
        self.processors = processors

    def run(self, image: np.ndarray) -> np.ndarray:
        """
        Apply all processors sequentially to the image.
        :param image: Input image
        :return: Processed image
        """
        output = image.copy()
        for processor in self.processors:
            output = processor.process(output)
        return output