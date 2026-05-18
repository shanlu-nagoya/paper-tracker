# Spatial–Temporal EEG Imaging for Dual-Loop Neuro-Adaptive Simulation: Cognitive-State Decoding and Communication Gating in Critical Human–Machine Teams

## Metadata
- **Authors**: Rubén Juárez, Antonio Hernández-Fernández, Claudia de Barros Camargo, D. Molero
- **Year**: 2026
- **Venue**: Journal of Imaging
- **Topic**: Intent-Aware Communication
- **Keyword matched**: `task-oriented communication wireless`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/1ed093a8dd4669ff53fa897439254ffac7dc85e8
- **arXiv**: N/A
- **DOI**: 10.3390/jimaging12050208
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-18

## Abstract
Human performance in critical environments is frequently degraded by mistimed communication delivered during periods of visual–cognitive saturation. In such settings, failures arise not only from individual limitations but also from poor coordination between operators under rapidly changing workload conditions. We present a dual-loop neuro-adaptive simulation framework based on real-time spectral–topographic EEG representations, in which multichannel cortical activity is transformed into dynamic spatial maps and decoded to regulate both operator assistance and team communication. The system integrates 14-channel wireless EEG (Emotiv EPOC X, 256 Hz), gaze tracking, telemetry, and communication events through an LSL-based multimodal synchronization pipeline. A hybrid CNN–LSTM model processes sequences of spectral-topographic EEG maps to classify three operationally actionable neurocognitive states—Channelized Attention, Diverted Attention, and Surprise/Startle—while also estimating a continuous Cognitive Load Index (CLI). These representation-derived features are then used by a multi-agent proximal policy optimization (MAPPO) controller to generate two coordinated outputs: (i) adaptive haptic guidance for the pilot, designed to reduce reliance on overloaded visual and auditory channels, and (ii) a traffic-light communication gate for the telemetry engineer, regulating whether radio intervention should proceed, be delayed, or be withheld. In a high-fidelity dual-station simulation with 25 pilot–engineer pairs, the proposed framework was associated with a reduction of more than 30% in communication breakdown errors relative to open-loop telemetry, with the strongest effects observed during peak-load windows, while preserving realistic task progression. It also improved pilot reaction time to time-critical warnings and reduced engineer decision load under the tested conditions. These findings support the use of spectral-topographic EEG representations as a practical basis for combining multimodal neurophysiological sensing, spatiotemporal pattern decoding, and adaptive coordination in high-pressure human–machine teams. At the same time, the study should be interpreted as evidence of controlled feasibility in a simulated setting rather than as definitive proof of field-level generalization. We further discuss deployment constraints and propose privacy-by-design safeguards to ensure that neurocognitive signals are used exclusively for operational adaptation rather than employability assessment or performance scoring.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
