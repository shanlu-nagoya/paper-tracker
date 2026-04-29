# Hierarchical Semantic Transmission and Lyapunov-Optimized Online Scheduling for the Internet of Vehicles

## Metadata
- **Authors**: Le Jiang, Yani Guo, Wenzhao Zhang, Penghao Wang, Shujun Han
- **Year**: 2026
- **Venue**: Italian National Conference on Sensors
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/f76dc900d2f33403abf0222b19519a6c21e62477
- **arXiv**: N/A
- **DOI**: 10.3390/s26092606
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-04-29

## Abstract
The inherent redundancy in vehicle sensor data, coupled with constrained onboard resources and stringent latency requirements, renders traditional bit-oriented transmission paradigms inefficient for autonomous-driving perception tasks. Semantic communication offers a promising direction by shifting the focus from bit-level fidelity to task-level information delivery. In this paper, we propose a unified framework that integrates hierarchical transmission and online scheduling for Internet of Vehicles (IoV)-oriented collaborative perception. The proposed hierarchy separates information into two complementary layers: a coarse metadata layer (object bounding boxes) for latency-critical awareness, and fine-grained visual semantics (multi-scale region-of-interest (ROI) patches) for perception-intensive tasks. We formulate an online scheduling problem that jointly exploits Age of Information (AoI) and Channel State Information (CSI) to dynamically decide what to transmit and at what fidelity under per-frame budget constraints. To address cross-scheme fairness, we report resource utilization under a fixed kbps/fps physical budget and evaluate robustness using a combination of a lightweight task-proxy metric and COCO-style Average Recall (AR100) under ROI-only evaluation. The hierarchical transmission architecture, combined with AoI awareness, reduces global semantic staleness by approximately 78%. The Lyapunov-based online scheduler enables intelligent, signal-to-noise ratio (SNR)-adaptive switching between coarse and fine semantic levels, ensuring robust perception under varying channel quality. Under strict physical-budget constraints and unreliable channel conditions, joint source-channel coding (JSCC) exhibits significantly stronger task robustness than conventional schemes: at 0 dB SNR, the task-proxy detection rate improves by nearly 47 percentage points over the uncoded baseline.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
