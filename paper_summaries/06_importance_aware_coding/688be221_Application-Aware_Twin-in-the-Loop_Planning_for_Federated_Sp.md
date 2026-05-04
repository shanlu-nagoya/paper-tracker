# Application-Aware Twin-in-the-Loop Planning for Federated Split Learning over Wireless Edge Networks

## Metadata
- **Authors**: Zihao Ding, Beining Wu, Jun Huang, Shiwen Mao
- **Year**: 2026
- **Venue**: 
- **Topic**: Importance-Aware Coding
- **Keyword matched**: `significance-aware wireless transmission`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/688be2215028c1363be634b79686f5ed9598f6e1
- **arXiv**: https://arxiv.org/abs/2604.26105
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
We investigate task-success-oriented resource allocation for federated split learning (FSL) at the wireless edge. In this setting, the server must jointly determine bandwidth, transmit power, split-layer placement, compression level, and terminal participation under per-round deadline, memory, and spectrum constraints. These coupled decisions affect wireless transmission, model training, and task execution, which evolve at different time scales and cannot be efficiently evaluated through repeated real-world trials. To address this challenge, we propose TiLP, a twin-in-the-loop planner that evaluates candidate decisions through a cross-domain digital twin before execution. The twin integrates network, training, and task sub-twins, with each sub-twin calibrated at the time scale of the process it models. Based on this twin, TiLP performs receding-horizon cross-entropy method planning with actor-critic guidance to search over mixed continuous-discrete decisions. Experiments on LIBERO robotic manipulation tasks over a Sionna RT-simulated wireless network show that TiLP improves task success by 9.5 percentage points over the strongest single-axis baseline, while satisfying the per-round deadline and energy budget.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
