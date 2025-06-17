import numpy as np

# Initial conditions (in AU and AU/days)
#
# The state vector 'q' is a single flat array structured to be compatible with the solver.
# It contains all position components first, followed by all velocity components.
# Format: [x1, y1, z1, x2, y2, z2, ..., vx1, vy1, vz1, vx2, vy2, vz2, ...]
#
# The solver will unpack this flat array like so:
# N = len(body_names)
# positions = q[:3*N].reshape((N, 3))
# velocities = q[3*N:].reshape((N, 3))

initial_conditions = np.array([
    # ===== POSITIONS (x, y, z) for all bodies in order =====
    # Sun
    -6.131042484363762e-03, -4.681968209220235e-03, 1.859335691083634e-04,
    # Mercury
    1.635741635892671e-01, -4.137841191213306e-01, -4.881212275819490e-02,
    # Venus
    5.537899705865670e-01, -4.685689836370686e-01, -3.849291117792204e-02,
    # Earth
    7.223097544906500e-01, 6.680194857062529e-01, 1.466819623598208e-04,
    # Moon
    7.219265966536434e-01, 6.654173307928256e-01, -8.422945939099281e-05,
    # Mars
    2.286611025992892e-01, 1.525285707539813e+00, 2.648815523597513e-02,
    # Jupiter
    1.471622873599419e+00, 4.838928321119571e+00, -5.299634686311931e-02,
    # Saturn
    9.409434508103104e+00, -2.080428754910253e+00, -3.384632291365005e-01,
    # Uranus
    1.128338007844716e+01, 1.597170058688966e+01, -8.685962746558047e-02,
    # Neptune
    2.987101143973271e+01, -8.190376478875210e-01, -6.715417063593708e-01,

    # ===== VELOCITIES (vx, vy, vz) for all bodies in order =====
    # Sun
    6.863234229776752e-06, -4.326634817474759e-06, -1.061839441128688e-07,
    # Mercury
    2.035932861794505e-02, 1.219058200410085e-02, -8.702931527377319e-04,
    # Venus
    1.278349854459380e-02, 1.549290947382977e-02, -5.244944393338642e-04,
    # Earth
    -1.195219879705250e-02, 1.257129916482715e-02, -6.195926402339273e-07,
    # Moon
    -1.137992595149114e-02, 1.251085455795946e-02, -1.120274327502465e-05,
    # Mars
    -1.329617775500723e-02, 3.307487489330665e-03, 3.955613163726505e-04,
    # Jupiter
    -7.304974728025273e-03, 2.554607745702978e-03, 1.528312286887247e-04,
    # Saturn
    8.942624373567732e-04, 5.436499164738797e-03, -1.304736713216418e-04,
    # Uranus
    -3.241349011221665e-03, 2.086076220497466e-03, 4.959294005296330e-05,
    # Neptune
    6.513035824661948e-05, 3.156802405838206e-03, -6.614325181016875e-05
])

# Masses of celestial bodies (in kg)
masses = [
    1.988410e30,  # Sun
    3.302e23,     # Mercury
    48.685e23,    # Venus
    5.97219e24,   # Earth
    7.349e22,     # Moon
    6.4171e23,    # Mars
    1898.18722e24,# Jupiter
    5.6834e26,    # Saturn
    86.813e24,    # Uranus
    102.409e24    # Neptune
]

# Names of celestial bodies
body_names = [
    "Sun",
    "Mercury",
    "Venus",
    "Earth",
    "Moon",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]