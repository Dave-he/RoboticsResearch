# 机器人研究每日摘要 · 2026-08-08

> 自动生成,共 91 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (5 篇)

### 1. Explicit Language Memory for Long-Horizon Planning in Vision-Language-Action Models

- **arXiv**: [2608.04765v1](https://arxiv.org/abs/2608.04765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04765v1)
- **作者**: Houze Xu, Jizhong Li, Ziyi Ye
- **发表**: 2026-08-05  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models provide a unified paradigm for connecting visual perception, language understanding, and robotic control. However, existing VLA models still face major challenges in long-horizon tasks: sparse expert demonstrations constrain cross-task compositional generalization; the non-Markovian nature of long-horizon tasks makes it d…

### 2. SAFECAST: Robust Failure Detection for VLA Policies with Contrast-Set Training and Calibration

- **arXiv**: [2608.04246v1](https://arxiv.org/abs/2608.04246v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04246v1)
- **作者**: Harshitha Rajaprakash, Aditeya Prajapati, Rong Xue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-language-action policies often fail under deployment-time distribution shifts such as clutter, distractor objects, lighting changes, novel objects, altered initial states, and reworded instructions. Hidden-state-based risk probes combined with functional conformal prediction can detect rollout failures, but their reliability depends on calibration da…

### 3. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 4. Suppression Sticks, Locality Is Fragile: A Closed-Loop Target-and-Control Audit of Task-Vector Negation in VLA Policies

- **arXiv**: [2608.04692v1](https://arxiv.org/abs/2608.04692v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04692v1)
- **作者**: Shaoguang Wang, Weiyu Guo, Rushi Dai et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Task-vector arithmetic offers a closed-form way to modify a model, yet its behavioral locality remains unclear in closed-loop robot control. We present a target-and-control audit of per-skill task-vector subtraction from multitask vision-language-action (VLA) policies. Across all ten LIBERO-Goal skills, subtraction produces three qualitatively different reg…

### 5. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. UniNav: A Unified World-Action Diffusion Model for Visual Navigation

- **arXiv**: [2608.03244v1](https://arxiv.org/abs/2608.03244v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03244v1)
- **作者**: Changqing Zhou, Yueru Luo, Zeyu Jiang et al.
- **发表**: 2026-08-04  ·  **类别**: cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Image-goal visual navigation is a fundamental capability for embodied agents. Existing navigation policies efficiently predict waypoint trajectories but lack visual foresight, while navigation world models can anticipate future observations but often require costly planning rollouts. We present UniNav, a unified world-action model that generates future visu…

### 2. GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?

- **arXiv**: [2608.05747v1](https://arxiv.org/abs/2608.05747v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05747v1)
- **作者**: Qifeng Zhang, Kaixiang Huang, Heng Dong et al.
- **发表**: 2026-08-06  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Spatial intelligence is fundamental to embodied agents, yet existing benchmarks focus on local spatial perception from single or few viewpoints, overlooking global spatial awareness over continuous, long-horizon visual streams. To address this limitation, we introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global spatial inte…

### 3. SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries

- **arXiv**: [2608.05604v1](https://arxiv.org/abs/2608.05604v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05604v1)
- **作者**: Xingyu Tan, Xiaoyang Wang, Qing Liu et al.
- **发表**: 2026-08-06  ·  **类别**: cs.CL, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Large Language Models (LLMs) increasingly act as agents whose procedural knowledge is stored in reusable skill packages and loaded at inference time. As skill libraries grow, a central challenge is to expose the smallest sufficient executable context under a limited context budget. Existing systems struggle to reuse routines below the whole-skill level, pre…

### 4. Mimir: A Neuro-Symbolic Memory System with Dynamic Grounding for Embodied Agents in Interactive Environments

- **arXiv**: [2608.04933v1](https://arxiv.org/abs/2608.04933v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04933v1)
- **作者**: Haoming Xu, Zhenlin He, Hengyi Wang et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Long-horizon embodied task requires agents to act under partial observability while preserving both scene belief and execution progress. Flat histories or implicit policy states may contain past observations, but they do not provide an explicit interface for deciding which world facts support the currently active goal. We introduce Mimir, a neuro-symbolic m…

### 5. When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents

- **arXiv**: [2608.01428v1](https://arxiv.org/abs/2608.01428v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01428v1)
- **作者**: Shuaijun Liu, Feiyang You, Xingwei Chen et al.
- **发表**: 2026-08-02  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents replan frequently to recover from execution drift, partial observability, and coordination hazards, but each LLM-based replanning call can consume an accumulated textual context that grows over time and across agents. Once this context becomes large, replanning latency develops heavy tails and can miss real-time deadlines even when task succ…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. InteracVid: Building a Real Interactive Audio-Visual Response Dataset from Live-Chat Videos

- **arXiv**: [2608.01157v1](https://arxiv.org/abs/2608.01157v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01157v1)
- **作者**: Chi Zhang, Haoyang Shi, Yueyi Liu et al.
- **发表**: 2026-08-02  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Large language models have made text the default medium for human--AI interaction, buttext alone cannot express the full range of responses required by multimodal assistants,avatars, and embodied agents. While recent audio-video generative models can synthesizehigh-fidelity synchronized content, existing supervision is largely \emph{descriptive}:models are…

### 8. SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

- **arXiv**: [2607.27703v2](https://arxiv.org/abs/2607.27703v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.27703v2)
- **作者**: Yang Zhou, Zixuan Huang, Sunzhu Li et al.
- **发表**: 2026-07-30  ·  **类别**: cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specia…

### 9. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

## 🦵 人形 / 足式机器人 (26 篇)

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

### 3. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v2](https://arxiv.org/abs/2608.03387v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v2)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 4. Handroid: Bridging Dexterous Hand and Humanoid

- **arXiv**: [2607.16187v1](https://arxiv.org/abs/2607.16187v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16187v1)
- **作者**: Ruogu Li, Chenyang Ma, Sikai Li et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a s…

### 5. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine

- **arXiv**: [2607.28625v1](https://arxiv.org/abs/2607.28625v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.28625v1)
- **作者**: Yukang Cao, Haozhe Xie, Beichen Wen et al.
- **发表**: 2026-07-30  ·  **类别**: cs.CV
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action…

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

### 9. KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots

- **arXiv**: [2608.05647v1](https://arxiv.org/abs/2608.05647v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05647v1)
- **作者**: Jixin Gao, Fucheng Liu, Teng Zhang et al.
- **发表**: 2026-08-06  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated Kal…

### 10. PFM-HR: Pose Flow Matching for Humanoid Robots

- **arXiv**: [2608.03227v1](https://arxiv.org/abs/2608.03227v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03227v1)
- **作者**: Yukang Gao, Yi Gu, Yangchen Zhou et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Motion priors improve reinforcement learning for physics-based humanoid tracking, but temporal priors require ordered motion clips, while pose priors provide limited guidance for policy-induced pose transitions. We present Pose Flow Matching for Humanoid Robots (PFM-HR), a reusable flow matching prior trained directly on large scale unordered pose data. PFM…

## 🦾 操控 / 灵巧手 / 抓取 (30 篇)

### 1. Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation

- **arXiv**: [2608.05999v1](https://arxiv.org/abs/2608.05999v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05999v1)
- **作者**: He Kong, Zengjue Chen, Qi Wang et al.
- **发表**: 2026-08-06  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform robust long-horizon manipulation. Although hier…

### 2. DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation

- **arXiv**: [2607.08751v1](https://arxiv.org/abs/2607.08751v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.08751v1)
- **作者**: Yunchao Yao, Zhuxiu Xu, Tianqi Zhang et al.
- **发表**: 2026-07-09  ·  **类别**: cs.RO
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Building general-purpose dexterous manipulation policies requires benchmarks that go beyond isolated tasks to systematically evaluate policies across diverse interaction modes, sensory conditions, and robot embodiments. However, existing benchmarks remain limited in task and data diversity, embodiment coverage, or controllable visual variation, hindering st…

### 3. BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation

- **arXiv**: [2608.05042v1](https://arxiv.org/abs/2608.05042v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05042v1)
- **作者**: Peiyan Li, Yuze Zhu, Yixiang Chen et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations. These limitations hinder their appli…

### 4. World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation

- **arXiv**: [2608.05369v1](https://arxiv.org/abs/2608.05369v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05369v1)
- **作者**: Yuhao Pan, Haosong Peng, Zhengshen Zhang et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context. To address this limitation, we present World-to-Wrist VL…

### 5. ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction

- **arXiv**: [2608.01824v1](https://arxiv.org/abs/2608.01824v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01824v1)
- **作者**: Shiqi Zhang, Xin Zhang, Yedong Shen et al.
- **发表**: 2026-08-03  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports conta…

### 6. DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation

- **arXiv**: [2608.06374v1](https://arxiv.org/abs/2608.06374v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.06374v1)
- **作者**: Junfeng Li, Junjie He, Zhide Zhong et al.
- **发表**: 2026-08-06  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer…

### 7. SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation

- **arXiv**: [2608.05970v1](https://arxiv.org/abs/2608.05970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05970v1)
- **作者**: Changyuan Wang, Chubin Zhang, Zhenyu Wu et al.
- **发表**: 2026-08-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of…

### 8. In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use

- **arXiv**: [2608.05738v1](https://arxiv.org/abs/2608.05738v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05738v1)
- **作者**: Jiarui Yang, Wen Huang, Jiale Zhang et al.
- **发表**: 2026-08-06  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have become the dominant recipe for generalist manipulation, yet they are almost universally trained by behavior cloning: a policy imitates expert action chunks conditioned on a static image and a fixed instruction. A natural remedy is to inject explicit reasoning through textual chain-of-thought (CoT). We show, both empi…

### 9. RORA: Realistic Object Reconstruction with Articulation

- **arXiv**: [2608.04842v1](https://arxiv.org/abs/2608.04842v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04842v1)
- **作者**: Hyesung Lee, Youngseon Lee, Kyutae Lee et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Replicating real-world environments into simulation by realistic visual representation like NeRF and 3D Gaussian Splatting (3DGS) has emerged as an effective strategy to reduce the sim-to-real gap in robot learning. However, implementing object articulation during the real-to-sim process is still a challenging task. Existing motion tracking or learning base…

### 10. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 2. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 3. Dual-Attention and Adversarial Transfer Networks for Sim-to-Real Cross-Orientation Wireless Sensing

- **arXiv**: [2608.05664v1](https://arxiv.org/abs/2608.05664v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05664v1)
- **作者**: Linfeng Du, Kehan Wu, Tong Zhang et al.
- **发表**: 2026-08-06  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Millimeter-wave human activity recognition suffers significant performance degradation when the user's orientation changes relative to the sensing system, yet collecting labeled multi-orientation data is labor-intensive and costly. To eliminate the need for exhaustive multi-orientation measured data, we develop a physics-guided simulator that synthesizes or…

### 4. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 5. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 6. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models

- **arXiv**: [2608.06020v1](https://arxiv.org/abs/2608.06020v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.06020v1)
- **作者**: Jiale Han, Xiang Li, Jing Qian et al.
- **发表**: 2026-08-06  ·  **类别**: cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as ge…

### 7. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 8. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

### 9. Query Quantized Neural SLAM

- **arXiv**: [2412.16476v1](https://arxiv.org/abs/2412.16476v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2412.16476v1)
- **作者**: Sijia Jiang, Jing Hua, Zhizhong Han
- **发表**: 2024-12-21  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Neural implicit representations have shown remarkable abilities in jointly modeling geometry, color, and camera poses in simultaneous localization and mapping (SLAM). Current methods use coordinates, positional encodings, or other geometry features as input to query neural implicit functions for signed distances and color which produce rendering errors to d…

### 10. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

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
- **相关性评分**: 2  ·  **📌 info**
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
1. [Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation](https://arxiv.org/abs/2608.05999v1) — score 22
2. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v2) — score 22
3. [DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation](https://arxiv.org/abs/2607.08751v1) — score 21

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
