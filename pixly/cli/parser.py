import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Pixly: Image Processing CLI")
    parser.add_argument("image_path", type=str, help="Path to the .pgm image")

    # --- NEW: Preset pipelines ---
    parser.add_argument(
        "--preset",
        type=str,
        choices=['clean_mlo', 'classic_segment', 'morph_then_segment'],
        help="Run a predefined pipeline (overrides individual flags)"
    )
    
    # Morphological
    parser.add_argument("--morph", type=str, choices=['erode', 'dilate', 'open', 'close'],
                        help="Apply a morphological operation")
    parser.add_argument("--kernel", type=int, default=3, help="Kernel size (default=3)")
    parser.add_argument("--iterations", type=int, default=1, help="Morph iterations (default=1)")
    
    # Segmentation
    parser.add_argument("--segment", type=str, choices=['threshold', 'otsu', 'adaptive'],
                        help="Apply a segmentation method")
    parser.add_argument("--thresh", type=int, default=128, help="Threshold value for 'threshold'")
    
    # New: MLO pipeline
    parser.add_argument("--segment-mlo", action="store_true", help="Apply full MLO segmentation pipeline")

    # Visualization
    parser.add_argument("--show", action="store_true", help="Display processed image")
    
    return parser
