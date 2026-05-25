# Application-Oriented Evaluation of Federated Learning for IoT Intrusion Detection Under Non-IID Conditions in Wireless Sensor Networks

## Metadata
- **Authors**: W. Alayed, H. Tahir, Waqar Ul Hassan
- **Year**: 2026
- **Venue**: Applied Sciences
- **Topic**: Mission Reliability
- **Keyword matched**: `mission reliability wireless communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/8167d9f418b347bec4b7d264e68c74fc6e00f093
- **arXiv**: N/A
- **DOI**: 10.3390/app16105092
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-25

## Abstract
Federated learning is a distributed machine learning paradigm that enables multiple devices to collaboratively train a shared model while keeping their raw data localized. Federated learning has become an attractive solution for intrusion detection in Internet of Things (IoT)-based wireless sensor networks because it enables collaborative model training without transferring raw traffic data. However, real deployments rarely satisfy the common assumption that client data are independent and identically distributed (IID). In practical wireless sensor networks, data heterogeneity naturally arises from spatial variation, uneven attack exposure, traffic imbalance, and differences in sensing conditions, which can substantially affect detection reliability and deployment feasibility. This study presents an application-oriented evaluation of federated intrusion detection under controlled non-IID conditions using three representative datasets: WSN-DS, CIC-IDS-2017, and UNSW-NB15. An LSTM-based intrusion detection model is trained in a federated setting and assessed using three aggregation strategies, namely, FedAvg, FedProx, and SCAFFOLD, under label skew, quantity skew, and feature skew scenarios. The results show that standard FedAvg degrades markedly as heterogeneity increases, with accuracy reductions of up to 23.4 percentage points and substantially higher communication cost under extreme non-IID settings. In contrast, FedProx and SCAFFOLD improve convergence stability and reduce the impact of client drift, with SCAFFOLD showing the strongest overall robustness and up to 45% lower communication cost than FedAvg due to faster convergence. These results demonstrate that non-IID awareness is essential for building deployable privacy-preserving intrusion detection systems for resource-constrained IoT environments. The study provides practical guidance for selecting federated aggregation strategies in wireless sensor network security applications where robustness, bandwidth efficiency, and real-world data heterogeneity must be jointly considered.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
