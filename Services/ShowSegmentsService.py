import vedo
def show_segments(input_image):
    volume = vedo.Volume(input_image)
    mesh = volume.isosurface(value=0.5).c('red')
    vedo.show(mesh, __doc__, axes=1)