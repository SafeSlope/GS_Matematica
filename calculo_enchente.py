"""
CitizenTech Flood Prediction Model
Modeling urban street water accumulation using Differential and Integral Calculus.
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# =============================================================================
# Step 1: Project Setup & Variables
# =============================================================================

# Symbolic time variable t (measured in hours over a 6-hour storm event: 0 <= t <= 6)
t = sp.Symbol("t")

# Base rain intensity function r(t) = -2t^2 + 12t (in mm/h)
r_t = -2 * t**2 + 12 * t

# Constant street drain capacity / drainage rate (in mm/h)
drainage_rate = 8
