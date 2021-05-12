from matplotlib import cm

from geomdl import NURBS
from geomdl import multi
from geomdl import utilities
from geomdl import exchange
from geomdl.visualization import VisVTK

# set face control points
face = NURBS.Surface()

face.degree_u = 3
face.degree_v = 3

ctrl_pts = exchange.import_txt("data/face.cpt", separator=",")

face.ctrlpts_size_u = 12
face.ctrlpts_size_v = 15
face.ctrlpts = ctrl_pts

face.knotvector_u = utilities.generate_knot_vector(face.degree_u, 12)
face.knotvector_v = utilities.generate_knot_vector(face.degree_v, 15)

# render with colourmap
face.vis = VisVTK.VisSurface(ctrlpts=False, axes=False)
face.render(cpcolor='wheat')

# .samplesize - levels of detail
