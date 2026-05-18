# LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?

## Metadata
- **Authors**: Xueqi Cheng, Yushun Dong
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/27235754640c7cdc652e428fbcc00527f5b931ec
- **arXiv**: https://arxiv.org/abs/2605.11301
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-18

## Abstract
Multimodal large language models (MLLMs) have heterogeneous strengths across OCR, chart understanding, spatial reasoning, visual question answering, cost, and latency. Effective MLLM routing therefore requires more than estimating query difficulty: a router must match the multimodal requirements of the current image-question input with the capabilities of each candidate model. We propose LatentRouter, a router that formulates MLLM routing as counterfactual multimodal utility prediction. Given an image-question query, LatentRouter extracts learned multimodal routing capsules, represents each candidate MLLM with a model capability token, and performs latent communication between these states to estimate how each model would perform if selected. A distributional outcome head predicts model-specific counterfactual quality, while a bounded capsule correction refines close decisions without allowing residual signals to dominate the prediction. The resulting utility-based policy supports performance-oriented and performance-cost routing, and handles changing candidate pools through shared per-model scoring with availability masking. Experiments on MMR-Bench and VL-RouterBench show that LatentRouter outperforms fixed-model, feature-level, and learned-router baselines. Additional analyses show that the gains are strongest on multimodal task groups where model choice depends on visual, layout-sensitive, or reasoning-oriented requirements, and that latent communication is the main contributor to the improvement. The code is available at: https://github.com/LabRAI/LatentRouter.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
