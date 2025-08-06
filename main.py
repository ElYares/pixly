#!/usr/bin/env python3
"""
main.py
Pixly CLI: Read and process mammography images with morphological operations.
"""

import os
import argparse
import cv2
from pixly.reader import ImageReader
from pixly.pipeline import ImagePipeline
from pixly.processors.morphological_processor import MorphologicalProcessor
from pixly.processors.segmentation_processor import SegmentationProcessor
from pixly.utils.visualization import overlay_contours

def main():
    parser = argparse.ArgumentParser(description="Pixly: Image Processing CLI")
    parser.add_argument("image_path", type=str, help="Path to the .pgm image")
    
    # Morphological args
    parser.add_argument("--morph", type=str, choices=['erode', 'dilate', 'open', 'close'],
                        help="Apply a morphological operation")
    parser.add_argument("--kernel", type=int, default=3, help="Kernel size (default=3)")
    parser.add_argument("--iterations", type=int, default=1, help="Morph iterations (default=1)")
    
    # Segmentation args
    parser.add_argument("--segment", type=str, choices=['threshold', 'otsu', 'adaptive'],
                        help="Apply a segmentation method")
    parser.add_argument("--thresh", type=int, default=128, help="Threshold value (for 'threshold' method)")
    
    parser.add_argument("--show", action="store_true", help="Display processed image")
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: the path '{args.image_path}' does not exist.")
        return

    # Read image
    reader = ImageReader()
    image = reader.read(args.image_path)
    print(f"[Pixly] Image loaded: {image.shape}")

    # Build processing pipeline
    processors = []
    
    if args.morph:
        processors.append(MorphologicalProcessor(args.morph, args.kernel, args.iterations))
    
    if args.segment:
        processors.append(SegmentationProcessor(args.segment, args.thresh))

    if processors:
        pipeline = ImagePipeline(processors)
        processed_image = pipeline.run(image)
        print("[Pixly] Processing complete.")

        if args.segment:
            final_image = overlay_contours(image, processed_image, color=(0, 255, 0))
        else:
            final_image = processed_image

         # Guardar salida
        output_path = f"processed_{args.morph or ''}_{args.segment or ''}.png".strip('_')
        cv2.imwrite(output_path, final_image)
        print(f"[Pixly] Output saved to {output_path}")

        if args.show:
            cv2.imshow("Processed Image", final_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("[Pixly] No processing selected.")


if __name__ == "__main__":
    main()
