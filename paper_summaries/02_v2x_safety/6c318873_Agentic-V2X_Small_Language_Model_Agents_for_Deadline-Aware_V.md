# Agentic-V2X: Small Language Model Agents for Deadline-Aware V2X Scheduling in 5G/6G Networks

## Metadata
- **Authors**: Gerasimos Papanikolaou-Ntais, A. Kaloxylos, Athanasios Kanavos
- **Year**: 2026
- **Venue**: 
- **Topic**: V2X Safety
- **Keyword matched**: `V2X safety communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/6c31887322317155717e7cc372428bde685b03e1
- **arXiv**: https://arxiv.org/abs/2607.04290
- **DOI**: N/A
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-07-13

## Abstract
Large Language Models (LLMs) are proposed as control interfaces for next-generation networks, but their latency, hallucinations, and lack of control guarantees make them unsuitable for near-real-time packet schedulers, especially in dynamic V2X environments. This paper introduces Agentic-V2X, an architecture where a small, locally deployed language model acts as a periodic non-real-time rApp-inspired policy creator, while a lightweight xApp-like controller executes validated policies at intervals suitable for scheduling. The framework targets deadline-aware 5G NR V2X scheduling with heterogeneous services (teleoperated driving, cooperative awareness, HD map sharing, and sensor sharing). Given a scenario summary, service objective, and telemetry, the LLM generates a structured policy containing service priorities, weight bounds, and safety constraints. A validator checks and repairs the policy before the controller enforces it via scheduler-weight adaptation in ns-3/ns3-ai. The evaluation compares proportional fair scheduling, static expert policies, a heuristic xApp, static LLM policies, and adaptive LLM-rApp policies over 126 completed runs. Metrics include deadline-constrained packet reception ratio, tail latency, deadline violations, throughput, fairness, policy validity, and safety interventions. Results show that the adaptive LLM-rApp/xApp design generates valid and executable policies and remains competitive at several operating points, including improved mean critical reliability over PF at the highest density. However, paired statistical analysis shows that the adaptive method is not the best aggregate method and remains below the strongest static policies overall. These results support Agentic-V2X as a safe, executable small-LLM policy-generation architecture rather than a universally dominant scheduler.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
