from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Create a B-Spline curve
curve = BSpline.Curve()

# Set up the curve
curve.degree = 4
curve.ctrlpts = [
    [10.0, 20.0],
    [7.0, 12.0],
    [15.0, 0.0],
    [36.0, 5.0],
    [40.0, 17.0],
    [32.0, 26.0],
    [33.0, 22.0],
    [36.0, 34.0],
    [26.0, 28.0],
    [26.0, 28.0],
    [21.0, 30.0],
    [16.0, 27.0],
    [16.0, 27.0],
    [7.0, 31.0],
    [10.0, 20.0]
]

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Plot the control point polygon and the evaluated curve
curve.vis = VisMPL.VisCurve2D()
curve.render()
