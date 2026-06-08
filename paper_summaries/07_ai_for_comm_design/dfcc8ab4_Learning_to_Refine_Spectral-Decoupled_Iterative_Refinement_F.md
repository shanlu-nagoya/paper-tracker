# Learning to Refine: Spectral-Decoupled Iterative Refinement Framework for Precipitation Nowcasting

## Metadata
- **Authors**: Yunlong Zhou, Chen Zhao, Danyang Peng, Fanfan Ji, Xia Yuan
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/dfcc8ab462c783d8f0c4de66ce77ea42e4abce90
- **arXiv**: https://arxiv.org/abs/2606.02661
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
Accurate precipitation nowcasting is vital for disaster mitigation, but deep learning methods face a key trade-off: regression models produce over-smoothed, spectrally decaying predictions that blur convective details and violate turbulence power laws; diffusion models generate realistic yet unanchored hallucinations lacking physical grounding. We propose Spectral-Decoupled Iterative Refinement (SDIR), a deterministic framework that reformulates nowcasting as progressive frequency-decoupled refinement. SDIR first extracts a stable low-frequency synoptic skeleton, then iteratively refines high-frequency textures under physical constraints, eliminating both blurring and hallucinations. It features a dual-path design: the Synoptic Frequency-Guided Former (SFG-Former) with Scale-Adaptive Transformers for global structure, and the Fourier Residual Refiner (FR-Refiner) with Scale-Conditioned Fourier Neural Operators for fine residuals. A Physically Consistent Power Spectral Density (PCPSD) loss with dynamic masking enforces a turbulence-consistent spectral distribution. Experiments on three benchmarks show SDIR significantly outperforms SOTA methods in spatial accuracy while achieving spectral fidelity competitive with diffusion-based methods, enabling reliable high-resolution operational nowcasting. Code link: https://github.com/RuntimeWarning/SDIR.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
