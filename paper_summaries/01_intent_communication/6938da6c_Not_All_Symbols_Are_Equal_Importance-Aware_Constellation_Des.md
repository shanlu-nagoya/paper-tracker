# Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication

## Metadata
- **Authors**: Albert Shaju, C. Thomas, M. R. Chowdhury
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/6938da6c19afe7c56886bdbecc6df2195104c662
- **arXiv**: https://arxiv.org/abs/2605.14940
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-18

## Abstract
Semantic communication systems for goal-oriented transmission must protect task-relevant information not only through source compression but also via physical layer mapping. Existing approaches decouple constellation design and semantic encoding, exposing critical symbols to channel errors at the same rate as irrelevant ones. Contrary to this, in this paper, a joint semantic-physical layer framework is proposed, which is composed of a vector quantized-variational autoencoder that extracts discrete latent concepts, a semantic criticality indicator (SCI) that scores each concept by task relevance, and a deep reinforcement learning agent that dynamically selects the transmission subset based on instantaneous channel conditions. At the physical layer, a learned semantic-aware M -QAM constellation assigns symbol positions according to joint co-occurrence statistics and SCI scores, departing from the uniform spacing and Gray coding of standard M -QAM which minimizes average BER without regard for semantic content. We introduce a novel semantic symbol vulnerability (SSV) metric and a semantic protection probability (SPP) to quantify the exposure of task-critical symbols to decoding errors, and prove that any Gray-coded constellation is strictly suboptimal in SCI-Weighted SSV whenever the source exhibits non-uniform semantic importance and co-occurrence statistics. Simulation results demonstrate that the proposed constellation achieves near 100% SPP across modulation orders from 4-QAM to 1024-QAM versus 50% for standard constellations at high spectral efficiency, a 21:1 compression ratio with semantic quality above 0.9, generalizing across MNIST, Fashion-MNIST, and FSDD without modification.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
