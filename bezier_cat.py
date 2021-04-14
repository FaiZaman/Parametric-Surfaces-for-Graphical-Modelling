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
    [5.0, 10.0],
    [35.0, 10.0],
    [32.0, 26.0]
]

# Generate a uniform knot vector
crv1.knotvector = knotvector.generate(crv1.degree, crv1.ctrlpts_size)

# Create the curve instance #2
crv2 = BSpline.Curve()

# Set degree
crv2.degree = 3

# Set control points
crv2.ctrlpts = [
    [20.0, 4.0],
    [36.0, 5.0],
    [40.0, 17.0],
    [32.0, 26.0]
]

# Generate a uniform knot vector
crv2.knotvector = knotvector.generate(crv2.degree, crv2.ctrlpts_size)

# Create the curve instance #3
crv3 = BSpline.Curve()

# Set degree
crv3.degree = 3

# Set control points
crv3.ctrlpts = [
    [34.0, 24.0],
    [36.0, 34.0],
    [26.0, 28.0],
    [26.0, 28.0]
]

# Generate a uniform knot vector
crv3.knotvector = knotvector.generate(crv3.degree, crv3.ctrlpts_size)

# Create the curve instance #2
crv4 = BSpline.Curve()

# Set degree
crv4.degree = 3

# Set control points
crv4.ctrlpts = [
    [26.0, 28.0],
    [21.0, 30.0],
    [16.0, 27.0],
    [16.0, 27.0]
]

# Generate a uniform knot vector
crv4.knotvector = knotvector.generate(crv4.degree, crv4.ctrlpts_size)

# Create the curve instance #2
crv5 = BSpline.Curve()

# Set degree
crv5.degree = 3

# Set control points
crv5.ctrlpts = [
    [16.0, 27.0],
    [7.0, 31.0],
    [10.0, 20.0],
    [10.0, 20.0]
]

# Generate a uniform knot vector
crv5.knotvector = knotvector.generate(crv5.degree, crv5.ctrlpts_size)

# Create a curve container
mcrv = multi.CurveContainer(crv1, crv2)# crv3, crv4, crv5)

# Set the visualization component of the curve container
mcrv.vis = VisMPL.VisCurve2D()

# Plot the curves in the curve container
mcrv.render()
