# A Two-Phase Optimization Framework for UAV Communication in Pickup-and-Delivery Missions

## Metadata
- **Authors**: Jun-Pyo Hong
- **Year**: 2026
- **Venue**: Electronics
- **Topic**: Mission Reliability
- **Keyword matched**: `mission reliability wireless communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/e9fd9fbc5f7faaf7621dfd2ed75ca62013653462
- **arXiv**: N/A
- **DOI**: 10.3390/electronics15102166
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-25

## Abstract
Unmanned aerial vehicles (UAVs) are increasingly employed for parcel logistics while simultaneously serving as aerial communication platforms. However, jointly optimizing pickup-and-delivery operations and wireless communication raises a large-scale mixed-integer nonlinear programming problem due to the coupling of binary logistics decisions, trajectory planning, time allocation, user scheduling, and transmit-power control. This paper proposes a two-phase optimization framework that enables a dual-purpose UAV mission by jointly considering parcel pickup-and-delivery and downlink communication within a single framework. The key strength of the proposed approach is that it separates the logistics-dominated delivery stage from the communication-oriented service stage, thereby reducing the difficulty of directly handling the highly coupled MINLP while exploiting the residual mission time for communication enhancement. In Phase 1, a pickup-and-delivery optimization problem is formulated to minimize the delivery completion time by determining the UAV trajectory, time-slot lengths, and item handling sequence, where the binary pickup/drop-off decisions are relaxed and progressively enforced through a penalty convex–concave procedure. In Phase 2, communication performance is enhanced by optimizing user scheduling and transmit power over the entire mission horizon, together with residual flight trajectory refinement after delivery completion using successive convex approximation and block coordinate descent. Simulation results show that the proposed algorithm substantially improves the minimum average spectral efficiency among ground nodes while achieving early completion of logistics tasks. Compared with baseline strategies, the proposed method delivers consistent performance gains under various system parameters. In particular, it improves the minimum average spectral efficiency by up to 15% compared with the baseline that removes the proposed post-delivery trajectory refinement, demonstrating the benefit of exploiting the residual flight trajectory for communication enhancement after delivery completion.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
