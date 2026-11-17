# Data sources and extraction

`block_observations.csv` contains 6,720 block-level rows extracted from the original authors' processed MATLAB arrays: 2 studies × 12 participants × 2 schedules × 70 blocks × 2 response windows. Compensation is dimensionless; feedback is force in N. The two rows for a block use different feedback windows and repeat its compensation value. Participant indices are study-local anonymized indices.

- Franklin & Franklin (2021), *Feedback Gains modulate with Motor Memory Uncertainty*. DOI: 10.51628/001c.22336. Figshare record 12816086; metadata records CC BY 4.0. Source archive: https://ndownloader.figshare.com/files/24313367 (approximately 2.5 GB).
- Franklin & Franklin (2023), *Visuomotor feedback tuning in the absence of visual error information*. DOI: 10.51628/001c.91252. Figshare record 23271833; metadata records CC BY 4.0. Source archive: https://ndownloader.figshare.com/files/41018855 (approximately 2.7 GB).

The CSV is a derived extraction of these CC BY 4.0 data. Retain attribution to the source authors and identify this processing when reusing it. Raw author files are not modified. Metadata preserve archive filenames, URLs and MD5 digests.

To verify extraction, download the two archives above, verify their MD5 against the corresponding metadata, and place the following members under `public_data/raw/`:

```text
visual_errors/visRJ_A_2018.mat
visual_errors/visRJ_B_2018.mat
visual_errors/RJforcecomp_1_2018.mat
visual_errors/RJforcecomp_2_2018.mat
visual_clamp/visRJ2_A.mat
visual_clamp/visRJ2_B.mat
visual_clamp/RJ2forcecomp_1.mat
visual_clamp/RJ2forcecomp_2.mat
```

Then run `python analysis/verify_extraction.py --raw-dir public_data/raw`. The file `analysis/extraction_check.json` records the expected SHA-256 digests and a completed 6,720-row equality check. Extraction uses the authors' waveform indexing and a day-B participant rotation of six, as documented in the script.

Localization uses Gastrock et al. (2020), *External error attribution dampens efferent-based predictions but not proprioceptive changes in hand localization*, DOI: 10.1038/s41598-020-76940-3. Source deposit: https://osf.io/xdgh6/. Four `*_loc_p3_AOV.csv` files contain the source authors' circle-corrected, spatially interpolated participant estimates. Retrieve them with `python public_data/fetch_localization.py`. SHA-256 digests and source URLs come from the recorded download manifest. Analysis averages three directions within each participant and uses rotated-minus-aligned contrasts.

Source localization CSVs are downloaded from their original deposit, not mirrored here. `analysis/localization_participants.csv` and `analysis/localization_summary.json` contain the secondary-analysis contrasts and bootstrap summaries used in the manuscript. There are no participant names or contact details in these analysis files.
