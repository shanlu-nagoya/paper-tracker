# JOMP: Jointly-Optimized Mixed-Precision Quantization Across Neural Video Coding Frameworks and Buffering Strategies

## Metadata
- **Authors**: Yu-Hsiang Lin, R. Conceiccao, Chunyan Wu, Huu-Tai Phung, Tzu-Hsiang Chou et al. (+3)
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/c1ae67be0b292f2cd0ae7604cfafe7fb6e1141c5
- **arXiv**: https://arxiv.org/abs/2606.13110
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-15

## Abstract
Variational autoencoder-based neural video coding has demonstrated impressive rate-distortion performance. However, its adoption in real-world applications remains hindered by challenges, such as prohibitively high computational complexity and limited cross-platform interoperability. These issues are often overlooked, as most neural video codecs rely on floating-point arithmetic to fully explore their rate-distortion potential. Practical deployment, however, requires integer-based implementations. Converting floating-point implementations into integer-based networks is non-trivial, since it involves quantizing inter-dependent coding components, whose sensitivity to precision may vary across codec designs. This paper introduces a Jointly-Optimized Mixed-Precision (JOMP) framework, in which both quantization parameters and bit widths are treated as learnable variables during training. This enables different codec modules to operate at varying precision levels, thereby jointly optimizing the rate-distortion-complexity trade-off. To the best of our knowledge, JOMP is the first mixed-precision quantization framework for neural video codecs. Its effectiveness is validated through a systematic investigation of quantization across different coding frameworks and temporal buffering strategies. Our study marks the first attempt to a unified understanding of the combined effects of modern coding frameworks and temporal buffering strategies, with the aim of informing future development of neural video codecs from a practicality perspective. In addition, we develop a complete integerization pipeline to achieve deterministic decoding. Overall, when applied to our best-performing model, JOMP enables end-to-end mixed-precision learning for integer neural video codecs, achieving rate-distortion performance comparable to that of the state-of-the-art DCVC-FM while reducing bit operations by 87.6%.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
