# 机器人研究每日摘要 · 2026-08-05

> 自动生成,共 93 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (7 篇)

### 1. Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies

- **arXiv**: [2608.03727v1](https://arxiv.org/abs/2608.03727v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03727v1)
- **作者**: Chenyi Wang, Xinkai Wang, Bokai Lin et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Action labels tell a vision-language-action (VLA) policy which robot commands to imitate, but not how those commands change the 3D world. The aligned demonstration clip contains this missing supervision because its $K$ frame transitions record the geometry, motion, visibility, and camera change produced during the corresponding $K$ actions. We introduce Tra…

### 2. ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies

- **arXiv**: [2608.02958v1](https://arxiv.org/abs/2608.02958v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.02958v1)
- **作者**: Inkyu Sa, Konstantin Stulov, Rajat Bhageria
- **发表**: 2026-08-03  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) policies trained by behavior cloning fail silently: from the action stream alone, a collapsing rollout looks much like one making clean progress, because imitation supplies no notion of progress. Reinforcement learning would supply one, but it is impractical here, where real-robot experience is costly and deformable food resists…

### 3. How Should Vision-Language-Action Models Use Proprioceptive State?

- **arXiv**: [2608.03052v1](https://arxiv.org/abs/2608.03052v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03052v1)
- **作者**: Yiren Zhao, Ziyang Chen, Ziyang Rao et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Recent Vision-Language-Action (VLA) models almost universally take robot proprioceptive state as input, yet wire it in incompatible ways -- serialized into text prompts, projected into the vision-language prefix, or fed directly to the action expert -- and almost always as a single current frame. Three questions remain open: (1) whether, and on which tasks,…

### 4. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

### 5. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 6. PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud

- **arXiv**: [2608.03682v1](https://arxiv.org/abs/2608.03682v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03682v1)
- **作者**: Chenghua Wang, Daliang Xu, Dongqi Cai et al.
- **发表**: 2026-08-04  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Physical AI policies require inference throughout their lifecycle, including model evaluation, cloud reinforcement learning rollout, edge GPU serving, and onboard deployment. Although these settings share the same checkpoint and action semantics, they often rely on separate inference programs. To unify them, we build PhyAI, a Physical AI inference engine wi…

### 7. DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack

- **arXiv**: [2608.03207v1](https://arxiv.org/abs/2608.03207v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03207v1)
- **作者**: Hoseong Tae, Jong-Seok Lee
- **发表**: 2026-08-04  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Flow-matching vision-language-action (VLA) models such as pi0 generate robot actions by integrating a learned denoising velocity field, and have been reported to resist adversarial perturbations that readily fool autoregressive VLAs. We show that this robustness is largely illusory: it stems from prior attacks ignoring the multi-step denoising ODE. We intro…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Learning-Based Motion Planning for Dynamic Environments: From Foundational Algorithms to Emerging Paradigms

- **arXiv**: [2608.00625v1](https://arxiv.org/abs/2608.00625v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00625v1)
- **作者**: Zongyuan Shen, Shalabh Gupta, Shancheng Zhao et al.
- **发表**: 2026-08-01  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Motion planning in dynamic environments is a fundamental problem in robotics, aiming to generate safe and efficient paths, trajectories, or control actions in the presence of moving obstacles, uncertain predictions, and multi-agent interactions. It has broad applications in autonomous driving, service robotics, warehouse logistics, human-robot collaboration…

### 2. UniNav: A Unified World-Action Diffusion Model for Visual Navigation

- **arXiv**: [2608.03244v1](https://arxiv.org/abs/2608.03244v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03244v1)
- **作者**: Changqing Zhou, Yueru Luo, Zeyu Jiang et al.
- **发表**: 2026-08-04  ·  **类别**: cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visu…

### 3. Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation

- **arXiv**: [2607.26148v2](https://arxiv.org/abs/2607.26148v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.26148v2)
- **作者**: Jian Zhou, Xunyi Zhao, Gengze Zhou et al.
- **发表**: 2026-07-28  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Autonomous embodied agents must sustain a long decision-making loop that involves perceiving, acting, verifying, and self-correcting over many steps. Current systems sustain this loop through task-specific workflows or embodied policies. However, these fixed workflows and policies offer limited flexibility across environments and often lack effective recove…

### 4. STAR-VLM: Spatiotemporal Grounding Vision-Language Models for Motion and Velocity Estimation via Automotive Radar Supervision

- **arXiv**: [2608.01535v1](https://arxiv.org/abs/2608.01535v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01535v1)
- **作者**: Pou-Chun Kung, Aryaman Rao, Utkrisht Sahai et al.
- **发表**: 2026-08-02  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Vision-language models (VLMs) are emerging as a key component of embodied intelligence, with growing applications in auto-labeling and end-to-end autonomous driving. However, existing approaches for improving spatiotemporal reasoning in VLMs often rely on complex preprocessing pipelines, expensive human annotations, or synthetic data, which limit scalabilit…

### 5. Learning Dynamic User Personas from Implicit Interaction Streams via Iterative Refinement

- **arXiv**: [2607.26473v1](https://arxiv.org/abs/2607.26473v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.26473v1)
- **作者**: Haifeng Wu
- **发表**: 2026-07-29  ·  **类别**: cs.LG, cs.CL
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Personalizing large language models (LLMs) to individual users is essential for improving user experience, yet existing approaches typically rely on explicit preference supervision such as pairwise comparisons or demographic attributes, limiting their applicability in natural interaction settings. We propose IRIS, a framework that learns dynamic user person…

### 6. When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents

- **arXiv**: [2608.01428v1](https://arxiv.org/abs/2608.01428v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01428v1)
- **作者**: Shuaijun Liu, Feiyang You, Xingwei Chen et al.
- **发表**: 2026-08-02  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents replan frequently to recover from execution drift, partial observability, and coordination hazards, but each LLM-based replanning call can consume an accumulated textual context that grows over time and across agents. Once this context becomes large, replanning latency develops heavy tails and can miss real-time deadlines even when task succ…

### 7. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 8. InteracVid: Building a Real Interactive Audio-Visual Response Dataset from Live-Chat Videos

- **arXiv**: [2608.01157v1](https://arxiv.org/abs/2608.01157v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01157v1)
- **作者**: Chi Zhang, Haoyang Shi, Yueyi Liu et al.
- **发表**: 2026-08-02  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language models have made text the default medium for human--AI interaction, buttext alone cannot express the full range of responses required by multimodal assistants,avatars, and embodied agents. While recent audio-video generative models can synthesizehigh-fidelity synchronized content, existing supervision is largely \emph{descriptive}:models are…

### 9. SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

- **arXiv**: [2607.27703v2](https://arxiv.org/abs/2607.27703v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.27703v2)
- **作者**: Yang Zhou, Zixuan Huang, Sunzhu Li et al.
- **发表**: 2026-07-30  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specia…

### 10. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

## 🦵 人形 / 足式机器人 (27 篇)

### 1. TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation

- **arXiv**: [2607.10132v2](https://arxiv.org/abs/2607.10132v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10132v2)
- **作者**: Muqun Hu, Yuhao Zhou, Kabir Ray Malik et al.
- **发表**: 2026-07-11  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback…

### 2. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 3. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine

- **arXiv**: [2607.28625v1](https://arxiv.org/abs/2607.28625v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.28625v1)
- **作者**: Yukang Cao, Haozhe Xie, Beichen Wen et al.
- **发表**: 2026-07-30  ·  **类别**: cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action…

### 4. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v1](https://arxiv.org/abs/2608.03387v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v1)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 5. Handroid: Bridging Dexterous Hand and Humanoid

- **arXiv**: [2607.16187v1](https://arxiv.org/abs/2607.16187v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16187v1)
- **作者**: Ruogu Li, Chenyang Ma, Sikai Li et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a s…

### 6. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **arXiv**: [2607.11874v1](https://arxiv.org/abs/2607.11874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11874v1)
- **作者**: Yunhai Feng, Natalie Leung, Jiaxuan Wang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires…

### 7. PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

- **arXiv**: [2607.11041v1](https://arxiv.org/abs/2607.11041v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11041v1)
- **作者**: Zhengmao He, Moonkyu Jung, Hyeongjun Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Loco-manipulation has recently shown promising capabilities; however, achieving high-precision control, managing the high-dimensional action space induced by many degrees of freedom (DoFs), and fully exploiting the inherent redundancy of whole-body systems remain challenging. In this paper, we propose a novel whole-body control framework that effectively ad…

### 8. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 9. Immersive Social Interaction with VR and LLM-Assisted Humanoids

- **arXiv**: [2607.07430v1](https://arxiv.org/abs/2607.07430v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07430v1)
- **作者**: Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO, eess.SY
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidi…

### 10. PFM-HR: Pose Flow Matching for Humanoid Robots

- **arXiv**: [2608.03227v1](https://arxiv.org/abs/2608.03227v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03227v1)
- **作者**: Yukang Gao, Yi Gu, Yangchen Zhou et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Motion priors improve reinforcement learning for physics-based humanoid tracking, but temporal priors require ordered motion clips, while pose priors provide limited guidance for policy-induced pose transitions. We present Pose Flow Matching for Humanoid Robots (PFM-HR), a reusable flow matching prior trained directly on large scale unordered pose data. PFM…

## 🦾 操控 / 灵巧手 / 抓取 (29 篇)

### 1. DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- **arXiv**: [2607.08751v1](https://arxiv.org/abs/2607.08751v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08751v1)
- **作者**: Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering st…

### 2. Data Pyramid for Embodied Manipulation

- **arXiv**: [2607.24744v1](https://arxiv.org/abs/2607.24744v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.24744v1)
- **作者**: Yifan Ye, Yankai Fu, Yaoxu Lv et al.
- **发表**: 2026-07-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Multimodal foundation models learned to see and to speak by consuming the whole internet. Embodied agents admit no such shortcut, since they require data that couple observations with physical states and actions. These signals can be provided, to varying degrees, by multiple data sources. In this work, we organize the embodied data ecosystem as a "pyramid"…

### 3. Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking

- **arXiv**: [2608.03231v1](https://arxiv.org/abs/2608.03231v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03231v1)
- **作者**: Jinquan Zhang, Dongfu Yin, Run Yang et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned at…

### 4. ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction

- **arXiv**: [2608.01824v1](https://arxiv.org/abs/2608.01824v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01824v1)
- **作者**: Shiqi Zhang, Xin Zhang, Yedong Shen et al.
- **发表**: 2026-08-03  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports conta…

### 5. UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis

- **arXiv**: [2607.28198v1](https://arxiv.org/abs/2607.28198v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.28198v1)
- **作者**: Hui Zhang, Julian Ferchow, Jie Song et al.
- **发表**: 2026-07-30  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Many dexterous manipulation tasks require the object to remain securely held throughout the interaction. From the perspective of hand-object relational motion, such manipulation comprises four canonical skills: grasping, relocation, in-hand rotation, and in-hand translation. Human hands flexibly compose these skills to accomplish complex tasks. Existing app…

### 6. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 7. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 8. MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand

- **arXiv**: [2607.14487v1](https://arxiv.org/abs/2607.14487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14487v1)
- **作者**: Alvin Zhu, Mingzhang Zhu, Beom Jun Kim et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, hu…

### 9. AnyDexRT: Calibration-Free Dexterous Hand Retargeting with Few-Shot Human Guidance

- **arXiv**: [2607.08341v1](https://arxiv.org/abs/2607.08341v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08341v1)
- **作者**: Chenxi Wang, Ying Feng, Hongjie Fang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Teleoperation is a key interface for controlling dexterous robotic hands and collecting demonstrations for imitation learning. Its effectiveness largely depends on kinematic retargeting, which maps operator hand motions to feasible and intuitive robot hand motions. Existing methods often require hand-crafted objectives, precise calibration, or global shape…

### 10. Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution

- **arXiv**: [2608.03483v1](https://arxiv.org/abs/2608.03483v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03483v1)
- **作者**: Weichen Xu, Zhenhua Liu, Lin Luo et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Existing chunk-based Vision-Language-Action (VLA) models execute a fixed number of actions (i.e., execution horizon) before replanning, turning replanning into a task-agnostic periodic schedule that is independent of task progress. As a result, when no replanning boundary falls before a critical manipulation stage, it is executed from a stale chunk rather t…

## 🎓 模仿学习 / 强化学习 (13 篇)

### 1. RayViT: Ray-Conditioned Visual Representations for Viewpoint-Robust Imitation Learning

- **arXiv**: [2607.29622v1](https://arxiv.org/abs/2607.29622v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.29622v1)
- **作者**: Qian Wang, Longrui Chen, Peiran Sun et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Visual imitation learning enables robots to acquire visuomotor skills directly from images, yet RGB observations lack explicit geometric cues, making learned policies brittle to camera perturbations. To address this, we propose \textbf{Ray-conditioned Vision Transformer Encoder (RayViT)}, a lightweight architecture that injects camera geometry into pretrain…

### 2. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 3. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 4. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 5. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 8. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 9. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

### 10. MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices

- **arXiv**: [2607.06600v1](https://arxiv.org/abs/2607.06600v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06600v1)
- **作者**: Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.AI, cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Line segment detection is a key building block in visual SLAM, 3D reconstruction, and industrial inspection. Recent deep learning methods have greatly improved accuracy, yet even the smallest models require several megabytes of memory, exceeding low-cost MCU capacity. This work investigates the maximum achievable accuracy under a sub-megabyte budget. We pro…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (6 篇)

### 1. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 2. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 3. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that a…

### 4. PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments

- **arXiv**: [2607.07374v1](https://arxiv.org/abs/2607.07374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07374v1)
- **作者**: Seunghun Lee, Jihun Nam, Dong-Uk Seo et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliabili…

### 5. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 6. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Certifying Plans under Model Mismatch: A Trilemma for Reachability from Scarce Data

- **arXiv**: [2608.02453v1](https://arxiv.org/abs/2608.02453v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.02453v1)
- **作者**: Yanliang Huang, Zhen Zhang, Ahmad Hafez et al.
- **发表**: 2026-08-03  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Sim-to-real policies are designed under nominal dynamics, but target-system trials may yield only a few isolated one-step transitions. We study pre-execution certification of a fixed control sequence, such as an action chunk produced by a learned policy. If the sequence reaches an unobserved state-input region, the observations remain consistent with target…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v2) — score 22
2. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2607.08751v1) — score 21
3. [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135v1) — score 18

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
