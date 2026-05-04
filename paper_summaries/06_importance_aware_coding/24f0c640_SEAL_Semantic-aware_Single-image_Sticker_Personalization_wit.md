# SEAL: Semantic-aware Single-image Sticker Personalization with a Large-scale Sticker-tag Dataset

## Metadata
- **Authors**: Changhyun Roh, Yonghyun Jeong, Jonghyun Lee, Chanho Eom, Jihyong Oh
- **Year**: 2026
- **Venue**: 
- **Topic**: Importance-Aware Coding
- **Keyword matched**: `importance-aware channel coding`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/24f0c640daf41ea01f2a1982457611c428ca1e89
- **arXiv**: https://arxiv.org/abs/2604.26883
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
Synthesizing a target concept from a single reference image is challenging in diffusion-based personalized text-to-image generation, particularly for sticker personalization where prompts often require explicit attribute edits. With only one reference, test-time fine-tuning (TTF) methods tend to overfit, producing \textit{visual entanglement}, where background artifacts are absorbed into the learned concept, and \textit{structural rigidity}, where the model memorizes reference-specific spatial configurations and loses contextual controllability. To address these issues, we introduce \textbf{SE}mantic-aware single-image sticker person\textbf{AL}ization (\textbf{SEAL}), a plug-and-play, architecture-agnostic adaptation module that integrates into existing personalization pipelines without modifying their U-Net-based diffusion backbones. SEAL applies three components during embedding adaptation: (1) a Semantic-guided Spatial Attention Loss, (2) a Split-merge Token Strategy, and (3) Structure-aware Layer Restriction. To support sticker-domain personalization with attribute-level control, we present StickerBench, a large-scale sticker image dataset with structured tags under a six-attribute schema (Appearance, Emotion, Action, Camera Composition, Style, Background). These annotations provide a consistent interface for varying context while keeping target identity fixed, enabling systematic evaluation of identity disentanglement and contextual controllability. Experiments show that SEAL consistently improves identity preservation while maintaining contextual controllability, highlighting the importance of explicit spatial and structural constraints during test-time adaptation. The code, StickerBench, and project page will be publicly released.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
