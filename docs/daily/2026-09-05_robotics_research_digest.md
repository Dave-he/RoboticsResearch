# 机器人研究每日摘要 · 2026-09-05

> 自动生成,共 16 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (2 篇)

### 1. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 2. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (3 篇)

### 1. SmoothRL: Online Reinforcement Learning During Asynchronous Execution

- **arXiv**: [2608.29768v1](https://arxiv.org/abs/2608.29768v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29768v1)
- **作者**: Guang Gao, Yuxuan Nong, Baifu Huang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learn…

### 2. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 3. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

## 🦵 人形 / 足式机器人 (1 篇)

### 1. CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning

- **arXiv**: [2607.29172v1](https://arxiv.org/abs/2607.29172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.29172v1)
- **作者**: Yuxin Chen, Hari Srikanth, Nathan Jew et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: While robot foundation models are growing increasingly capable, the strongest models are typically trained on proprietary data and remain closed-source, limiting downstream users' ability to adapt them to new tasks, embodiments, and deployment settings. Following the LLM community, an emerging access paradigm for closed-weight robot foundation models is the…

## 🦾 操控 / 灵巧手 / 抓取 (4 篇)

### 1. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 2. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 3. Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

- **arXiv**: [2609.01596v1](https://arxiv.org/abs/2609.01596v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01596v1)
- **作者**: Haoyuan Deng, Haichao Liu, Wenkai Guo et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Real-world robotic assembly at sub-millimeter tolerances demands spatial precision, compliant interaction, and robustness to contact failures. We present Facet-0, a robotic foundation model that predicts and values the contact consequences of its actions. Facet-0 unifies multimodal representation learning and reinforcement learning (RL) post-training around…

### 4. Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots

- **arXiv**: [2608.22035v1](https://arxiv.org/abs/2608.22035v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.22035v1)
- **作者**: Wooseong Chung, William Cong, Jakub Dworakowski et al.
- **发表**: 2026-08-22  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\script…

## 🎓 模仿学习 / 强化学习 (5 篇)

### 1. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 2. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 3. ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM

- **arXiv**: [2512.14032v1](https://arxiv.org/abs/2512.14032v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2512.14032v1)
- **作者**: Ignacio Alzugaray, Marwan Taher, Andrew J. Davison
- **发表**: 2025-12-16  ·  **类别**: cs.CV, cs.AI, eess.IV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image feature…

### 4. MISO: Multiresolution Submap Optimization for Efficient Globally Consistent Neural Implicit Reconstruction

- **arXiv**: [2504.19104v1](https://arxiv.org/abs/2504.19104v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2504.19104v1)
- **作者**: Yulun Tian, Hanwen Cao, Sunghwan Kim et al.
- **发表**: 2025-04-27  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Neural implicit representations have had a significant impact on simultaneous localization and mapping (SLAM) by enabling robots to build continuous, differentiable, and high-fidelity 3D maps from sensor data. However, as the scale and complexity of the environment increase, neural SLAM approaches face renewed challenges in the back-end optimization process…

### 5. NeRF and Gaussian Splatting SLAM in the Wild

- **arXiv**: [2412.03263v1](https://arxiv.org/abs/2412.03263v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.03263v1)
- **作者**: Fabian Schmidt, Markus Enzweiler, Abhinav Valada
- **发表**: 2024-12-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Navigating outdoor environments with visual Simultaneous Localization and Mapping (SLAM) systems poses significant challenges due to dynamic scenes, lighting variations, and seasonal changes, requiring robust solutions. While traditional SLAM methods struggle with adaptability, deep learning-based approaches and emerging neural radiance fields as well as Ga…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (1 篇)

### 1. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [$τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885v1) — score 14
2. [MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation](https://arxiv.org/abs/2607.17970v1) — score 13
3. [SmoothRL: Online Reinforcement Learning During Asynchronous Execution](https://arxiv.org/abs/2608.29768v1) — score 9

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
