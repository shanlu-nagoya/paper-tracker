# Goal-Oriented Semantic Communication for Distributed ISAC-Enabled Vehicle Coordination

## Metadata
- **Authors**: Wenjie Liu, Yansha Deng
- **Year**: 2026
- **Venue**: 
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `semantic communication goal-oriented`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/67309817a139da3f7c799bbfe1d7aefbc37dc187
- **arXiv**: https://arxiv.org/abs/2607.15111
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-07-20

## Abstract
Vehicle coordination at unsignalized intersections relies on accurate real-time vehicle state acquisition and reliable command-and-control (C&C) signal delivery. However, existing studies typically treat sensing, communication, and control separately, which may lead to redundant transmissions, outdated state information, and unreliable vehicle coordination. In this paper, we investigate a new scenario of distributed integrated sensing and communication (ISAC)-enabled vehicle coordination at intersections, where multiple roadside units (RSUs) collaboratively transmit sensing signals for vehicle state acquisition and C&C signals for vehicle movement control under the management of a central base station (BS). To improve signaling efficiency, we propose a unified goal-oriented semantic communication (GSC) framework, which transmits sensing and C&C signals only when they are semantically important for improving intersection traffic throughput. Specifically, an extended Kalman filter (EKF) is adopted to predict vehicle states and fuse distributed sensing measurements. A masked hybrid proximal policy optimization (MHPPO) framework is then developed to jointly determine sensing transmission decisions, C&C transmission decisions, and C&C signal contents based on a value-of-information (VoI) reward. Furthermore, we propose an uncertainty-aware transmission design (UTD), including robust beamforming and VoI-based time-division power allocation, to improve sensing and communication reliability under vehicle state uncertainty and inter-RSU interference. Simulation results show that our proposed framework achieves 100% collision-free vehicle coordination with significantly reduced signaling overhead compared with predictive ISAC baselines adapted from state-of-the-art related studies and several ablation baselines.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
