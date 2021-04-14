from geomdl import BSpline
from geomdl import multi
from geomdl import knotvector
from geomdl.visualization import VisMPL

# Create the curve instance #1
crv1 = BSpline.Curve()

# Set degree
crv1.degree = 2

# Set control points
crv1.ctrlpts = [
    [10.0, 20.0],
    [7.0, 12.0],
    [15.0, 0.0],
    [36.0, 5.0]
]

# Generate a uniform knot vector
crv1.knotvector = knotvector.generate(crv1.degree, crv1.ctrlpts_size)

# Create the curve instance #2
crv2 = BSpline.Curve()

# Set degree
crv2.degree = 3

# Set control points
crv2.ctrlpts = [
    [36.0, 5.0],
    [40.0, 17.0],
    [34.0, 24.0],
    [34.0, 24.0],
]

# Generate a uniform knot vector
crv2.knotvector = knotvector.generate(crv2.degree, crv2.ctrlpts_size)

# Create a curve container
mcrv = multi.CurveContainer(crv1, crv2)

# Set the visualization component of the curve container
mcrv.vis = VisMPL.VisCurve2D()

# Plot the curves in the curve container
mcrv.render()
