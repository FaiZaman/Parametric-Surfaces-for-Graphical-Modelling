from matplotlib import cm

from geomdl import NURBS
from geomdl import BSpline
from geomdl import multi
from geomdl import utilities
from geomdl import exchange
from geomdl.visualization import VisMPL

# set face control points
left_face = NURBS.Surface()

left_face.degree_u = 2
left_face.degree_v = 2
left_face.delta = 0.05

ctrl_pts = exchange.import_txt("data/left_face.cpt", separator=",")

left_face.ctrlpts_size_u = 3
left_face.ctrlpts_size_v = 4
left_face.ctrlpts = ctrl_pts

left_face.knotvector_u = utilities.generate_knot_vector(left_face.degree_u, 3)
left_face.knotvector_v = utilities.generate_knot_vector(left_face.degree_v, 4)

# set face control points
right_face = NURBS.Surface()

right_face.degree_u = 2
right_face.degree_v = 2
right_face.delta = 0.05

ctrl_pts = exchange.import_txt("data/right_face.cpt", separator=",")

right_face.ctrlpts_size_u = 3
right_face.ctrlpts_size_v = 4
right_face.ctrlpts = ctrl_pts

right_face.knotvector_u = utilities.generate_knot_vector(right_face.degree_u, 3)
right_face.knotvector_v = utilities.generate_knot_vector(right_face.degree_v, 4)

# set face control points
left_eye = NURBS.Surface()

left_eye.degree_u = 1
left_eye.degree_v = 1
left_eye.delta = 0.05

ctrl_pts = exchange.import_txt("data/left_eye.cpt", separator=",")

left_eye.ctrlpts_size_u = 2
left_eye.ctrlpts_size_v = 3
left_eye.ctrlpts = ctrl_pts

left_eye.knotvector_u = utilities.generate_knot_vector(left_eye.degree_u, 2)
left_eye.knotvector_v = utilities.generate_knot_vector(left_eye.degree_v, 3)

# add to container
human_face = multi.SurfaceContainer(left_face, right_face, left_eye)

# render with colourmap
human_face.vis = VisMPL.VisSurface()
human_face.render(colormap=[cm.copper, cm.copper, cm.plasma])

# .samplesize - levels of detail
