# Bitwise Over-Parameterized Neural Polar Decoding: A Theoretical Performance Analysis

## Metadata
- **Authors**: Hongzhi Zhu, Wei Xu, Xiaohu You
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/343ffb42b7dcf6a1e7e8e110ad5bbd52b6dfef9e
- **arXiv**: https://arxiv.org/abs/2604.27689
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
This paper proposes a bitwise over-parameterized neural network (ONN) decoder for polar-coded transmission and develops a tractable theoretical performance analysis framework. By modeling each synthesized message channel as an individual supervised regression task, the proposed decoder preserves the successive structure of polar decoding while enabling a communication-oriented integration of neural-network learning theory and polar-code reliability analysis. Under over-parameterization, we first characterize the empirical convergence behavior of each bitwise ONN and show that the training trajectory remains close to the random initialization. By expressing the empirical MSE convergence in the dB domain, the result further reveals a per-iteration training gain determined by the learning rate, the bit-channel Gram spectrum, and the training-set size. Upon this observation, we then derive a population mean squared error (MSE) bound via local generalization analysis and convert it into a bitwise decoding error bound through the posterior-margin structure of the bitwise maximum a posteriori (MAP) target. Under additive white Gaussian noise (AWGN) channels, a Gaussian approximation (GA)-based characterization of the low-margin probability is further established, which leads to explicit bounds for the bit error rate (BER) and block error rate (BLER). The analysis clarifies how the hidden-layer width affects optimization, generalization, and the final decoding performance, thereby providing theoretical guidance for network-scale selection. Numerical results validate the main theoretical findings and show that increasing the network width consistently improves both oracle-aided and sequential decoding performance.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
