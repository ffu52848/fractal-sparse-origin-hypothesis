"""
fsoh_fractal_field.py

Minimal fractal-like habitat field generator for FSOH.
"""

import numpy as np


def generate_fractal_field(
    size: int = 512,
    iterations: int = 5,
    seed: int | None = 42,
) -> np.ndarray:
    """
    Generate a simple fractal-like scalar field on a 2D grid.

    Parameters
    ----------
    size : int
        Size of the square grid (size x size).
    iterations : int
        Number of smoothing iterations to introduce large-scale structure.
    seed : int | None
        Random seed for reproducibility. If None, do not fix the seed.

    Returns
    -------
    field : np.ndarray
        2D array of shape (size, size) with values in [0, 1].
    """
    if seed is not None:
        np.random.seed(seed)

    # Start from uniform random noise
    field = np.random.rand(size, size)

    # Very simple "fractal-like" smoothing:
    # repeatedly average with shifted copies to create correlations.
    for _ in range(iterations):
        field = (
            field
            + np.roll(field, 1, axis=0)
            + np.roll(field, -1, axis=0)
            + np.roll(field, 1, axis=1)
            + np.roll(field, -1, axis=1)
        ) / 5.0

    # Normalize to [0, 1]
    field_min = field.min()
    field_max = field.max()
    if field_max > field_min:
        field = (field - field_min) / (field_max - field_min)

    return field
