import nibabel as nib
import numpy as np
import vedo
import pandas as pd
def process_segment_data(input_image):
    try:
        segmentation = nib.load(f"{input_image}")
        segmentation_data = segmentation.get_fdata()
        return segmentation_data
    except Exception as e:
        print(e)

def process_segment_index(ml_path):
    img_ml = nib.load(ml_path)
    data_ml = img_ml.get_fdata()
    volume = vedo.Volume(data_ml)
    data = volume.tonumpy()

    unique_labels = np.unique(data)
    segment_id = [label for label in unique_labels if label > 0]
    return segment_id