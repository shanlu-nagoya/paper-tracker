# AUGUSTE: Online-Learning dApp for Predictive URLLC Scheduling

## Metadata
- **Authors**: M. Elkael, Michele Polese, Yunseong Lee, Koichiro Furueda, Tommaso Melodia
- **Year**: 2026
- **Venue**: 
- **Topic**: Mission Reliability
- **Keyword matched**: `ultra-reliable low-latency URLLC`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/351241da2ba2d6106acd82e94f19c71976c9783b
- **arXiv**: https://arxiv.org/abs/2606.03664
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
Ultra Reliable and Low Latency Communications (URLLC) was one of the main motivations behind 5G, with 3GPP advertising 1-10 ms latency targets for applications such as industrial automation, Vehicle-To-Everything (V2X), tactical edge networking, and unmanned-system control. Years on, real 5G Time Division Duplexing (TDD) networks still show median Uplink (UL) round-trip times in the 50-70 ms range, largely because of the Scheduling Request (SR) procedure that a User Equipment (UE) must complete before transmitting UL data. Existing remedies, primarily Configured Grant (CG) scheduling, only eliminate this overhead for strictly periodic traffic and require cross-layer synchronization, which has limited their adoption. We propose AUGUSTE (Anticipatory Uplink Grants for URLLC via Self-Adapting Temporal Estimation), a learning-based Medium Access Control (MAC) scheduling framework that embeds online Machine Learning (ML) models in the UL scheduler to predict packet arrivals and proactively allocate resources before an SR is issued. An adaptive state machine alternates between a learning phase that collects unbiased arrival statistics and a confident phase that exploits the learned predictions to schedule only when traffic is expected. We evaluate AUGUSTE on a real 5G testbed running OpenAirInterface across three URLLC traffic patterns (request-response, ML edge inference, and periodic autonomous reporting), and show that it operates at the best achievable point on the latency-overhead trade-off: it matches always-on scheduling's median Round Trip Time (RTT) (around 10 ms, halving the 20 ms SR-based baseline) at roughly one-tenth its resource cost (7-10 percent overhead).

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
