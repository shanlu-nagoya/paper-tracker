# RoPeerTo: A Datacenter-Scale Architecture for Peer-To-Peer DMA between GPUs and FPGAs

## Metadata
- **Authors**: Marco Venere, Giuseppe Sorrentino, Benjamin Ramhorst, M. J. Heer, L. Petrica et al. (+5)
- **Year**: 2026
- **Venue**: Proceedings of the 21st European Conference on Computer Systems
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/e2eca037afd69c3b97b268e2ff4a1473a701af4f
- **arXiv**: N/A
- **DOI**: 10.1145/3767295.3803620
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-04-29

## Abstract
Modern datacenters integrate heterogeneous accelerators, such as GPUs and FPGAs, to speed up different stages of compute-intensive pipelines. GPUs are best suited for massively parallel workloads (e.g., deep learning), while FPGAs excel at task-level parallelism, stream-oriented processing, and in-network acceleration. Since these architectures must exchange data efficiently, literature introduced Peer-To-Peer (P2P) communication across PCI Express (PCIe) devices, to reduce CPU-driven orchestration and avoid intermediate, redundant buffer copies that degrade performance. However, current solutions are either closed-source or tied to proprietary frameworks, limiting P2P communication across most PCIe-based devices and requiring significant technical effort to enable P2P capabilities on supported hardware. For this reason, we propose RoPeerTo, a fully open-source, datacenter-scale architecture for P2P DMA communication over PCIe, validated on both GPUs and FPGAs. The goal is to provide a general, open alternative that ensures flexibility, efficiency, and usability. To this end, we design a complete HW/SW stack operating across different layers, supporting standard protocols for DMA-based memory sharing, advanced tools for device virtualization, memory address translation, and access protection. The result is a unified framework exposing a high-level API to end users, that enables direct communication between accelerators such as FPGAs and GPUs, and abstracts away the underlying hardware setup and management. We validate the system across different scenarios. First, we isolate the communication layer, observing a 5.61× speedup and a 37.99% reduction in GPU power consumption during data transfer. Next, we leverage the system for a compute-intensive workload where communication is only a partial bottleneck, achieving a 6.77% speedup without any compute-side modifications. Finally, we evaluate communication-heavy distributed computing workloads, demonstrating up to a 21.79× speedup in network-bound data scattering.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
