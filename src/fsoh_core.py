"""
fsoh_core.py

Minimal core logic for the Fractal Sparse-Origin Hypothesis (FSOH) model.
"""

from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

from .fsoh_fractal_field import generate_fractal_field


@dataclass
class SparseOriginConfig:
    """
    Configuration parameters for the minimal FSOH model.
    """
    size: int = 512
    field_iterations: int = 5
    threshold: float = 0.65   # Morphological eligibility threshold
    sparsity: float = 1e-4    # Probability for an eligible site to become an origin
    seed: int = 42            # Random seed for reproducibility


class SparseOriginModel:
    """
    Minimal FSOH model: fractal habitat + sparse origin sampling.
    """

    def __init__(self, config: SparseOriginConfig | None = None) -> None:
        if config is None:
            config = SparseOriginConfig()
        self.config = config

        self.field: np.ndarray | None = None
        self.eligible: np.ndarray | None = None
        self.origins: np.ndarray | None = None

    def run(self) -> None:
        """
        Run the minimal FSOH pipeline:

        1. Generate fractal-like habitat field.
        2. Apply threshold to obtain structurally eligible regions.
        3. Apply sparse origin sampling to obtain actual life-origin sites.
        """
        cfg = self.config

        # Step 1: fractal-like field
        self.field = generate_fractal_field(
            size=cfg.size,
            iterations=cfg.field_iterations,
            seed=cfg.seed,
        )

        # Step 2: eligibility mask (morphological constraint)
        self.eligible = self.field > cfg.threshold

        # Step 3: sparse origin sampling on eligible sites
        rng = np.random.default_rng(cfg.seed + 1)
        random_map = rng.random(self.eligible.shape)

        self.origins = (random_map < cfg.sparsity) & self.eligible

    def plot(self) -> None:
        """
        Visualize the habitat field, eligible regions, and sparse origins.
        """
        if self.field is None or self.eligible is None or self.origins is None:
            raise RuntimeError("Model has not been run yet. Call run() first.")

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        # 1. Raw field
        im0 = axes[0].imshow(self.field, cmap="viridis")
        axes[0].set_title("Fractal-like Habitat Field")
        fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)

        # 2. Eligible regions
        im1 = axes[1].imshow(self.eligible, cmap="gray")
        axes[1].set_title(f"Eligible Regions (field > {self.config.threshold})")
        fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

        # 3. Sparse origins overlay
        axes[2].imshow(self.eligible, cmap="gray")
        axes[2].imshow(self.origins, cmap="Reds", alpha=0.7)
        axes[2].set_title(
            f"Sparse Origins (p = {self.config.sparsity:.1e})"
        )

        for ax in axes:
            ax.set_xticks([])
            ax.set_yticks([])

        fig.suptitle("Minimal FSOH Simulation", fontsize=14)
        plt.tight_layout()
        plt.show()
