# YOLO-CAB: An Efficient Deep Learning-Based Underwater Object Detection Method for Autonomous Underwater Vehicles

## Metadata
- **Authors**: Runze Li, Changdong Yu, Shuaiyu Bao, Zijian Li, Jinyi Yao
- **Year**: 2026
- **Venue**: Mathematics
- **Topic**: AI for Communication Design
- **Keyword matched**: `deep learning physical layer design`
- **Semantic Scholar**: https://www.semanticscholar.org/paper/811ba7167f823f934e752175e617f7cff82d1e08
- **arXiv**: N/A
- **DOI**: 10.3390/math14111927
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: 2026-06-08

## Abstract
High-precision environmental perception is essential for deep-sea exploration and autonomous underwater vehicle operations. However, physical factors such as light scattering and selective absorption, along with high target–background similarity, cause existing detection methods to suffer from low recall and inaccurate localization on targets with blurred edges, low contrast, or category ambiguity. To address these challenges, we propose YOLO-CAB, a YOLOv13-based underwater object detector designed to handle these complex scenes by optimizing feature extraction, boundary perception, and the loss function. First, we introduce the Context-Aware Large Selective Kernel (CALSK) module into the shallow backbone layers to expand the receptive field and adaptively enhance spatial features via multi-scale depthwise convolutions. Furthermore, the Spatial Boundary Attention Module (SBAM) is applied before the feature pyramid enters the detection head to refine multi-scale features and enhance sensitivity to target boundaries. To address the variance in detection difficulty across categories, we also develop the Momentum-based Category-Aware Weighted Intersection over Union (MCAWIoU) loss. Consequently, the proposed weighting mechanism improves localization accuracy and confidence distribution for challenging samples. Evaluated on the RUOD benchmark dataset, YOLO-CAB improves mean average precision (mAP50) by 4.67%, the stricter localization metric (mAP50-95) by 3.0%, and F1 score by 3.7% over the vanilla YOLOv13n baseline. Ablation studies confirm the individual and synergistic contributions of these components. With 8.85 GFLOPs and an inference time of 5.21 ms under the tested hardware setting, YOLO-CAB improves detection accuracy while maintaining real-time inference.

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
