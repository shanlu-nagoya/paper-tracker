# Hybrid Classical-Quantum Variational Autoencoder for Neural Topic Modeling

## Metadata
- **Authors**: Ivan Kankeu
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/d204a6a1189ab6de0bd6afdfe0bf05cc6478f94e
- **arXiv**: https://arxiv.org/abs/2606.13852
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-15

## Abstract
Neural topic models enable scalable semantic discovery, but their integration with quantum hardware remains largely unexplored. We present a proof-of-concept hybrid classical-quantum variational autoencoder (VAE) for topic modeling, embedding parameterized quantum circuits within the VAE inference network while retaining a classical topic-word decoder. To address the resource constraints of quantum hardware, we propose a modified Gaussian Softmax posterior that decouples latent space dimensionality from the number of topics to be extracted, enabling the model to operate with a low-resource 10-qubit quantum device. On the AgNews dataset, the hybrid VAE outperforms state-of-the-art neural topic models (NTMs), reaching a $C_v$ coherence score of 0.71 and an NPMI score of 0.20 while preserving high topic diversity. For comparison, we also construct a fully classical variant, which also outperforms state-of-the-art models on AgNews and exhibits clear class separation in the latent space. These results demonstrate that hybrid VAEs are computationally viable even on NISQ-era devices and represent a promising direction for quantum-enhanced topic modeling.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
