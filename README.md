# Shared and separable motor learning

**Reconciling transfer, dissociation and error attribution**

JiaHao Wu and Long Zeng — Tsinghua Shenzhen International Graduate School, Tsinghua University.
Corresponding author: Long Zeng, zenglong@sz.tsinghua.edu.cn.

This repository accompanies a Perspective manuscript. It integrates evidence about motor-learning transfer, dissociation, error attribution and sensory-specific learning and connects those observations to experimental comparisons. Public-data reanalyses and constructed counterexamples characterize the inferences available from measured responses. The repository is a manuscript and reproducibility release, dated 18 November 2026.

## Read the manuscript

- [English manuscript](perspective_en.pdf) and [中文正文](perspective_zh.pdf)
- [English evidence atlas](evidence_atlas_en.pdf) and [中文证据图谱](evidence_atlas_zh.pdf)
- [Editable bilingual concept figures](editable_figures/concept_figures_bilingual.pptx): four slides, Figures 1–2 in English followed by Chinese.
- [Reproducibility archive](dist/reproducibility_package.zip)

Figures 1–2 were rebuilt using the installed Windows Microsoft PowerPoint application through COM. Their text, symbols, shapes and connectors are native editable objects. They contain no embedded raster images. The manuscript uses PowerPoint-exported vector PDFs. Earlier drafts used OpenAI image generation; the current reconstruction used AI-assisted layout code. Quantitative plots are generated from analysis arrays. See [figure provenance](image_provenance_native.json) and [native-object audit](editable_figures/native_audit.json).

## Reproduce and verify

Create a Python environment and install `requirements.txt`. `requirements-lock.txt` and `environment.json` record the tested environment. Numerical results can vary slightly across BLAS/library versions.

```bash
python -m pip install -r requirements.txt
python reproduce.py --mode verify
```

Verification checks package hashes when a manifest is present, re-evaluates held-out participant scores from stored fitted parameters and the deposited block data, checks the analytic counterexample and numerical basis, and audits editable figure objects. It does not rerun parameter optimization.

To regenerate localization estimates, constructed examples, plots and all four manuscripts:

```bash
python reproduce.py --mode figures
python reproduce.py --mode manuscripts
```

The figures mode downloads four required localization CSVs from the original public OSF deposit and verifies their recorded SHA-256 hashes. These source files are retrieved separately because an explicit redistribution licence was not present in the inspected OSF node metadata. The force-field processed block table and dataset metadata are included, with attribution and licence information in [public_data/README.md](public_data/README.md).

To rerun source-only fitting, cross-study prediction, model recovery and the independent optimization audit:

```bash
python reproduce.py --mode full
```

This runs the full configured optimization budgets and may take hours. It overwrites derived results in the working copy; retain a clean release copy for comparison. Full mode includes the figure and manuscript rebuild. The historical intervention simulations are a separate, clearly labelled snapshot; they are not required for the current temporal-model refit. Their saved run-level records and original commands are in `simulation_snapshot/`.

## Build requirements

Manuscript compilation uses XeLaTeX and BibTeX on `PATH` (MiKTeX or TeX Live), with Times New Roman and Arial. The Chinese version additionally uses SimSun, SimHei, KaiTi and Microsoft YaHei. Prepared PDFs are available without those dependencies.

Figure reconstruction requires Windows and installed Microsoft PowerPoint. To regenerate the four concept figures:

```powershell
powershell -NoProfile -File editable_figures/rebuild.ps1
```

The script creates native slides from the deposited layout JSON, exports PNG/PDF, assembles the four-slide deck and copies the vector figures into `figures/`. It closes only presentations it creates. Close an output deck before rebuilding that same output file.

## Contents and interpretation

- `analysis/`: temporal-model fitting, predictions, participant scores, recovery, calibration examples and localization analysis.
- `public_data/`: 6,720 processed force-field block observations, source metadata, retrieval scripts and data documentation.
- `evidence_map_bilingual.json`: 29 experiment-level evidence records; companion JSONs contain claim audits, eight experiment-selection rules and measurement-removal comparisons.
- `editable_figures/`: native PPTX files, vector PDFs, previews, layouts, reconstruction code and audits.
- `simulation_snapshot/`: inherited intervention-design simulations, noise library, run-level records and provenance. Their calibration selectivity is a design assumption.
- `build.py`, supporting modules and `.tex` files: paired manuscript/evidence-atlas sources.

The analyses are retrospective. Two force-field studies contribute 24 participants; localization estimates cover 90 participants. Target post-exposure observations are withheld from fitting and penalty selection; target pre-exposure calibration and source-baseline-only scoring are both reported. Recovery compares overlapping effective temporal-response families. Behavioural equivalence between shared states and duplicated states remains explicit in the manuscript.

No new human experiment was conducted for this release. Existing results, including model-ranking changes and unresolved comparisons, are retained. The final 18 November editorial revision explains the increment relative to prior work, develops the early-transfer/late-dissociation case and reports family-specific recovery. Main-text scientific conclusions point to Supplementary Methods SM1–SM3 for derivations, report-loadings analysis, optimization and recovery procedures. Numerical observations, fitted parameters and predictions are unchanged. `final_content.py` and `supplementary_methods.py` contain the paired final revision; `build.py` generates the manuscript and atlas from these sources. Private synopsis and editorial-email files are distributed separately from this public repository.

## Attribution and AI assistance

Source-study citations and dataset identifiers are in the manuscripts and data documentation. Third-party data retain their source terms. No blanket licence is asserted for third-party material. Article text, code and diagrams are provided for inspection and reproduction; the authors have not selected a general reuse licence for their original materials.

Language-model assistance supported literature organization, bilingual drafting, analysis-code preparation and figure-layout code. Source articles, private editorial correspondence and previous AI raster concept figures are excluded from this release.
