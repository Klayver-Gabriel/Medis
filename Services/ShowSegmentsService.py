import vedo
import nibabel as nib
import numpy as np

from Services import SegmentService, ProcessSegmentService


def show_segments(input_image):

    volume = vedo.Volume(input_image)
    mesh = volume.isosurface(value=0.5).c('red')
    vedo.show(mesh, __doc__, axes=4)


def show_multiple_segments(ml_path,style):
    img_ml = nib.load(ml_path)
    data_ml = img_ml.get_fdata()
    actors = []
    volume = vedo.Volume(data_ml)

    segment_id = ProcessSegmentService.process_segment_index(ml_path)
    segments_properties = SegmentService.segment_map(segment_id)

    for segment in segment_id:
        actors.append(customize_mesh(segment,segments_properties, volume,style))

    vedo.show(actors,title="Complete body part image",axes=4,bg='black',size=(1000, 800))

def customize_mesh(segment,segment_map,volume,style):
    properties = segment_map[segment]
    segment_color = properties['color']
    segment_alpha = properties['alpha']
    mesh = volume.isosurface(value=segment)
    mesh.c(segment_color)
    mesh.alpha(float(segment_alpha))
    mesh.lighting(style)
    return mesh