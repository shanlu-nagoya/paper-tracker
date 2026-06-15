# Deep learning assisted modeling of Li-ion transport in SEI: a graph neural network based study

## Metadata
- **Authors**: A. S. Kulathuvayal, Yanqing Su
- **Year**: 2026
- **Venue**: Frontiers in Batteries and Electrochemistry
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/7297089c6328a4e9528ed1a22853e7d5b8f63720
- **arXiv**: N/A
- **DOI**: 10.3389/fbael.2026.1849012
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-15

## Abstract
Understanding Li-ion transport through the solid electrolyte interphase (SEI) is essential for improving the stability of lithium-metal batteries, as nonuniform ionic transport through the inorganic SEI can promote spatially localized Li deposition and dendrite formation. In this work, we develop a deep-learning-assisted framework to model Li-ion transport across the inorganic SEI by combining density functional theory (nudged elastic band) calculations with graph neural network learning. A systematic diffusion dataset was first generated for eight major inorganic SEI compo-nents, namely, LiF, LiCl, LiBr, LiI, Li2O, Li2S, Li3N, and Li2CO3, covering both bulk (grain) diffusion and grain-boundary diffusion over representative low-energy surfaces and interfaces. This dataset includes homogeneous and heterogeneous interfaces (in-terfaces), providing a unified design space for Li-ion migration in SEI environments. A path-aware graph variational autoencoder (GVAE) was then used to learn latent representations of NEB trajectories, and the learned embeddings were incorporated one into a predictive GNN model for minimum-energy-path and migration-barrier estimation. The combined GVAE-GNN framework achieved strong predictive performance for both grain and grain-boundary diffusion, with test-set R2 values of 0.93 and 0.94, respectively. Feature-importance and latent-space analyses further show that migration behavior is governed not only by composition, but also by local structural factors such as exposed surface, saddle-point character, and grain-boundary energetics. The results reveal clear transport trends across SEI chemistries, with halide-rich systems generally associated with narrower low-barrier distributions, while Li3N, Li2CO3, and structurally mismatched heterogeneous interfaces exhibit broader and higher-barrier landscapes. This study give a physics-informed machine-learning framework for Mapping and predicting Li-ion migration in complex SEI structures and provides insight into how SEI chemistry and microstructure jointly control interfacial ion transport.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
