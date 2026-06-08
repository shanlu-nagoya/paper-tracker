# EpiFormer: Learning Antigen-Antibody Interactions for Epitope Prediction via Geometric Deep Learning

## Metadata
- **Authors**: Mansoor Ahmed, Huirong Chai, Haoxin Wang, Hemanth Venkateswara, Murray Patterson
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/9acec4c9f0a14ee3947797afaa842dfa5ec0e694
- **arXiv**: https://arxiv.org/abs/2606.04154
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
Antibodies neutralize foreign antigens by binding to specific surface regions called epitopes. Computational epitope prediction is critical for understanding immune recognition and guiding antibody engineering. However, existing methods face three fundamental challenges: antibody-aware models encode each chain independently and combine them only at a late stage, failing to capture co-dependent structural features that define binding interfaces, whereas severe class imbalance and scarcity of known antibody-antigen complexes render standard training objectives ineffective. We propose EpiFormer, a general encoder-decoder framework that addresses these challenges jointly. Our key design principle is interleaved cross-attention within GNN encoding layers, enabling bidirectional antigen-antibody information flow throughout representation learning rather than only at the output. This early-fusion principle is backbone-agnostic, providing consistent gains across GNN architectures from simple GCNs to equivariant models. We further show that sparsity-aware objectives are effective when paired with early-fusion architectures for the epitope prediction task. EpiFormer improves over the previous best method by over 40% in F1 score on standard benchmarks, demonstrating generalizability and cross-dataset transferability. Notably, EpiFormer discovers known biological principles as emergent behaviors of end-to-end training, where the learned cross-attention gates favor antigen-to-antibody information flow, consistent with the asymmetric roles of the two chains at the binding interface, and the model's preference for geometric over evolutionary features aligns with the established finding that epitope residues are not evolutionarily conserved. The source code is available at: https://github.com/mansoor181/epiformer.git

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
