# SwiftSNNI: Optimized Scheduling for Secure Neural Network Inference (SNNI) on Multi-Core Systems

## Metadata
- **Authors**: Kanwal Batool, S. Anwar, Francesco Regazzoni, Andy D. Pimentel, Zoltán Ádám Mann
- **Year**: 2026
- **Venue**: Proceedings of the 17th ACM/SPEC International Conference on Performance Engineering
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/4778ec98424d47a1a646166d96fd0ad22d5bccdf
- **arXiv**: N/A
- **DOI**: 10.1145/3777884.3797005
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
Secure Neural Network Inference (SNNI) enables privacy-preserving inference on encrypted data with strong cryptographic guarantees. However, practical deployments suffer from high preprocessing overhead, significant communication costs, and sequential execution. These limitations lead to low throughput, underutilized system resources, long queueing delays, and poor scalability. This work introduces SwiftSNNI, a unified, resource-aware scheduling framework for SNNI. It implements a hybrid offline–online strategy that orchestrates offline preprocessing (Tpre,i) and online inference (Ton,i) jobs to maximize parallelism. By formulating SNNI scheduling as a constrained optimization problem, SwiftSNNI overlaps Tpre,i phase execution of future requests with active Ton,j, jobs. SwiftSNNI also incorporates optional advance notices to enable proactive Tpre,i, which further reduces average input delay (D). Evaluations using five benchmark neural networks (M1, M2, HiNet, AlexNet, VGG-16) under diverse workloads and stochastic arrival rates confirm substantial performance gains. Compared to a parallelized sequential baseline (MS-SHARK), SwiftSNNI achieves up to 97% lower average input delay (D), a 81% reduction in makespan (≈ 5.4 × speedup), and delivers 5.6 × increase in throughput. Furthermore, SwiftSNNI reduces average waiting time (W) by over 99%, demonstrating robust starvation prevention for high-concurrency workloads. SwiftSNNI supports concurrent execution, scales to larger neural networks, and provides an efficient runtime for SNNI deployments. The SwiftSNNI implementation is available online.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
