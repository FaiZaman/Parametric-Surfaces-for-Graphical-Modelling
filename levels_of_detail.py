from geomdl import NURBS
from geomdl import utilities
from geomdl import exchange
from geomdl.visualization import VisVTK

# set level_of_detail
# ======= CHANGE THIS VARIABLE TO ONE OF ['low', 'medium', 'high'] TO CHANGE THE LEVEL OF DETAIL =======
level_of_detail = 'high'
removal = 2

# set face control points
face = NURBS.Surface()

# set face degrees
face.degree_u = 3
face.degree_v = 3

# import right face control points from file
right_ctrl_pts = exchange.import_txt("data/face.cpt", separator=",")
mirrored_ctrl_pts = []
left_ctrl_pts = []

# generate left face control points by mirroring right face control points
for ctrl_pt in right_ctrl_pts:
    x = ctrl_pt[0]
    mirrored_x = x * -1
    mirrored_ctrl_pt = [mirrored_x] + ctrl_pt[1:3]
    mirrored_ctrl_pts.append(mirrored_ctrl_pt)

for i in range(len(mirrored_ctrl_pts), 0, -15):

    ctrl_pts_line = mirrored_ctrl_pts[i-15:i]
    for ctrl_pt in ctrl_pts_line:
        left_ctrl_pts.append(ctrl_pt)

# combine left and right face control points
ctrl_pts = left_ctrl_pts + right_ctrl_pts
levels = [ctrl_pts[i:i+15] for i in range(0, len(ctrl_pts), 15)]

# low LoD
if level_of_detail == 'low':

    del levels[removal - 1 :: removal]
    del levels[removal - 1 :: removal]

    low_ctrl_pts = [item for sublist in levels for item in sublist]

    # set face control points and their sizes
    face.ctrlpts_size_u = 6
    face.ctrlpts_size_v = 15
    face.ctrlpts = low_ctrl_pts

    # generate face knot vectors
    face.knotvector_u = utilities.generate_knot_vector(face.degree_u, 6)
    face.knotvector_v = utilities.generate_knot_vector(face.degree_v, 15)

    # render face with colourmap
    face.vis = VisVTK.VisSurface()
    face.render(cpcolor='wheat')

# medium LoD
elif level_of_detail == 'medium':

    del levels[removal - 1 :: removal]
    medium_ctrl_pts = [item for sublist in levels for item in sublist]

    # set face control points and their sizes
    face.ctrlpts_size_u = 12
    face.ctrlpts_size_v = 15
    face.ctrlpts = medium_ctrl_pts

    # generate face knot vectors
    face.knotvector_u = utilities.generate_knot_vector(face.degree_u, 12)
    face.knotvector_v = utilities.generate_knot_vector(face.degree_v, 15)

    # render face with colourmap
    face.vis = VisVTK.VisSurface()
    face.render(cpcolor='wheat')

# high (original) LoD
elif level_of_detail == 'high':

    # set face control points and their sizes
    face.ctrlpts_size_u = 24
    face.ctrlpts_size_v = 15
    face.ctrlpts = ctrl_pts

    # generate face knot vectors
    face.knotvector_u = utilities.generate_knot_vector(face.degree_u, 24)
    face.knotvector_v = utilities.generate_knot_vector(face.degree_v, 15)

    # render face with colourmap
    face.vis = VisVTK.VisSurface()
    face.render(cpcolor='wheat')
