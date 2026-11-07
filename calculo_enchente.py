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

# =============================================================================
# Step 2: Calculus Implementation (Derivative & Integral)
# =============================================================================

# Rate of Change (Derivative context): dh/dt = r(t) - drainage_rate (in mm/h)
water_rise_rate = r_t - drainage_rate

# Accumulation (Integral context): h(t) = integral of (dh/dt) dt (in mm, with h(0) = 0)
h_t = sp.integrate(water_rise_rate, t)

