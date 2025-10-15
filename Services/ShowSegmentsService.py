import vedo
import nibabel as nib
import numpy as np

def show_segments(input_image):

    volume = vedo.Volume(input_image)
    mesh = volume.isosurface(value=0.5).c('red')
    vedo.show(mesh, __doc__, axes=4)


def show_multiple_segments(ml_path,segment_map):
    img_ml = nib.load(ml_path)
    data_ml = img_ml.get_fdata()
    segment_id = []
    actors = []
    volume = vedo.Volume(data_ml)
    data = volume.tonumpy()

    unique_labels = np.unique(data)

    for label in unique_labels:
        if label > 0:
            segment_id.append(label)

    for segment in segment_id:

        if segment not in segment_map:
            continue
        actors.append(customize_mesh(segment,segment_map, volume))

    vedo.show(actors,title="TotalSegmentator Multilabel Visualization",axes=2,bg='black',size=(1000, 800))

def customize_mesh(segment,segment_map,volume):

    segment_alpha, segment_color = segment_map[segment]
    mesh = volume.isosurface(value=segment)
    mesh.c(segment_color)
    mesh.alpha(segment_alpha)
    mesh.lighting('plastic')
    return mesh