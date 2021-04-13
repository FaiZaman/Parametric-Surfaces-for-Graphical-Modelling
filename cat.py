from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL

# Create a B-Spline curve
curve = BSpline.Curve()

# Set up the curve
curve.degree = 4
curve.ctrlpts = [
    [5.0, 10.0], 
    [15.0, 25.0], 
    [30.0, 30.0], 
    [45.0, 5.0], 
    [55.0, 5.0],
    [70.0, 40.0], 
    [60.0, 60.0], 
    [35.0, 60.0], 
    [20.0, 40.0]
]

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Plot the control point polygon and the evaluated curve
curve.vis = VisMPL.VisCurve2D()
curve.render()
