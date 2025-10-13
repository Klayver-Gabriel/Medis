from totalsegmentator.python_api import totalsegmentator
import nibabel as nib
import vedo
import numpy as np


def segmentate(image:str,output_name:str):
    totalsegmentator(image,output_name)

def process_segment(input_image):
    segmentation = nib.load(f"Results/{input_image}")
    segmentation_data = segmentation.get_fdata()
    return segmentation_data if np.sum(segmentation_data) != 0 else Exception("Image is null / Segment not found on the image")

def show_segments(input_image):
    volume = vedo.Volume(input_image)
    mesh = volume.isosurface(value=0.5).c('red')
    vedo.show(mesh, __doc__, axes=1)