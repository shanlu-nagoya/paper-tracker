# DriftDecode: One-Step Wireless Image Decoding via Drifting-Inspired Detail Recovery

## Metadata
- **Authors**: Jingwen Fu, Ming Xiao, Mikael Skoglund
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/392c3e30dd86ac28cfc5c07e2300f7588c051173
- **arXiv**: https://arxiv.org/abs/2605.02325
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-11

## Abstract
Generative receivers for wireless image transmission can improve reconstruction quality, but diffusion-based and flow-based decoding relies on iterative inference and therefore incurs substantial latency. In wireless image transmission, however, the received signal already preserves the coarse structure of the source image. Wireless decoding is therefore better viewed as a recovery task than as image generation from scratch, and the main challenge lies in restoring channel-impaired details. Motivated by this recovery-oriented perspective, this paper proposes DriftDecode, a signal-to-noise ratio (SNR)-conditioned one-step decoder for wireless image reconstruction. DriftDecode couples a one-step U-Net decoder with a drift-inspired instance-level texture loss. The loss reformulates the drifting-field mechanism from generative drifting models in perceptual feature space, guiding each reconstructed local feature toward its spatially aligned ground-truth counterpart while suppressing mismatched textures. Experiments on DIV2K and MNIST under additive white Gaussian noise (AWGN) and Rayleigh fading channels show a favorable quality-latency tradeoff. DriftDecode achieves 30~ms decoding latency, providing a 4.8$\times$ speedup over a 10-step flow-matching decoder, while consistently outperforming MSE-only training and yielding up to 1.13~dB PSNR gain on MNIST under Rayleigh fading. These results support recovery-oriented one-step decoding as an effective alternative to iterative generative decoding for low-latency wireless image transmission.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
