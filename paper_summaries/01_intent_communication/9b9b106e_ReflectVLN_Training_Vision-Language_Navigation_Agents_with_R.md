# ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning

## Metadata
- **Authors**: Jiahang Wang, Yirong Yang, Yanqing Zhu, Minghua Luo, Shichao Xie et al. (+2)
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `semantic communication goal-oriented`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/9b9b106e2b5ca51c68edc7a196b4a966d5fe6a3e
- **arXiv**: https://arxiv.org/abs/2607.12680
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-07-20

## Abstract
Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent performs subtask decomposition and reflection, generating executable subtask descriptions as corrective plans. Conditioned on these descriptions, the execution agent grounds them into short-horizon actions under current observations while monitoring sub-goal progress and detecting off-track behavior. Crucially, ReflectVLN enables closed-loop bidirectional communication: the execution agent emits progress and deviation signals to trigger reflection and subtask updates on demand, and the intention agent returns structured guidance that reconditions subsequent actions for recovery. To encourage temporally coherent decisions with interpretable intermediate rationales, we introduce Action Chain-of-Thought (Action-CoT), a path-conditioned dual-query training scheme for action generation. Experiments on standard VLN benchmarks show that ReflectVLN improves success rates and path efficiency under a constrained data budget, with favorable training cost and fewer high-level intention calls at inference time, while providing interpretable intermediate decisions for analysis and collaboration. Code is available at: https://github.com/AIprogrammer/ReflectVLN

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
