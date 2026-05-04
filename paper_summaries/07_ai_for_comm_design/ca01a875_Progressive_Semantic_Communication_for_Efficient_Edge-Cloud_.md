# Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models

## Metadata
- **Authors**: C. Hsu, Wig Yuan-Cheng Cheng, C. Papagianni
- **Year**: 2026
- **Venue**: 
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/ca01a87540bdb50a8fc69c29b8578585f7599112
- **arXiv**: https://arxiv.org/abs/2604.26508
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms. Conversely, fully offloading inference to the cloud is often impractical in bandwidth-limited environments, where transmitting raw visual data introduces substantial latency overhead. While recent edge-cloud collaborative architectures attempt to partition VLM workloads across devices, they typically rely on transmitting fixed-size representations, lacking adaptability to dynamic network conditions and failing to fully exploit semantic redundancy. In this paper, we propose a progressive semantic communication framework for edge-cloud VLM inference, using a Meta AutoEncoder that compresses visual tokens into adaptive, progressively refinable representations, enabling plug-and-play deployment with off-the-shelf VLMs without additional fine-tuning. This design allows flexible transmission at different information levels, providing a controllable trade-off between communication cost and semantic fidelity. We implement a full end-to-end edge-cloud system comprising an embedded NXP i.MX95 platform and a GPU server, communicating over bandwidth-constrained networks. Experimental results show that, at 1 Mbps uplink, the proposed progressive scheme significantly reduces network latency compared to full-edge and full-cloud solutions, while maintaining high semantic consistency even under high compression. The implementation code will be released upon publication at https://github.com/open-ep/ProSemComVLM.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
