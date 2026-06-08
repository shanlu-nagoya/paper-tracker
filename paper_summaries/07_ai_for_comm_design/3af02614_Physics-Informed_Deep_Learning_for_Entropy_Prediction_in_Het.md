# Physics-Informed Deep Learning for Entropy Prediction in Heterogeneous Systems: Thermodynamic and Information-Theoretic Case Studies

## Metadata
- **Authors**: Biswajeet Sahoo, Debadutta Patra
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/3af026147692bda967c0befc4a1c95cc9836bf48
- **arXiv**: https://arxiv.org/abs/2606.01179
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
Entropy production governs irreversibility and uncertainty in both physical and information-theoretic systems. While Physics-Informed Neural Networks (PINNs) successfully solve differential equations, current architectures remain inherently domain-specific. The extraction of domain-invariant entropy representations across fundamentally different physical laws remains unexplored. This paper introduces a unified Physics-Informed Deep Learning (PIDL) framework that simultaneously enforces differential equation residuals and information-theoretic bounds within a single neural architecture. We demonstrate this framework via two canonical studies: (i) a thermodynamic continuous stirred-tank reactor (CSTR) model solving governing ODEs, where a Softplus constraint strictly enforces the Second Law of Thermodynamics; and (ii) an information-theoretic financial market model solving the inverse Fokker-Planck PDE to infer latent drift and diffusion coefficients, guaranteeing diffusion positivity via a Softplus constraint while naturally inducing Shannon entropy. Three model variants are evaluated: two domain-specific baselines and one shared-encoder architecture. The PIDL framework guarantees absolute thermodynamic admissibility with zero Second-Law violations and exhibits exceptional data efficiency, retaining>90% predictive accuracy using merely 30% of available training data. Furthermore, a post-hoc Ruppeiner Riemannian geometric analysis of the learned entropy surface successfully identifies thermodynamic phase instabilities. This methodology provides a robust, domain-agnostic architecture for physics-constrained entropy modeling, advancing applications in sustainable process design and quantitative financial risk assessment.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
