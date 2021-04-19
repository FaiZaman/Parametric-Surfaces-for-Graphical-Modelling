from matplotlib import cm

from geomdl import NURBS
from geomdl import exchange
from geomdl.visualization import VisMPL

# import the control point data
surface = exchange.import_json("data/head.json")

# set surface parameters and generate
surface[0].sample_size = 100
surface[0].delta = 0.05
surface[0].vis = VisMPL.VisSurface()
surface[0].render(colormap=cm.copper)
