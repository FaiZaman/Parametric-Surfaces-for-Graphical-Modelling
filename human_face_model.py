from matplotlib import cm

from geomdl import NURBS
from geomdl import BSpline
from geomdl import multi
from geomdl import exchange
from geomdl.visualization import VisMPL

# import the control point data
head = exchange.import_json("data/head.json")

# set head parameters
head[0].sample_size = 100
head[0].delta = 0.05

# set eye control points
eye_ctrlpts = [
    [[6000, -2000, 1000], [6000, -1750, 1250], [6000, -1500, 1500]],
    [[6000, -1250, 1250], [6000, -1000, 1000], [6000, -1250, 750]],
    [[6000, -1500, 500], [6000, -1750, 750], [6000, -2000, 1000]]
]

eyes = BSpline.Surface()
eyes.degree_u = 2
eyes.degree_v = 2
eyes.ctrlpts2d = eye_ctrlpts

# number of knots in u = number of rows of control points + degree of u + 1
# number of knots in u = number of columns of control points + degree of v + 1
eyes.knotvector_u = [0, 0, 0, 1, 1, 2]
eyes.knotvector_v = [0, 0, 0, 1, 1, 2]

eyes.delta = 0.025
eyes.evaluate()

# add to container
human_face = multi.SurfaceContainer(head)

# render with colourmap
human_face.vis = VisMPL.VisSurface()
human_face.render(colormap=[cm.copper])

# .samplesize - levels of detail
