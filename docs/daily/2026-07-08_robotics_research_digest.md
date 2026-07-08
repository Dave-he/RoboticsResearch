# 机器人研究每日摘要 · 2026-07-08

> 自动生成,共 85 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (2 篇)

### 1. SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models

- **arXiv**: [2607.06442v1](https://arxiv.org/abs/2607.06442v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06442v1)
- **作者**: Changti Wu, Bin Yu, Zhaolong Shen et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models are typically trained by imitation learning on large-scale robot demonstration datasets, but more data does not necessarily yield better policies due to redundancy, noise, and uneven coverage. Existing data selection methods often assess demonstrations at either the trajectory or state-action level, missing the reusable s…

### 2. Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies

- **arXiv**: [2607.05122v1](https://arxiv.org/abs/2607.05122v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05122v1)
- **作者**: Adrian Szvoren, Dimitrios Kanoulas, Nilufer Tuptuk
- **发表**: 2026-07-06  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highligh…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. TypeGo: An OS Runtime for Embodied Agents

- **arXiv**: [2607.05482v1](https://arxiv.org/abs/2607.05482v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05482v1)
- **作者**: Guojun Chen, Alex Schott, Lin Zhong
- **发表**: 2026-07-06  ·  **类别**: cs.SE, cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Large language models (LLMs) can plan behavior for embodied agents from natural language, but treating the LLM as a request/response oracle on the critical path is fundamentally at odds with real-time control and concurrent goals. We argue for an operating-system-style runtime for embodied agents, and instantiate this idea in an early prototype, TypeGo. Typ…

### 2. Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator

- **arXiv**: [2607.05765v1](https://arxiv.org/abs/2607.05765v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05765v1)
- **作者**: Zihan Wang, Seungjun Lee, Yinghao Xu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Embodied navigation aims to build agents that interpret multimodal goals, reason in 3D space, and reach target destinations reliably in the real world. However, progress remains constrained by the lack of scalable, high-fidelity, and physically grounded interactive environments. Although real-world scanned datasets offer visual realism, they are limited by…

### 3. Overloading Large Vision-Language Models for Jailbreaking

- **arXiv**: [2607.02961v1](https://arxiv.org/abs/2607.02961v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02961v1)
- **作者**: Haoyu Zhang, Yangyang Guo, Mohan Kankanhalli
- **发表**: 2026-07-03  ·  **类别**: cs.CV, cs.CR
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Large Vision-Language Models (LVLMs) exhibit remarkable vision-language capabilities and are increasingly deployed in real-world applications such as personal assistants, document analysis systems, and embodied agents. However, their dual-modal attack surfaces make them vulnerable to jailbreak attacks. Existing LVLM jailbreaks rely on simple designs, e.g.,…

### 4. Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation

- **arXiv**: [2607.01754v1](https://arxiv.org/abs/2607.01754v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01754v1)
- **作者**: Sung June Kim, Sangpil Kim, Honglak Lee
- **发表**: 2026-07-02  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: On-policy exploration is a crucial component for training robust Vision-Language Navigation agents, as it exposes the policy to a broader state distribution. However, such exploration inevitably leads to trajectories that deviate from expert demonstrations, resulting in a semantic mismatch between the executed visual stream and the original language instruc…

### 5. Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments

- **arXiv**: [2607.00457v1](https://arxiv.org/abs/2607.00457v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00457v1)
- **作者**: Jinwoo Jang, Daniel J. Rho, Sihyung Yoon et al.
- **发表**: 2026-07-01  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a uniform update policy cannot accommodate the different rates…

### 6. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 7. Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning

- **arXiv**: [2607.06501v1](https://arxiv.org/abs/2607.06501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06501v1)
- **作者**: Anxing Xiao, Hanbo Zhang, Tianrun Hu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We consider an open-world planning setting in which service robots must operate in unknown environments with incomplete knowledge of objects and actions. Traditional closed-world approaches with pre-programmed knowledge bases fail when robots encounter unexpected situations and tasks, posing a fundamental challenge for autonomous knowledge expansion in huma…

### 8. RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail

- **arXiv**: [2607.00310v1](https://arxiv.org/abs/2607.00310v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00310v1)
- **作者**: Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar et al.
- **发表**: 2026-07-01  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocent…

### 9. EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards

- **arXiv**: [2607.00218v1](https://arxiv.org/abs/2607.00218v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00218v1)
- **作者**: Siddhant Panpatil, Arth Singh, Mijin Koo et al.
- **发表**: 2026-06-30  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric v…

## 🦵 人形 / 足式机器人 (23 篇)

### 1. RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation

- **arXiv**: [2606.31836v1](https://arxiv.org/abs/2606.31836v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31836v1)
- **作者**: Xinyi Wang, Donghan Li, Zi'Ang Chen et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTa…

### 2. Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning

- **arXiv**: [2607.02205v2](https://arxiv.org/abs/2607.02205v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02205v2)
- **作者**: Satoshi Yamamori, Koji Ishihara, Kenjiro Minamikawa et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learne…

### 3. Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory

- **arXiv**: [2606.31037v2](https://arxiv.org/abs/2606.31037v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31037v2)
- **作者**: Yuhan Wu, Zhao Jin, Tao Li et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, m…

### 4. Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots

- **arXiv**: [2607.01574v1](https://arxiv.org/abs/2607.01574v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01574v1)
- **作者**: Taizoon Chunawala, Jeeseop Kim, Kaveh Akbari Hamed
- **发表**: 2026-07-02  ·  **类别**: cs.RO, math.OC
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: This paper presents a novel layered planning and control framework based on multi-rate nonlinear model predictive control (MR-NMPC) that enables quadrupedal robots to perform hybrid bipedal locomotion with wall-assisted support in constrained environments. Real-time trajectory optimization for this locomotion presents significant challenges, as the controll…

### 5. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 6. Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot

- **arXiv**: [2606.31807v1](https://arxiv.org/abs/2606.31807v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31807v1)
- **作者**: Ethan Marot, Thomas Bi, Clemens Schwarke et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-effici…

### 7. CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation

- **arXiv**: [2606.27676v1](https://arxiv.org/abs/2606.27676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27676v1)
- **作者**: Wenqi Ge, Junde Guo, Zhen Fu et al.
- **发表**: 2026-06-26  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Achieving everyday tasks with humanoid robots requires coordinating stable locomotion with versatile manipulation. However, existing whole-body controllers still face significant challenges. Methods trained solely via command sampling, without motion-capture (MoCap) data, often struggle with sparse rewards and require carefully tuned curricula to converge.…

### 8. HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation

- **arXiv**: [2606.27239v2](https://arxiv.org/abs/2606.27239v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27239v2)
- **作者**: Hongwu Wang, Chenhao Yu, Youhao Hu et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors that require coordinated perception, locomotion, and manipulation. Existing data-collection methods largely rely on robot teleoperation, which is constrained by hardware accessibility, operator expertise, and limited efficiency. Inspired by t…

### 9. ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force Demonstrations

- **arXiv**: [2607.06052v1](https://arxiv.org/abs/2607.06052v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06052v1)
- **作者**: Chenhao Yu, Hongwu Wang, Weitao Zhang et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots are increasingly expected to perform contact-rich tasks that require not only accurate whole-body motion but also robust physical interaction with surrounding objects and humans. Although recent advances in humanoid motion imitation and whole-body control have achieved remarkable tracking performance, existing datasets and benchmarks primari…

### 10. From Foundation to Application: Improving VLA Models in Practice

- **arXiv**: [2607.06403v1](https://arxiv.org/abs/2607.06403v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06403v1)
- **作者**: Wei Wu, Fangjing Wang, Fan Lu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to…

## 🦾 操控 / 灵巧手 / 抓取 (31 篇)

### 1. Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation

- **arXiv**: [2607.04940v1](https://arxiv.org/abs/2607.04940v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.04940v1)
- **作者**: Zhe Zhao, Zhibin Li, Yilin Ou et al.
- **发表**: 2026-07-06  ·  **类别**: cs.RO
- **相关性评分**: 24  ·  **🔥 read_now**
- **摘要**: Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing t…

### 2. LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation

- **arXiv**: [2607.06323v1](https://arxiv.org/abs/2607.06323v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06323v1)
- **作者**: Xinye Yang, Zhiyuan Ma, Hongze Yu et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: Real-world learning for dexterous hands remains brittle because high-dimensional hand actions amplify imitation errors and make reinforcement-learning exploration prone to contact-breaking motion. While combining imitation learning (IL) with online reinforcement learning (RL) can reduce manual supervision, unconstrained exploration in raw hand-action spaces…

### 3. Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation

- **arXiv**: [2607.05377v1](https://arxiv.org/abs/2607.05377v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05377v1)
- **作者**: Jiaqi Peng, Xiqian Yu, Delin Feng et al.
- **发表**: 2026-07-06  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We int…

### 4. GraspIT: A Dataset Bridging the Sim-to-Real gap and back for Validated Grasping SE(3) Pose Generation

- **arXiv**: [2607.05869v1](https://arxiv.org/abs/2607.05869v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05869v1)
- **作者**: Paul Koch. Adem Karakurt, André Sers
- **发表**: 2026-07-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Robust robotic grasping of novel objects requires datasets that simultaneously provide photorealistic RGB-D observations, physically validated grasp quality annotations, and a principled bridge between simulation and the real world, which existing datasets lack to provide jointly. \textbf{GraspIT} addresses this gap: tabletop scenes in NVIDIA Isaac Sim are…

### 5. Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation

- **arXiv**: [2607.06564v1](https://arxiv.org/abs/2607.06564v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06564v1)
- **作者**: Jiaming Liu, Qingpo Wuwu, Nuowei Han et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Recently, Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse tasks. However, effective robotic manipulation in physical environments fundamentally requires geometric understanding and spatial reasoning. While some VLA approaches attempt to incorporate 3D information, they are constrained by limited data availability a…

### 6. Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation

- **arXiv**: [2607.03529v1](https://arxiv.org/abs/2607.03529v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.03529v1)
- **作者**: Chenyang Ma, Yunchao Yao, Zhenyu Wei et al.
- **发表**: 2026-07-03  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Compliance is essential for dexterous manipulation, yet existing solutions often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands. We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states. Since motor current is closely relate…

### 7. SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing

- **arXiv**: [2607.04616v1](https://arxiv.org/abs/2607.04616v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.04616v1)
- **作者**: Stone Tao, Jie Xu, Hesam Rabeti et al.
- **发表**: 2026-07-06  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Linear-deformable manipulation remains challenging due to the complex deformations of objects such as cables and ropes. Prior data-driven approaches, particularly imitation learning, have shown some promise in narrowly defined settings but typically require thousands of demonstrations for specific tasks and cable types, limiting scalability and generalizati…

### 8. WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control

- **arXiv**: [2607.03941v1](https://arxiv.org/abs/2607.03941v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.03941v1)
- **作者**: Jiahao Jiang, Jianing Zhang, Zhenhan Yin et al.
- **发表**: 2026-07-04  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current…

### 9. UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models

- **arXiv**: [2606.31723v1](https://arxiv.org/abs/2606.31723v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31723v1)
- **作者**: Xidong Zhang, Yichi Zhang, Jiaxin Shi et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat…

### 10. VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models

- **arXiv**: [2607.04517v1](https://arxiv.org/abs/2607.04517v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.04517v1)
- **作者**: Damir Shodiev, Aleksei Staroverov, Nikita Kachaev et al.
- **发表**: 2026-07-05  ·  **类别**: cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies…

## 🎓 模仿学习 / 强化学习 (18 篇)

### 1. MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM

- **arXiv**: [2606.19874v1](https://arxiv.org/abs/2606.19874v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.19874v1)
- **作者**: Fan Zhu, Ziyu Chen, Peichen Liu et al.
- **发表**: 2026-06-18  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: 3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to in…

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

### 4. Why does Deep Learning Improve Visual SLAM?

- **arXiv**: [2607.06023v1](https://arxiv.org/abs/2607.06023v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06023v1)
- **作者**: Giovanni Cioffi, Davide Scaramuzza
- **发表**: 2026-07-07  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combinin…

### 5. A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity

- **arXiv**: [2607.02005v1](https://arxiv.org/abs/2607.02005v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02005v1)
- **作者**: Sujan Kumar Dhali, Bhaskar Dasgupta
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping. To address this…

### 6. Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints

- **arXiv**: [2606.27509v1](https://arxiv.org/abs/2606.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27509v1)
- **作者**: Huaiyuan Weng, Huibin Li, Chul Min Yeum
- **发表**: 2026-06-25  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In this study, we develop a Structured framework for Gaussian Splatting (3DGS) with LiDAR integration (Structured-Li-GS). It is a lightweight Gaussian Splatting pipeline that leverages LiDAR-inertial-visual SLAM. Structured-Li-GS achieves high-quality 3D reconstructions with fewer Gaussians by training on accurate, dense, colorized point clouds. Gaussian pr…

### 7. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 8. Learning to Throw Objects Safely in Multi-Obstacle Environments

- **arXiv**: [2607.06388v1](https://arxiv.org/abs/2607.06388v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06388v1)
- **作者**: Mohammadreza Kasaei, Klemen Voncina, Hamidreza Kasaei
- **发表**: 2026-07-07  ·  **类别**: cs.RO, cs.CV, cs.LG
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Robotic throwing enables fast and efficient object placement beyond the robot's immediate workspace, but reliable throwing in cluttered environments remains underexplored. Existing approaches, such as TossingBot, learn throwing strategies from visual input but assume obstacle-free settings. In this paper, we address the problem of throwing objects into a ta…

### 9. Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure

- **arXiv**: [2607.05805v1](https://arxiv.org/abs/2607.05805v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.05805v1)
- **作者**: Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore
- **发表**: 2026-07-07  ·  **类别**: cs.AI, cs.LG, quant-ph
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, yet their fault diagnosis is still dominated by threshold alarms that report that something is wrong, not what. We present Onnes, a physics-grounded digital-twin simulator of a dilution refrigerator (a forward physics model with a learned real-fridge noise fingerpri…

### 10. Hilti-Trimble-Oxford Dataset: 360 Visual-Inertial Benchmark with Floor Plan Priors for SLAM and Localization

- **arXiv**: [2607.06464v1](https://arxiv.org/abs/2607.06464v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.06464v1)
- **作者**: Samuele Centanni, Yuhao Zhang, Yifu Tao et al.
- **发表**: 2026-07-07  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Automated progress monitoring on construction sites is an active area of research and development. Robot and human-carried mapping systems have been developed to build 3D maps of building and infrastructure projects. While LiDAR-based mapping systems achieve high accuracy, the cost of LiDAR can be prohibitive. Consumer-grade cameras with wide field of view…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (2 篇)

### 1. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 2. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation](https://arxiv.org/abs/2607.04940v1) — score 24
2. [LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation](https://arxiv.org/abs/2607.06323v1) — score 22
3. [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377v1) — score 20

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
