import nibabel as nib
import numpy as np
def process_segment(input_image):
    segmentation = nib.load(f"{input_image}")
    segmentation_data = segmentation.get_fdata()
    return segmentation_data if np.sum(segmentation_data) != 0 else Exception("Image is null / Segment not found on the image")