# 机器人研究每日摘要 · 2026-08-12

> 自动生成,共 88 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models

- **arXiv**: [2608.10484v1](https://arxiv.org/abs/2608.10484v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.10484v1)
- **作者**: Li Wenjie, Yash Jangir, Ignacy Stepka et al.
- **发表**: 2026-08-11  ·  **类别**: cs.RO, cs.AI, cs.CL
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Action verbs describe not only the physical outcomes of actions, but also how those actions are performed. Yet action representations in vision-language-action models (VLAs) are typically optimized for reconstruction under L1/L2 losses in raw action space, where numerical proximity need not reflect linguistically meaningful distinctions. On BridgeV2, we sho…

### 2. Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models

- **arXiv**: [2608.10824v1](https://arxiv.org/abs/2608.10824v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.10824v1)
- **作者**: Zhijie Wu, Kento Kawaharazuka, Kei Okada
- **发表**: 2026-08-11  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-Language-Action(VLA) models map camera images and language instructions directly to motor commands through a single autoregressive transformer. In real-time control, they still spend substantial compute recomputing key-value(KV) representations for visual tokens that barely change across neighboring frames. Recent work such as VLA-Cache reduces that…

### 3. Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models

- **arXiv**: [2607.10655v1](https://arxiv.org/abs/2607.10655v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.10655v1)
- **作者**: Xiatao Sun, Yuan Zhuang, Mateo Sanchez Lopez Negrete et al.
- **发表**: 2026-07-12  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Robotic foundation models have recently made substantial progress in multi-task capability, cross-embodiment transfer, and language-conditioned control. Yet robust deployment across diverse real-world settings remains difficult, in part because policies often fail to distinguish causally relevant visual structure from spurious scene-level correlations. We i…

### 4. World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

- **arXiv**: [2608.09730v1](https://arxiv.org/abs/2608.09730v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09730v1)
- **作者**: Qu Tang, Benhui Zhuang, Bo Yuan et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation…

### 5. Action- and Language-Conditioned Video Assessment for Embodied Control

- **arXiv**: [2608.08273v1](https://arxiv.org/abs/2608.08273v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.08273v1)
- **作者**: Hwanhee Kim, Jaehyun Jang, Seungmin Cha et al.
- **发表**: 2026-08-08  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-based embodied agents executing multi-step natural language instructions require feedback mechanisms that assess task progress over complete trajectories. Conventional approaches based on final-frame matching or continuous embedding similarity may overlook intermediate transitions that are necessary for determining whether an instruction has been com…

### 6. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization

- **arXiv**: [2608.08523v1](https://arxiv.org/abs/2608.08523v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.08523v1)
- **作者**: Pengfei Xu, Yong Liu, Xiaoya Nan et al.
- **发表**: 2026-08-09  ·  **类别**: cs.AI
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Multimodal embodied agents are increasingly required to solve long-horizon tasks by integrating visual observations, textual goals, and interaction history into closed-loop decision making. However, state-of-the-art large-model-based planners often rely on a single dominant planning style during execution. Once this execution mode becomes ineffective, the a…

### 2. 360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents

- **arXiv**: [2608.08814v1](https://arxiv.org/abs/2608.08814v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.08814v1)
- **作者**: Kenta Watanabe, Atsuyuki Miyai, Mizuki Takenawa et al.
- **发表**: 2026-08-09  ·  **类别**: cs.CV, cs.AI, cs.LG
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present 360CityArena, a benchmark for evaluating the urban exploration capabilities of embodied agents within a photorealistic environment constructed from 360-degree videos. Existing outdoor benchmarks either lack sufficient photorealism or complexity, resulting in a considerable gap from real-world urban environments. 360CityArena is built on a realist…

### 3. Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent

- **arXiv**: [2608.10618v1](https://arxiv.org/abs/2608.10618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.10618v1)
- **作者**: Zitong Shan, Baichuan Lou, Yanxin Zhou et al.
- **发表**: 2026-08-11  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomou…

### 4. CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems

- **arXiv**: [2608.09848v1](https://arxiv.org/abs/2608.09848v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09848v1)
- **作者**: Aimilios Hadjiliasi, Louis Nisiotis
- **发表**: 2026-08-10  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: The development of embodied Intelligent Virtual Agents (IVAs) that have cognitive capabilities in real-time interactive virtual environments remains a challenge, even with today's advancements in technology. Existing architectures are often focused on either the implementation of low-level reactive control systems that are constrained by commercial game eng…

### 5. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation

- **arXiv**: [2608.11051v1](https://arxiv.org/abs/2608.11051v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.11051v1)
- **作者**: Raphael Lorenzo-Louis, Fabio Amadio, Bertrand Luvison et al.
- **发表**: 2026-08-11  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: As robots increasingly operate in human-populated environments, anticipating human intentions is essential for enabling proactive and socially aware behavior. Automatic anticipation of human-robot interactions is thus emerging as a crucial perception challenge for embodied agents. To this end, we introduce HUI360, the largest dataset for human-robot interac…

### 8. ComBodied Agents: a New Paradigm of Human-Centric Agentic AI

- **arXiv**: [2608.10915v1](https://arxiv.org/abs/2608.10915v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.10915v1)
- **作者**: Qianggang Ding, Xingyao Wang, Rui Feng et al.
- **发表**: 2026-08-11  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform soft…

### 9. SAIN: Structure-Aware Interactive Navigation with Active Dialogue Grounding for Mobile Robot

- **arXiv**: [2608.09196v1](https://arxiv.org/abs/2608.09196v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09196v1)
- **作者**: Yuhao Cao, Xiao Liu, Yang Xie et al.
- **发表**: 2026-08-10  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Most existing vision-language navigation tasks assume that instructions are complete and unambiguous. However, real-world robots often encounter natural human instructions that are ambiguous, underspecified, or incomplete, requiring them to resolve such uncertainties through active questioning. Interactive Instance Goal Navigation (IIGN) requires an embodie…

### 10. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

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
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: Dynamic loco-manipulation requires legged robots to coordinate whole-body motion while maintaining stable physical interaction with grasped objects under uncertain external forces. While tactile sensing has been widely studied for robotic manipulation, its role in dynamic whole-body control remains largely unexplored. Existing works without tactile feedback…

### 2. Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition

- **arXiv**: [2608.09762v1](https://arxiv.org/abs/2608.09762v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09762v1)
- **作者**: Changhao Li, Yifang Zhang, Heng Zhang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Real-world online reinforcement learning (RL) provides a promising approach for training robotic manipulation policies directly in the physical world, avoiding the sim-to-real gap and enabling continuous policy refinement through human-in-the-loop interaction. Recent methods have demonstrated sample-efficient learning through human intervention but remain l…

### 3. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 4. Spatiotemporal Agility: Time-Constrained Reinforcement Learning for Vision-Guided Dynamic Quadrupedal Interception

- **arXiv**: [2608.06907v1](https://arxiv.org/abs/2608.06907v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.06907v1)
- **作者**: Yidong Zhu, Zibo Dai, Tongning Zhang et al.
- **发表**: 2026-08-07  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Legged robots require robust agility to perceive and interact with complex and dynamic environments within a constrained time. However, most existing quadruped locomotion works rely on velocity-tracking policy, which struggle to reach precise targets within strict temporal constraints. Moreover, integrating real-time perception with agile locomotion for hig…

### 5. Handroid: Bridging Dexterous Hand and Humanoid

- **arXiv**: [2607.16187v1](https://arxiv.org/abs/2607.16187v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16187v1)
- **作者**: Ruogu Li, Chenyang Ma, Sikai Li et al.
- **发表**: 2026-07-17  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a s…

### 6. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine

- **arXiv**: [2607.28625v1](https://arxiv.org/abs/2607.28625v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.28625v1)
- **作者**: Yukang Cao, Haozhe Xie, Beichen Wen et al.
- **发表**: 2026-07-30  ·  **类别**: cs.CV
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action…

### 7. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **arXiv**: [2607.11874v1](https://arxiv.org/abs/2607.11874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11874v1)
- **作者**: Yunhai Feng, Natalie Leung, Jiaxuan Wang et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires…

### 8. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v2](https://arxiv.org/abs/2608.03387v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v2)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 9. PAKE: Learning Whole-Body Loco-Manipulation with Partial Kinematic Embeddings

- **arXiv**: [2607.11041v1](https://arxiv.org/abs/2607.11041v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11041v1)
- **作者**: Zhengmao He, Moonkyu Jung, Hyeongjun Kim et al.
- **发表**: 2026-07-13  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Loco-manipulation has recently shown promising capabilities; however, achieving high-precision control, managing the high-dimensional action space induced by many degrees of freedom (DoFs), and fully exploiting the inherent redundancy of whole-body systems remain challenging. In this paper, we propose a novel whole-body control framework that effectively ad…

### 10. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

## 🦾 操控 / 灵巧手 / 抓取 (25 篇)

### 1. Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models

- **arXiv**: [2608.10393v1](https://arxiv.org/abs/2608.10393v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.10393v1)
- **作者**: Jiahui Han, Yuhui Yao, Xin Wang et al.
- **发表**: 2026-08-11  ·  **类别**: cs.AI, cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on pixel-space perturbations or white-box access, resulting in…

### 2. C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video

- **arXiv**: [2608.07045v1](https://arxiv.org/abs/2608.07045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.07045v1)
- **作者**: Jie Ren, Zhehao Jiang, Yinhong Yang et al.
- **发表**: 2026-08-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: High-quality demonstrations for dexterous robot manipulation are costly and difficult to collect, whereas monocular human videos provide a scalable source of diverse manipulation behaviors. However, transferring such demonstrations to dexterous robots remains challenging: monocular hand-object interaction (HOI) reconstruction often produces temporally unsta…

### 3. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 4. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 5. SAFE-CHEM: Uncertainty-Aware Policy Switching for Robust Robotic Chemistry

- **arXiv**: [2608.09303v1](https://arxiv.org/abs/2608.09303v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09303v1)
- **作者**: Laura Jones, Shazil Shahzad, Ayesha Sana et al.
- **发表**: 2026-08-10  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: The deployment of autonomous robotic systems in chemistry laboratories is accelerating experimental workflows and providing the foundational data for AI-driven scientific discovery. However, despite the success of data-driven methods in acquiring dexterous skills, safety remains a primary barrier to their deployment in high-risk domains, such as early-stage…

### 6. RORA: Realistic Object Reconstruction with Articulation

- **arXiv**: [2608.04842v1](https://arxiv.org/abs/2608.04842v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04842v1)
- **作者**: Hyesung Lee, Youngseon Lee, Kyutae Lee et al.
- **发表**: 2026-08-05  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Replicating real-world environments into simulation by realistic visual representation like NeRF and 3D Gaussian Splatting (3DGS) has emerged as an effective strategy to reduce the sim-to-real gap in robot learning. However, implementing object articulation during the real-to-sim process is still a challenging task. Existing motion tracking or learning base…

### 7. ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction

- **arXiv**: [2608.01824v1](https://arxiv.org/abs/2608.01824v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.01824v1)
- **作者**: Shiqi Zhang, Xin Zhang, Yedong Shen et al.
- **发表**: 2026-08-03  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Fusing tactile signals has proven effective for contact-rich manipulation, enabling robots to perceive contact states and adapt to rapidly changing physical interactions. Yet effectively integrating tactile feedback into dexterous manipulation remains underexplored. In this work, we introduce ReTouch, a vision-language-action model (VLA) that supports conta…

### 8. UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis

- **arXiv**: [2607.28198v1](https://arxiv.org/abs/2607.28198v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.28198v1)
- **作者**: Hui Zhang, Julian Ferchow, Jie Song et al.
- **发表**: 2026-07-30  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Many dexterous manipulation tasks require the object to remain securely held throughout the interaction. From the perspective of hand-object relational motion, such manipulation comprises four canonical skills: grasping, relocation, in-hand rotation, and in-hand translation. Human hands flexibly compose these skills to accomplish complex tasks. Existing app…

### 9. MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand

- **arXiv**: [2607.14487v1](https://arxiv.org/abs/2607.14487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.14487v1)
- **作者**: Alvin Zhu, Mingzhang Zhu, Beom Jun Kim et al.
- **发表**: 2026-07-16  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, hu…

### 10. SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation

- **arXiv**: [2608.04196v1](https://arxiv.org/abs/2608.04196v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.04196v1)
- **作者**: Nie Lin, Takehiko Ohkawa, Sijin Chen et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: Recent years have witnessed an explosive trend of scaling ego-centric human videos for robot manipulation, yet it remains unclear which data actually benefits dexterous manipulation. We present SiMDex, a similarity-based data mining framework that casts human data selection for VLA post-training in dexterous manipulation as a recommendation problem. For eac…

## 🎓 模仿学习 / 强化学习 (16 篇)

### 1. Overcoming Data Scarcity and Confidentiality in Hardware Assurance via Synthetic Generation

- **arXiv**: [2608.09914v1](https://arxiv.org/abs/2608.09914v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09914v1)
- **作者**: Gijung Lee, Ronald Wilson, Damon L. Woodard et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CR, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Hardware assurance relies on scanning electron microscopy (SEM) to verify nanoscale structures, but assembling the large, high-quality datasets required for automated analysis is impeded by time-intensive acquisition and strict intellectual property (IP) constraints on proprietary designs. We propose a privacy-preserving pipeline that secures IP by heavily…

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

### 4. LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning

- **arXiv**: [2608.06481v1](https://arxiv.org/abs/2608.06481v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.06481v1)
- **作者**: Riccardo Curcio, Hongpeng Cao, Marco Caccamo
- **发表**: 2026-08-06  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Training controllers that are safe and robust in simulation, and systematically assessing their readiness for real-world deployment, remain key challenges in sim-to-real transfer. To address this, we propose LyEvO, a physics-grounded framework that combines constrained Evolutionary Optimization and Statistical Model Checking (SMC)-based verification with Ly…

### 5. Dual-Attention and Adversarial Transfer Networks for Sim-to-Real Cross-Orientation Wireless Sensing

- **arXiv**: [2608.05664v1](https://arxiv.org/abs/2608.05664v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.05664v1)
- **作者**: Linfeng Du, Kehan Wu, Tong Zhang et al.
- **发表**: 2026-08-06  ·  **类别**: cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Millimeter-wave human activity recognition suffers significant performance degradation when the user's orientation changes relative to the sensing system, yet collecting labeled multi-orientation data is labor-intensive and costly. To eliminate the need for exhaustive multi-orientation measured data, we develop a physics-guided simulator that synthesizes or…

### 6. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 8. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models

- **arXiv**: [2608.06020v1](https://arxiv.org/abs/2608.06020v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.06020v1)
- **作者**: Jiale Han, Xiang Li, Jing Qian et al.
- **发表**: 2026-08-06  ·  **类别**: cs.AI, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as ge…

### 9. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (5 篇)

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

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [TAC-LOCO: Unified Whole-Body Control for Quadrupedal TACtile-Informed LOCO-Manipulation](https://arxiv.org/abs/2607.10132v2) — score 21
2. [Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition](https://arxiv.org/abs/2608.09762v1) — score 19
3. [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135v1) — score 18

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
