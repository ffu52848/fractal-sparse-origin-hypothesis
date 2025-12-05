# Fractal Sparse-Origin Hypothesis (FSOH)

**Fractal Sparse-Origin Hypothesis (FSOH)** proposes that the emergence and distribution of life in the universe follow a **fractal, sparse, and strongly constrained structure**, rather than a uniform or weakly random process.  

This repository provides the conceptual framework, mathematical skeleton, and (in future versions) computational tools for exploring the FSOH model.

---

## 1. Overview

FSOH addresses two core questions:

1. **Why is life extremely rare, despite the vastness of the universe?**  
2. **Why do local environments that support life appear as “fractal oases” rather than uniformly distributed habitats?**

The hypothesis assumes that:

- Life is not only constrained by local chemistry and temperature,  
- But also by **multi-scale structural conditions** that follow a **fractal and sparse** pattern in space, time, and underlying physical fields.

FSOH is designed as a **structure-level model**:  
it does not depend on any specific biochemistry, but rather on abstract constraints on where life *can* appear.

---

## 2. Core Ideas

FSOH is built on the following conceptual pillars:

- **Fractal Structure**  
- **Sparse Origin**  
- **Constraint Layers**  
- **Effective Observational Bias**

These elements collectively imply that life is extraordinarily rare and strongly clustered in fractal-like “habitable nodes.”

---

## 3. Axioms (Conceptual Form)

**Axiom 1 – Fractal Habitat Structure**  
**Axiom 2 – Multi-Layer Constraints**  
**Axiom 3 – Sparse Effective Origin**  
**Axiom 4 – Observer Selection**

(Equations and full logical derivations included in the paper.)

---

## 4. Model Structure (Conceptual Skeleton)

A simplified mapping:

\[
S \xrightarrow{F} S_F \xrightarrow{\mathcal{K}} S_{\text{eligible}} \xrightarrow{\mathcal{O}} S_{\text{life}}
\]

Future code will include:

- Fractal region generators  
- Constraint layer operators  
- Sparse-origin sampling  
- Visualization tools  

---

## 5. Relation to Other Models

FSOH is compatible with:

- **FDM** (Fractal Dark Matter Model)  
- **AFSM** (Anthropic Fractal Selection Model)  
- **ASIT** (Absolute Space–Interface Topology)

---

## 6. Repository Structure (Planned)

```text
fractal-sparse-origin-hypothesis/
├─ README.md
├─ docs/
│  ├─ FSOH_paper.pdf
│  └─ notes/
├─ src/
│  ├─ fsoh_core.py
│  ├─ fsoh_fractal_field.py
│  ├─ fsoh_constraints.py
│  └─ fsoh_simulation.py
├─ notebooks/
│  └─ FSOH_demo.ipynb
└─ figures/
   └─ *.png
```
````  ← **這行反引號非常重要**（關閉 code block）

````markdown
## 7. How to Use (Future Code Plan)

```python
from fsoh_core import SparseOriginModel

model = SparseOriginModel(
    domain_size=1024,
    fractal_dimension=1.6,
    constraint_layers=3,
    seed=42,
)

result = model.run_simulation()
model.plot(result)
```

(Example only; API subject to change.)

---

## 8. Documentation and Paper

The formal exposition of FSOH is archived on Zenodo.

### DOI  
**https://doi.org/10.5281/zenodo.17787315**

The PDF will also be mirrored under `docs/` in this repository.

---

## 9. Citation

If you reference this hypothesis, please cite:

**Author, A. (2025).  
Fractal Sparse-Origin Hypothesis (FSOH): A Fractal Model of Life Emergence and Distribution.  
Zenodo. https://doi.org/10.5281/zenodo.17787315**

### BibTeX

```bibtex
@misc{FSOH_2025,
  author       = {Author, A.},
  title        = {Fractal Sparse-Origin Hypothesis (FSOH): A Fractal Model of Life Emergence and Distribution},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17787315},
  url          = {https://doi.org/10.5281/zenodo.17787315}
}
```

---

## 10. License / Rights

All rights are reserved by the author unless otherwise specified.  
For reuse or adaptation, please contact the author or refer to future updates.
