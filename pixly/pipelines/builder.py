from pixly.pipeline import ImagePipeline
from pixly.processors.morphological_processor import MorphologicalProcessor
from pixly.processors.segmentation_processor import SegmentationProcessor
from pixly.processors.mlo_segmentation_processor import MLOSegmentationProcessor
from pixly.pipelines.presets import get_preset_pipeline

def build_pipeline(args) -> ImagePipeline:
    processors = []

    if args.preset:  # <<--- priorizamos presets
        processors = get_preset_pipeline(args.preset)
    elif args.segment_mlo:
        processors.append(MLOSegmentationProcessor())
    else:
        if args.morph:
            processors.append(MorphologicalProcessor(args.morph, args.kernel, args.iterations))
        if args.segment:
            processors.append(SegmentationProcessor(args.segment, args.thresh))

    return ImagePipeline(processors) if processors else None
