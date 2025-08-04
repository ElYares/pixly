#!/usr/bin/env python3
"""
main.py
Pixly CLI: Read and process mammography images with morphological operations.
"""

import os
import argparse
from pixly.reader import ImageReader
from pixly.pipeline import ImagePipeline
from pixly.processors.morphological_processor import MorphologicalProcessor
import cv2


def main():
    parser = argparse.ArgumentParser(description="Pixly: Morphological Image Processing CLI")
    parser.add_argument("image_path", type=str, help="Path to the .pgm image")
    parser.add_argument("--morph", type=str, choices=['erode', 'dilate', 'open', 'close'],
                        help="Apply a morphological operation")
    parser.add_argument("--kernel", type=int, default=3, help="Kernel size for morphological operation (default=3)")
    parser.add_argument("--iterations", type=int, default=1, help="Number of iterations (default=1)")
    parser.add_argument("--show", action="store_true", help="Display processed image")
    args = parser.parse_args()

    # Validate path
    if not os.path.exists(args.image_path):
        print(f"Error: the path '{args.image_path}' does not exist.")
        return

    # Read image
    reader = ImageReader()
    image = reader.read(args.image_path)
    print(f"[Pixly] Image loaded: {image.shape}")

    # Build pipeline
    processors = []
    if args.morph:
        processors.append(MorphologicalProcessor(args.morph, args.kernel, args.iterations))

    if processors:
        pipeline = ImagePipeline(processors)
        processed_image = pipeline.run(image)
        print("[Pixly] Processing complete.")

        if args.show:
            cv2.imshow("Processed Image", processed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("[Pixly] No processing selected.")


if __name__ == "__main__":
    main()
