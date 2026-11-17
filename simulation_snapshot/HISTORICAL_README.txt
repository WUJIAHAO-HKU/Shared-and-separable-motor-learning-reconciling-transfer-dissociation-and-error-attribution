Identifiability follow-up, 17 November 2026

Scope: all prospective responses are simulations. noise_library.npz is an inherited
24-participant processed-block residual library. See noise_provenance.json.
No new human data were collected. The calibration precision and routing effect
sizes are assumptions for design sensitivity; they are not estimates from that archive.

Core scripts (Python 3, numpy, scipy, matplotlib):
python interventions.py --audit
python interventions.py --design calibrated --people 48 --reps 4 --seed 9561117 --starts 8
python interventions.py --design calibrated --people 96 --reps 16 --seed 9561117 --starts 8
python interventions.py --design calibrated --people 96 --reps 16 --seed 9561117 --starts 8 --near
python interventions.py --design calibrated --people 96 --reps 16 --seed 9561117 --starts 8 --miscal 0.2
python verify_summarize.py
python invariant.py
python mixing_stress.py
python contrast.py
python plots.py
python report.py
xelatex -interaction=nonstopmode -halt-on-error identifiability_en.tex
xelatex -interaction=nonstopmode -halt-on-error identifiability_zh.tex
python qa_report.py

Exploratory four-family screens are archived in the coupled/crossed/orthogonal files.
Use --legacy-four --seed 9261117 --people 48 --reps 4 --starts 5 for those designs.
Their original matrix bounds were [-2,2]; final source uses [-4,4] after a generating
support audit, so rerunning the early screens with final bounds can change those fits.
All final calibrated comparisons were rerun with the widened bounds. No comparison
requires separate updating to have zero cross-transfer or a nonzero difference from sharing.

Model labels: S1 scalar source modulation, rank-one effective map; S2 scalar, free map;
R1 source-specific rank-one maps; R2 source-specific free maps; G separable row/column gains.
These are effective impulse kernels, not complete neural circuits. Sensory-error input
columns are not direct selective interventions on feedforward/feedback learning pathways.
Every family has independent output retention and readout gain. Auxiliary calibration is
jointly fitted through its measurement likelihood. Independent calibration transport is
an assumption that a real pilot must validate.

invariant.py: scalar/row/column-gain-controlled Q interaction. Values are centered on
analytic population targets for Monte Carlo power; raw finite-pool power is also saved.
mixing_stress.py: non-diagonal input mixing plus independent noisy calibration;
two independent repetition halves and cross-products avoid correlated-product bias.
These displayed rates do not cover arbitrary calibration bias or nonlinear input mixing.
contrast.py: earlier simpler signed contrast, retained as an exploratory comparison;
it does not eliminate separable input/output gain changes and is not the primary endpoint.

Source-cue training, active/passive localization, independent readout and retention
calibration, matched corrective responses, context-retrieval controls and held-out
compound-error tests are required. Eight teaching cells specify the smallest core
factorial contrast; they do not include all nuisance/control sessions.

No human sample size is certified. Conditional Q power is reported for explicit effect
assumptions. Whole-family recovery remains poor. Equal input-output kernels leave
shared storage and synchronized separate storage observationally equivalent.

AI assisted implementation, analysis, verification and bilingual writing. Numerical
plots are generated from saved computation arrays; no generated pixels encode data.
