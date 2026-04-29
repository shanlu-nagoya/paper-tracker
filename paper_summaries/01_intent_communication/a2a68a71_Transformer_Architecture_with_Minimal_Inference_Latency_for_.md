# Transformer Architecture with Minimal Inference Latency for Multi-Modal Wireless Networks

## Metadata
- **Authors**: Minsu Kim, Walid Saad, Kui Wang, Zongdian Li, Tao Yu et al. (+1)
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/a2a68a71fb9558bcfb2aeaab236144460f38f6ae
- **arXiv**: https://arxiv.org/abs/2604.18965
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-04-29

## Abstract
Next-generation wireless networks are expected to leverage multi-modal data sources to execute various wireless communication tasks such as beamforming and blockage prediction with situational-awareness. To do so, multi-modal transformers emerged as an effective tool, however, existing transformer-based approaches suffer from high inference latency and large memory footprints when processing multi-modal data. Hence, such existing solutions cannot handle wireless communication tasks that require fast inference to track a dynamically changing environment with moving vehicles and blockages. One major bottleneck is the reliance on attention mechanisms whose complexity grows quadratically with respect to the number of tokens. Hence, in this paper, a novel, fast multi-modal transformer inference framework is designed to practically support wireless communication tasks by processing only important tokens. To this end, an optimization problem is formulated to find the optimal number of tokens under a target FLOPs for a given wireless communication task while maintaining the task accuracy. To solve this problem, modality-specific tokenizers are first designed to project each modality into the same embedding dimension. Then, a token router is introduced to learn the importance of each token and process only important tokens. Subsequently, a trainable keep ratio is introduced to learn how many tokens to process for each layer under the target FLOPs. Simulation results show that, on DeepSense 6G beamforming tasks, we can reduce the inference latency, GPU memory, and FLOPs by 86.2% 35%, and 80%, respectively, with negligible accuracy loss. To validate the feasibility for real-world deployments, a multi-modal handover dataset is developed using a real-world testbed. Emulation results on the developed dataset show that the proposed framework can proactively initiate handover before blockage.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
