# SAC-BBR: A Semantic-Aware and Cross-Layer Collaborative Congestion Control Mechanism for Heterogeneous Campus Networks

## Metadata
- **Authors**: Zhaolu Li, Ning Xu, Xiaoli Zhang
- **Year**: 2026
- **Venue**: Applied Sciences
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/6029eec0778cf3d985be7f06915d3491261a7f75
- **arXiv**: N/A
- **DOI**: 10.3390/app16115587
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
With the widespread adoption of Wi-Fi 7 in campus networks, high-density access and large-scale research data transmission challenge traditional congestion control algorithms. TCP-bottleneck bandwidth and round-trip propagation time (BBR) lacks deep link awareness and service semantic breadth, leading to misinterpreting non-congestive packet loss and inter-flow unfairness in complex wireless scenarios. To address this, this paper proposes semantic-aware and cross-layer collaborative optimized BBR (SAC-BBR), a semantic-aware cross-layer optimization mechanism for high-density heterogeneous campus networks. It leverages an Extended Berkeley Packet Filter (eBPF) to capture physical link characteristics in real time within the Linux kernel, accurately distinguishing random loss from congestion loss. It then constructs a lightweight semantic identification engine to classify traffic and establish a service satisfaction utility model. Finally, a deep reinforcement learning-based dynamic gain regulator maps cross-layer states and service priorities to the action space, enabling millisecond-level intelligent tuning of pacing_gain and cwnd_gain. Experimental results show that SAC-BBR improves throughput by over 22% compared to BBRv3 and reduces average round-trip time (RTT) by 17% while suppressing RTT jitter by over 60% in high-density scenarios. Furthermore, it enhances the Jain fairness index to 0.93 under multi-protocol competition, ensuring high-performance and equitable transmission.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
