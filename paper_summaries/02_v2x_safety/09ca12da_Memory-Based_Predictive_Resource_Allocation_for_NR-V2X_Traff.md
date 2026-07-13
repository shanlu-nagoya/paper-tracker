# Memory-Based Predictive Resource Allocation for NR-V2X Traffic

## Metadata
- **Authors**: Nurgüneş Yordanov, B. Cavusoglu
- **Year**: 2026
- **Venue**: Electronics
- **Topic**: V2X Safety
- **Keyword matched**: `V2X safety communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/09ca12da69700bd2760f2f7dbd87128e3b394413
- **arXiv**: N/A
- **DOI**: 10.3390/electronics15142995
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-07-13

## Abstract
New Radio Vehicle-to-Everything (NR-V2X) safety scheduling is difficult because burst episodes increase urgent arrivals, lower transmission success, and create retransmissions that compete for future slots. A scheduler that waits for the visible queue can react late, whereas always reserving extra safety physical resource blocks (PRBs) consumes the best-effort (BE) capacity after the stress has passed. This study proposes Memory-Based Predictive Allocation (MPA), a finite-action PRB allocation rule for safety and BE coexistence. MPA combines the deadline queue and retry state with a decayed transient-deficit memory, online success calibration, and a recoverability-aware BE cost guard. At each slot, it tests feasible safety PRB increments and chooses the action that first limits urgent safety loss, then reduces next-slot carryover, and finally avoids unnecessary PRB use. The model uses an NR-V2X resource pool interpretation and a calibrated signal-to-interference-plus-noise-ratio (SINR)-to-success mapping with hybrid automatic repeat request (HARQ)-like combining. Monte Carlo results show that MPA lowers safety misses relative to queue-reactive scheduling while preserving more BE throughput than a maximum safety reservation. In dense non-line-of-sight (NLOS) stress, MPA keeps the 95th-percentile (p95) delivered packet delay within the three-millisecond budget and preserves 0.892 normalized BE throughput, versus 0.534 under fixed maximum reservation.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
