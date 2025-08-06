import os
import cv2
from pixly.reader import ImageReader
from pixly.utils.visualization import overlay_contours
from pixly.pipelines.builder import build_pipeline

def run(args):
    if not os.path.exists(args.image_path):
        print(f"Error: the path '{args.image_path}' does not exist.")
        return

    reader = ImageReader()
    image = reader.read(args.image_path)
    print(f"[Pixly] Image loaded: {image.shape}")

    pipeline = build_pipeline(args)
    if not pipeline:
        print("[Pixly] No processing selected.")
        return

    processed_image = pipeline.run(image)
    print("[Pixly] Processing complete.")

    # Overlay contours if segmentation or preset implies segmentation
    if args.segment or args.segment_mlo or args.preset in ['clean_mlo', 'classic_segment', 'morph_then_segment']:
        final_image = overlay_contours(image, processed_image, color=(0, 255, 0))
    else:
        final_image = processed_image

    # Output file name
    name_tag = args.preset or args.morph or args.segment or "output"
    output_file = f"processed_{name_tag}.png"
    cv2.imwrite(output_file, final_image)
    print(f"[Pixly] Output saved to {output_file}")

    if args.show:
        cv2.imshow("Processed Image", final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
