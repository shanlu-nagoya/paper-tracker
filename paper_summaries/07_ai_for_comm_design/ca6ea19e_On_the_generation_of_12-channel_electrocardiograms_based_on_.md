# On the generation of 12-channel electrocardiograms based on a hybrid of diffusion and graph neural network models

## Metadata
- **Authors**: Evgeniy Schetinin, Anna V. Pestryakova, J. Shatalova, Andrey Andreevich Shevchuk
- **Year**: 2026
- **Venue**: VESTNIK OF ASTRAKHAN STATE TECHNICAL UNIVERSITY SERIES MANAGEMENT COMPUTER SCIENCE AND INFORMATICS
- **Topic**: AI for Communication Design
- **Keyword matched**: `neural network autoencoder communication`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/ca6ea19e498a5326cbafdbbcb99b1bb9b1e40122
- **arXiv**: N/A
- **DOI**: 10.24143/2072-9502-2026-2-15-22
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-05-04

## Abstract
A hybrid VAE-GNN-SSSD model is presented for generating physiologically correct 12-channel electro-cardiograms with a duration of 10 seconds. The proposed architecture combines three key components: a variational autoencoder for isolating the morphological components of P-QRS-T, a graph neural network with a partially fixed adjacency matrix to ensure compliance with the biophysical laws of Einthoven and Wilson, as well as a diffusion model with a structured state space for modeling long-term time dependencies. The model allows you to generate signals controlled by clinical parameters: type of arrhythmia, age, gender, and heart rate. Experimental results on the PTB-XL test sample showed FID = 0.052 and PRD = 10.8%, which is comparable with the results of modern methods. The key advantage of the model is its built–in biophysical correctness, confirmed by the MSE metric according to Einthoven's law (0.084). The practical effectiveness was confirmed in the MIT BIH classification of arrhythmias: augmentation with synthetic data increased Macro F1 from 0.84 to 0.89 (+6%), improved the recognition of rare ventricular and fuzed contractions by 5-7% and reduced the false omission of dangerous arrhythmias by 27%. The model has demonstrated good generalizing ability on independent ICU data (MIMIC-IV-ECG). The results open up prospects for the use of diagnostic systems for training, pathology simulation, creation of digital heart twins and training of medical specialists in solving the problem of shortage of annotated data and maintaining patient privacy.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
