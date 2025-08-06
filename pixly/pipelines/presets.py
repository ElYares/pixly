from pixly.processors.morphological_processor import MorphologicalProcessor
from pixly.processors.segmentation_processor import SegmentationProcessor
from pixly.processors.mlo_segmentation_processor import MLOSegmentationProcessor

def get_preset_pipeline(name: str):
    """
    Returns a list of processors for the given preset name.
    """
    if name == "clean_mlo":
        # Limpieza completa para MLO
        return [MLOSegmentationProcessor()]
    
    elif name == "classic_segment":
        # Segmentación Otsu básica
        return [SegmentationProcessor(method='otsu')]
    
    elif name == "morph_then_segment":
        # Morfología seguida de segmentación Otsu
        return [
            MorphologicalProcessor(operation='open', kernel_size=5, iterations=1),
            SegmentationProcessor(method='otsu')
        ]
    
    else:
        raise ValueError(f"Preset '{name}' is not defined.")
