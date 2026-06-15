# Ultra Flash: Scaling Real-Time Streaming Video Generation to High Resolutions

## Metadata
- **Authors**: Luxury, Jie Huang, Zihao Fan, Xiaoxiao Ma, Yuming Li et al. (+23)
- **Year**: 2026
- **Venue**: 
- **Topic**: Mission Reliability
- **Keyword matched**: `ultra-reliable low-latency URLLC`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/deefcd232eba1847b2b68826bc4da587101c06ce
- **arXiv**: https://arxiv.org/abs/2606.09150
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-15

## Abstract
While recent autoregressive video diffusion models achieve remarkable streaming quality, they remain confined to low resolutions (e.g., 480P), leaving efficient, scalable, real-time high-resolution video generation a fundamental open challenge. To bridge this gap, we present Ultra Flash, a cascaded streaming framework capable of real-time high-resolution video generation. Ultra Flash achieves ~30 FPS at 1K resolution and ~18 FPS at 2K resolution on a single GPU through three key contributions: (1) an architecture-preserving T2V-to-TV2V super-resolution training paradigm coupled with an AIGC-oriented data degradation pipeline that effectively preserves the generative capability of the base model, enabling enhanced high-resolution detail when cascaded after mainstream low-resolution generative models; (2) a causal streaming latent upsampler paired with a high-resolution decoder, which enhances spatiotemporal coherence while enabling efficient latent spatial scaling and precise high-resolution decoding with negligible computational overhead; and (3) a cascade high-resolution streaming video generation optimization scheme that first performs hybrid-reward-enhanced sparse causalization and single-step distillation of the super-resolution model, then introduces cascaded streaming self-forcing preference optimization with dynamic cache management, jointly enhancing overall coherence, improving quality, and enabling real-time high-resolution streaming video generation. Extensive experiments demonstrate that Ultra Flash reliably produces ultra-high-resolution streaming video while maintaining state-of-the-art visual quality and superior efficiency.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
