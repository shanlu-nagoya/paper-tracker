# ZID-Net: Zero-Inference Diffusion Prior Decoupling Network for Single Image Dehazing

## Metadata
- **Authors**: Xinheng Li, Minghao Chen, Mengqing Wu, Yan Liu, Guanying Huo
- **Year**: 2026
- **Venue**: 
- **Topic**: Importance-Aware Coding
- **Keyword matched**: `importance-aware channel coding`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/e89ab8ec24ec6608a50e685f35decb6083cdac0c
- **arXiv**: https://arxiv.org/abs/2604.23709
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
Single image dehazing is often constrained by a trade-off between restoration quality and computational efficiency. While efficient, CNN networks struggle to learn robust priors for dense and non-homogeneous haze. Conversely, diffusion models provide strong generative priors but suffer from severe inference latency and sampling instability. To address these limitations, we propose ZID-Net, a novel framework that explicitly decouples diffusion supervision from feed-forward inference. For efficient inference, we design a frequency-spatial decoupled feed-forward backbone. Within this backbone, a Channel-Spatial Laplacian Mask (CSLM) filters haze-amplified noise to extract purified structural details, while Lightweight Global Context Blocks (LGCBs) establish long-range spatial dependencies to capture the global variations of haze. A Dynamic Feature Arbitration Block (DFAB) then adaptively fuses these semantic and structural features for robust reconstruction. To provide this backbone with physical priors without the inference cost, we introduce a Zero-Inference Prior Propagation Head (ZI-PPH) during training. ZI-PPH leverages a conditional diffusion process to predict residual noise, providing degradation-aware structural supervision to the backbone. By discarding the diffusion branch at test time, ZID-Net integrates diffusion priors into a pure feed-forward architecture for accurate and efficient restoration. ZID-Net achieves 40.75 dB PSNR on the synthetic RESIDE dataset and outperforms existing methods with a 1.13 dB gain on real-world datasets. Additionally, it yields a 3.06 dB PSNR gain on the StateHaze1k remote sensing dataset with an inference time of just 19.35 ms. The project code is available at: https://github.com/XoomitLXH/ZID-Net.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
