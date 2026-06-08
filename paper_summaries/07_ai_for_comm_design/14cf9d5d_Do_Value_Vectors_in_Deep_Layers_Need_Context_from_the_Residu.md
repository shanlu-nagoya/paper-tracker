# Do Value Vectors in Deep Layers Need Context from the Residual Stream?

## Metadata
- **Authors**: Muyu He, Yuchen Liu, Qing Huang, Li Zhang
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/14cf9d5d9dbb41e5bbcdc66e251fce51b17ab4e4
- **arXiv**: https://arxiv.org/abs/2606.02780
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
The success of the transformer architecture as the backbone of modern LLMs is in large part due to its use of attention layers. An attention layer follows the standard neural network paradigm: it takes the residual stream as input and thereby produces context-dependent query, key, and value vectors. However, we find that model performance meaningfully improves when deeper layers learn only a context-free value vector to preserve the original token information, without drawing on any context from the residual stream. When the model has access to this context-free value vector, adding back the context-dependent component provides little additional benefit for aggregate benchmark performance. Such context-free value vectors can be stored as sparse model parameters, eliminating the need to recompute or persistently cache these values. Through systematic ablations on the key design choices for such context-free value vectors, we propose Bank of Values (BoV), a new way of computing value vectors in attention by learning a lookup table of token-specific value vectors for each of the last third of layers. Across 135M and 780M models, BoV improves validation loss over standard attention and, at 780M, the average score across 21 benchmarks, matching the previous best method that adds token information to the value vector with less compute and memory.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
