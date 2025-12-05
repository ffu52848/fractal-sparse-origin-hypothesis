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
  The universe exhibits nested structures (from large-scale cosmic web down to planetary environments).  
  FSOH assumes that *life-eligible regions* follow a similar nested pattern.

- **Sparse Origin**  
  Even within life-friendly zones, the *actual* emergence of life is **highly suppressed** and occurs only in a small subset of possible sites.

- **Constraint Layers**  
  The model separates constraints into multiple layers (e.g. cosmic, galactic, planetary, micro-environmental), each acting as a “filter” that reduces the probability of life.

- **Effective Observational Bias**  
  Any observer (such as humans) will, by construction, find themselves in a rare, high-constraint-satisfied region, creating strong selection effects.

---

## 3. Axioms (Conceptual Form)

FSOH can be summarized by a small set of axioms.  
The exact mathematical formalizations are left to the accompanying paper, but the logical form is:

**Axiom 1 – Fractal Habitat Structure**  
The set of regions that can in principle host life can be represented as a **fractal subset** of the underlying physical space (or state space), with non-trivial dimension \( D_f \) and strong scale dependence.

**Axiom 2 – Multi-Layer Constraints**  
The probability that life can *emerge* in a given region is determined by the intersection of multiple constraint layers:
\[
\mathcal{C} = \mathcal{C}_{\text{cosmic}} \cap \mathcal{C}_{\text{galactic}} \cap \mathcal{C}_{\text{stellar}} \cap \mathcal{C}_{\text{planetary}} \cap \mathcal{C}_{\text{micro}}
\]

**Axiom 3 – Sparse Effective Origin**  
Even in regions that satisfy all constraints \(\mathcal{C}\), the actual emergence of life is governed by an additional suppression factor, resulting in a **sparse set** of realized origins.

**Axiom 4 – Observer Selection**  
All observations of “typical” environments are intrinsically biased by the existence of observers.  
Thus, observable habitats are not representative of the global ensemble, but of a *filtered* subset extremely biased toward life-permitting conditions.

---

## 4. Model Structure (Conceptual Skeleton)

In a simplified form, FSOH can be expressed as:

- A **state space** \( S \) of possible regions/environments  
- A **fractal mask** \( F \subset S \) selecting structurally eligible regions  
- A **constraint operator** \( \mathcal{K} \) applying multi-layer filters  
- A **sparse origin operator** \( \mathcal{O} \) assigning actual life emergence  

Schematically:
\[
S \xrightarrow{F} S_F \xrightarrow{\mathcal{K}} S_{\text{eligible}} \xrightarrow{\mathcal{O}} S_{\text{life}}
\]

Future code in this repository will implement toy models of:

- Generating fractal subsets of a domain  
- Applying layered constraints  
- Measuring the sparsity and clustering of life-origin candidates  
- Visualizing the resulting distributions  

---

## 5. Relation to Other Models

FSOH is designed to be compatible with several other theoretical frameworks by the same author, including (not implemented here yet):

- **Fractal Dark Matter Model (FDM)**  
- **Anthropic Fractal Selection Model (AFSM)**  
- **ASIT (Absolute Space–Interface Topology)**  

This repository focuses solely on **FSOH as a stand-alone hypothesis**, while keeping interfaces open for future integration.

---

## 6. Repository Structure (Planned)

```text
fractal-sparse-origin-hypothesis/
├─ README.md                  # This document
├─ docs/
│  ├─ FSOH_paper.pdf         # Main paper (to be added)
│  └─ notes/                 # Additional notes or slides
├─ src/
│  ├─ fsoh_core.py           # Core model abstractions (planned)
│  ├─ fsoh_fractal_field.py  # Fractal field generators (planned)
│  ├─ fsoh_constraints.py    # Multi-layer constraints (planned)
│  └─ fsoh_simulation.py     # Simple simulations / experiments (planned)
├─ notebooks/
│  └─ FSOH_demo.ipynb        # Example Jupyter notebook (planned)
└─ figures/
   └─ *.png                  # Diagrams, visualizations (planned)
```

---

## 7. How to Use (Future Code Plan)

Once the Python modules are added, a minimal usage pattern may look like:

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

This is **illustrative only** and does not represent a finalized API.

---

## 8. Documentation and Paper

The formal exposition of FSOH, including:

- Detailed axioms  
- Mathematical framework  
- Conceptual implications for astrobiology  
- Possible observational consequences  

will be provided in the accompanying paper under `docs/` once uploaded.

### DOI

This hypothesis is formally archived on Zenodo:

**https://doi.org/10.5281/zenodo.17787315**

---

## 9. Citation

If you reference or build upon the Fractal Sparse-Origin Hypothesis (FSOH), please cite:

**Ku, Yung-Cheng. (2025).  
Fractal Sparse-Origin Hypothesis (FSOH): A Fractal Model of Life Emergence and Distribution.  
Zenodo. https://doi.org/10.5281/zenodo.17787315**

### BibTeX

```bibtex
@misc{Ku_FSOH_2025,
  author       = {Ku, Yung-Cheng},
  title        = {Fractal Sparse-Origin Hypothesis (FSOH): A Fractal Model of Life Emergence and Distribution},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17787315},
  url          = {https://doi.org/10.5281/zenodo.17787315}
}
```

---

## 10. License / Rights

By default, all rights are reserved by the author unless explicitly stated otherwise.

If you wish to reuse or adapt the contents of this repository,  
please contact the author or refer to future updates of this section.

---
