"""
run_fsoh_demo.py

Minimal demo script to run and visualize the FSOH model.
"""

from src.fsoh_core import SparseOriginModel, SparseOriginConfig


def main() -> None:
    # You can tweak these parameters if needed.
    config = SparseOriginConfig(
        size=512,
        field_iterations=5,
        threshold=0.65,
        sparsity=1e-4,
        seed=42,
    )

    model = SparseOriginModel(config)
    model.run()
    model.plot()


if __name__ == "__main__":
    main()
