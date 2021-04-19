from geomdl import NURBS
from geomdl import exchange
from geomdl.visualization import VisMPL

surface = exchange.import_json("data/head.json")

surface[0].sample_size = 100
surface[0].delta = 0.05
surface[0].vis = VisMPL.VisSurface()
surface[0].render()
