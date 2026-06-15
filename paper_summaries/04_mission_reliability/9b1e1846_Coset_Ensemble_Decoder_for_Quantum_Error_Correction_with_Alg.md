# Coset Ensemble Decoder for Quantum Error Correction with Algorithm-Hardware Co-Design

## Metadata
- **Authors**: Shuang Liang, Jubo Xu, Giulio Bassanino, Qianzhou Wang, Yidong Zhou et al. (+6)
- **Year**: 2026
- **Venue**: 
- **Topic**: Mission Reliability
- **Keyword matched**: `ultra-reliable low-latency URLLC`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/9b1e184681782014fa0d12dfcea622ba59b75cb4
- **arXiv**: https://arxiv.org/abs/2606.11076
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-15

## Abstract
Reliable large-scale quantum computation relies on fault-tolerant architectures, where quantum error correction (QEC) continuously extracts and decodes error syndromes in real time. A critical component in QEC is the decoder, a classical subsystem that must simultaneously deliver high logical accuracy and ultra-low latency. This paper presents a novel algorithm-hardware co-design that improves the accuracy-latency trade-off over existing approaches such as vanilla Minimum-Weight Perfect Matching (MWPM) and Union-Find (UF) decoders. At the algorithmic level, we introduce coset ensemble decoding, which improves UF decoding by explicitly exploiting logically equivalent cosets. Our method performs ensemble forest exploration to generate multiple coset-consistent candidates and aggregates them to approximate coset-level maximum-likelihood decoding. We further reduce computational and memory complexity via reverse-order elimination and lossless graph compression, without sacrificing accuracy. At the hardware level, we design a domain-specific architecture that temporally reuses resources, avoiding the code-distance-proportional resource growth in prior spatial architectures. Several optimizations, such as multi-bank memory hashing and hierarchical ID mapping, are proposed to mitigate pipeline stalls and memory conflicts under highly concurrent access patterns. Under a circuit-level depolarizing noise model, our co-design approach achieves a better accuracy-latency trade-off than prior MWPM- and UF-based decoders, while reducing FPGA LUT consumption by up to 8.2 times compared with reported UF-based decoder resources. The tunable candidate number further exposes a flexible design knob, enabling users to tailor decoding performance to the requirements of different fault-tolerant workloads. Our implementation is publicly available at https://github.com/IMSeonL/coset-ensemble-decoder.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
