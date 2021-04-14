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
    [10.0, 0.0],
    [35.0, 2.5],
    [40.0, 15.0],
    [34.0, 24.0],
    [34.0, 24.0],
    [36.0, 36.0],
    [25.0, 28.0],
    [25.0, 28.0],
    [18.0, 30.0],
    [17.0, 24.0],
    [8.0, 32.0],
    [10.0, 20.0]
]

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Plot the control point polygon and the evaluated curve
curve.vis = VisMPL.VisCurve2D()
curve.render()
