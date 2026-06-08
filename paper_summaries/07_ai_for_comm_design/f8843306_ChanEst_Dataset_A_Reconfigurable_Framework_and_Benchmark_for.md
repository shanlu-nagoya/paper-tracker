# ChanEst Dataset: A Reconfigurable Framework and Benchmark for Deep Learning–Based 6G Channel Estimation

## Metadata
- **Authors**: O. Okoyeigbo, Xutao Deng, R. Sheriff, Daniel Jeremiah, Olamilekan Shobayo
- **Year**: 2026
- **Venue**: Telecom
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/f884330658a4d2e3a9c639d74b12a499d4a42343
- **arXiv**: N/A
- **DOI**: 10.3390/telecom7030065
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
Accurate channel estimation is essential for reliable wireless communication, yet it becomes significantly challenging in 6G due to extreme propagation conditions. Factors such as high mobility, large delay spreads, and low signal-to-noise ratios (SNRs) create environments where traditional estimators struggle to perform effectively. While deep learning (DL)–based channel estimation has emerged as an alternative approach, its advancement is hindered by the lack of standardized and reproducible datasets that follow 3GPP-compliant signal models and realistic receiver preprocessing. This paper introduces ChanEst, a reproducible dataset generation framework for DL-based channel estimation. The ChanEst dataset uses 3GPP-compliant physical-layer procedures, demodulation reference signals (DMRS), tapped delay line (TDL) channel models, and FR3 (Frequency Range 3) configurations, performing stratified random sampling of key channel parameters to ensure statistical diversity. Least squares (LS) estimates are obtained and interpolated across the time–frequency grid to construct practical receiver input tensors, while the corresponding labels are derived from the perfect channel responses produced by the channel model. The resulting datasets are stored as real-valued tensors suitable for DL models and accompanied by metadata logs to enable stratified evaluation and fair benchmarking. Comprehensive statistical analysis validates the dataset’s diversity and physical consistency, and a fully implemented DL baseline model demonstrates its practical machine learning utility by outperforming conventional estimators under severe channel impairments. The ChanEst dataset is publicly available on Mendeley Data, with full code provided on GitHub, enabling reproducible experimentation for DL-based 6G channel estimation.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
