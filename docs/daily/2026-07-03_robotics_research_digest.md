# 机器人研究每日摘要 · 2026-07-03

> 自动生成,共 90 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (4 篇)

### 1. Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots

- **arXiv**: [2607.02501v1](https://arxiv.org/abs/2607.02501v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02501v1)
- **作者**: Ling Xu, Chuyu Han, Borui Li et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.CV, cs.OS
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do…

### 2. Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs

- **arXiv**: [2607.02466v1](https://arxiv.org/abs/2607.02466v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02466v1)
- **作者**: Junhao Shi, Siyin Wang, Xiaopeng Yu et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of expert demonstrations -- triplets of observations, instructions, and actions that are costly to collect at scale. We argue that this bottleneck stems from conflating two distinct learning objectives: acquiring physical competence (how to move) and acquiring semantic alignm…

### 3. CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation

- **arXiv**: [2607.02222v1](https://arxiv.org/abs/2607.02222v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02222v1)
- **作者**: Haokun Liu, Zhaoqi Ma, Yicheng Chen et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language Navigation has increasingly emphasized high-level instruction reasoning, memory, global map construction, and instruction decomposition, while the low-level action representation remains comparatively underexplored. We propose CoFL-S, a low-level vision-language-action framework that predicts a language-conditioned flow field over the robot'…

### 4. Robots Need More than VLA and World Models

- **arXiv**: [2606.06556v1](https://arxiv.org/abs/2606.06556v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.06556v1)
- **作者**: Elis Karcini, Faisal Mehrban, Quang Nguyen et al.
- **发表**: 2026-06-04  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the…

## 🌐 具身智能 / 机器人基础模型 (10 篇)

### 1. Path-level Hindsight Instructions for Semantic Exploration in Vision-Language Navigation

- **arXiv**: [2607.01754v1](https://arxiv.org/abs/2607.01754v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01754v1)
- **作者**: Sung June Kim, Sangpil Kim, Honglak Lee
- **发表**: 2026-07-02  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: On-policy exploration is a crucial component for training robust Vision-Language Navigation agents, as it exposes the policy to a broader state distribution. However, such exploration inevitably leads to trajectories that deviate from expert demonstrations, resulting in a semantic mismatch between the executed visual stream and the original language instruc…

### 2. MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments

- **arXiv**: [2606.31966v1](https://arxiv.org/abs/2606.31966v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31966v1)
- **作者**: Qingyun Liu, Jiwen Zhang, Jingyi Hu et al.
- **发表**: 2026-06-30  ·  **类别**: cs.MA, cs.AI, cs.CL
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures,…

### 3. ScaRF-SLAM: Scale-Consistent Reconstruction with Feed-Forward Models and Classical Visual SLAM

- **arXiv**: [2606.00307v1](https://arxiv.org/abs/2606.00307v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00307v1)
- **作者**: Yuhao Zhang, Yifu Tao, Frank Dellaert et al.
- **发表**: 2026-05-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent works have explored unifying SLAM with geometric foundation models (GFMs). However, directly using GFM predictions for tracking is highly sensitive to model capability and uncertainty, as geometric inaccuracies in the predictions can adversely affect pose estimation. To address this limitation, we present a decoupled framework that integrates classic…

### 4. Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments

- **arXiv**: [2607.00457v1](https://arxiv.org/abs/2607.00457v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00457v1)
- **作者**: Jinwoo Jang, Daniel J. Rho, Sihyung Yoon et al.
- **发表**: 2026-07-01  ·  **类别**: cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents operating in the real world require multi-scale reasoning and knowledge adaptation as conditions change. We identify two challenges in applying Mixture of Experts (MoE) to this setting: routing lacks an explicit notion of scale, preventing targeted updates at specific scales, and a uniform update policy cannot accommodate the different rates…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. RetailSMV: Exocentric vs. Egocentric Adaptation of Foundation Video World Models in Retail

- **arXiv**: [2607.00310v1](https://arxiv.org/abs/2607.00310v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00310v1)
- **作者**: Amirreza Rouhi, Rajat Aggarwal, Parikshit Sakurikar et al.
- **发表**: 2026-07-01  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Foundation video diffusion models are increasingly viewed as world simulators for embodied agents, yet their pretraining on internet-scale generic video leaves them poorly aligned with real-world deployment domains. We study parameter-efficient adaptation of a pretrained foundation video world model to retail scenes: when synchronized egocentric and exocent…

### 7. EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards

- **arXiv**: [2607.00218v1](https://arxiv.org/abs/2607.00218v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00218v1)
- **作者**: Siddhant Panpatil, Arth Singh, Mijin Koo et al.
- **发表**: 2026-06-30  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric v…

### 8. MVP-Nav: Multi-layer Value Map Planner Navigator

- **arXiv**: [2606.31919v1](https://arxiv.org/abs/2606.31919v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31919v1)
- **作者**: Wenyuan Xie, Shaokai Wu, Yijin Zhou et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies t…

### 9. Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation

- **arXiv**: [2606.31071v1](https://arxiv.org/abs/2606.31071v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31071v1)
- **作者**: Bing Wu, Zuyao Chen, Changwen Chen
- **发表**: 2026-06-30  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Semantic navigation is a fundamental task for embodied agents operating in unseen environments, requiring both semantic understanding and long-term decision-making. Recent foundation models have empowered agents with rich semantic priors for this task. However, without structured global representations, decision-making often falls back on local observations…

### 10. LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents

- **arXiv**: [2606.31045v1](https://arxiv.org/abs/2606.31045v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31045v1)
- **作者**: Jingpu Yang, Fengxian Ji, Zhengzhao Lai et al.
- **发表**: 2026-06-30  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating…

## 🦵 人形 / 足式机器人 (24 篇)

### 1. RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation

- **arXiv**: [2606.31836v1](https://arxiv.org/abs/2606.31836v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31836v1)
- **作者**: Xinyi Wang, Donghan Li, Zi'Ang Chen et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 22  ·  **🔥 read_now**
- **摘要**: In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTa…

### 2. Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory

- **arXiv**: [2606.31037v2](https://arxiv.org/abs/2606.31037v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31037v2)
- **作者**: Yuhan Wu, Zhao Jin, Tao Li et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, m…

### 3. Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning

- **arXiv**: [2607.02205v1](https://arxiv.org/abs/2607.02205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02205v1)
- **作者**: Satoshi Yamamori, Koji Ishihara, Kentaro Minamikawa et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learne…

### 4. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 5. A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

- **arXiv**: [2606.26425v1](https://arxiv.org/abs/2606.26425v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.26425v1)
- **作者**: Duncan William Calvert
- **发表**: 2026-06-24  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Humanoid robots could take on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole body motion, perception, contact, and operator supervision. This thesis presents a robot-local, runtime-editable behavior authoring and runtime system. Our system strives to…

### 6. Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot

- **arXiv**: [2606.31807v1](https://arxiv.org/abs/2606.31807v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31807v1)
- **作者**: Ethan Marot, Thomas Bi, Clemens Schwarke et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-effici…

### 7. CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation

- **arXiv**: [2606.27676v1](https://arxiv.org/abs/2606.27676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27676v1)
- **作者**: Wenqi Ge, Junde Guo, Zhen Fu et al.
- **发表**: 2026-06-26  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Achieving everyday tasks with humanoid robots requires coordinating stable locomotion with versatile manipulation. However, existing whole-body controllers still face significant challenges. Methods trained solely via command sampling, without motion-capture (MoCap) data, often struggle with sparse rewards and require carefully tuned curricula to converge.…

### 8. CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation

- **arXiv**: [2606.23680v1](https://arxiv.org/abs/2606.23680v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.23680v1)
- **作者**: Sikai Li, Shuning Li, Zhenyu Wei et al.
- **发表**: 2026-06-22  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexter…

### 9. Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots

- **arXiv**: [2607.01574v1](https://arxiv.org/abs/2607.01574v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01574v1)
- **作者**: Taizoon Chunawala, Jeeseop Kim, Kaveh Akbari Hamed
- **发表**: 2026-07-02  ·  **类别**: cs.RO, math.OC
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: This paper presents a novel layered planning and control framework based on multi-rate nonlinear model predictive control (MR-NMPC) that enables quadrupedal robots to perform hybrid bipedal locomotion with wall-assisted support in constrained environments. Real-time trajectory optimization for this locomotion presents significant challenges, as the controll…

### 10. HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation

- **arXiv**: [2606.27239v1](https://arxiv.org/abs/2606.27239v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27239v1)
- **作者**: Hongwu Wang, Chenhao Yu, Youhao Hu et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors that require coordinated perception, locomotion, and manipulation. Existing data-collection methods largely rely on robot teleoperation, which is constrained by hardware accessibility, operator expertise, and limited efficiency. Inspired by t…

## 🦾 操控 / 灵巧手 / 抓取 (33 篇)

### 1. From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation

- **arXiv**: [2606.30749v1](https://arxiv.org/abs/2606.30749v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30749v1)
- **作者**: Ying Yuan, Xinyu Liu, Sriram Krishna et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving…

### 2. UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models

- **arXiv**: [2606.31723v1](https://arxiv.org/abs/2606.31723v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31723v1)
- **作者**: Xidong Zhang, Yichi Zhang, Jiaxin Shi et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat…

### 3. OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

- **arXiv**: [2606.31993v1](https://arxiv.org/abs/2606.31993v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31993v1)
- **作者**: Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi et al.
- **发表**: 2026-06-30  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanis…

### 4. VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity

- **arXiv**: [2606.27344v1](https://arxiv.org/abs/2606.27344v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27344v1)
- **作者**: Yuemin Mao, Uksang Yoo, Jean Oh et al.
- **发表**: 2026-06-25  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation depends on contact events that are fast, local, and often visually occluded. Piezoelectric microphones offer a compact and high-bandwidth way to sense these interactions, but the resulting vibro-acoustic signals are difficult to simulate faithfully enough for end-to-end sim-to-real policy learning on dexterous robot hands. We propose…

### 5. Steering Autoregressive Vision-Language-Action Policies via Action Token Intervention

- **arXiv**: [2606.15021v1](https://arxiv.org/abs/2606.15021v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.15021v1)
- **作者**: Jason Chan, Jonathan C. Kao
- **发表**: 2026-06-12  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We present Token Steering (TS), a method for dynamically steering trajectories generated by an autoregressive vision-language-action (VLA) model through direct intervention in the action-token space. TS injects low-dimensional user inputs into the model's native action-token representation, allowing users to influence trajectory generation without modifying…

### 6. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 7. The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection

- **arXiv**: [2607.02322v1](https://arxiv.org/abs/2607.02322v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02322v1)
- **作者**: Jincheng Tang, Yilong Zhu, Zhengyuan Xie et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have shown remarkable promise in generalized robotic manipulation. However, their spatial generalization remains fragile. We argue that simply increasing the number of viewpoints is insufficient. Models often fall into the trap of Shortcut Learning, latching onto spurious correlations (e.g., fixed relative poses between o…

### 8. VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon

- **arXiv**: [2607.01804v1](https://arxiv.org/abs/2607.01804v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.01804v1)
- **作者**: Yi Pan, Miao Pan, Qi Lu et al.
- **发表**: 2026-07-02  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) foundation models have recently achieved strong progress in embodied intelligence. To reduce policy-call frequency while preserving temporal coherence, most generative policies adopt an action chunk mechanism, executing multiple future actions in an open-loop manner under a fixed action horizon. However, this "predict-then-blind…

### 9. WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation

- **arXiv**: [2606.13672v2](https://arxiv.org/abs/2606.13672v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.13672v2)
- **作者**: Arnav Kumar Jain, Yilin Wu, Jesse Farebrother et al.
- **发表**: 2026-06-11  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction. To unlock these downstream capabilities, a WM needs to jointly satisfy three desiderata: $\textit{(i)}$ fidelity (i.e., producing simulated trajectorie…

### 10. YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale

- **arXiv**: [2606.10244v1](https://arxiv.org/abs/2606.10244v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.10244v1)
- **作者**: Takehiko Ohkawa, Jumpei Arima, Yuki Noguchi et al.
- **发表**: 2026-06-08  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 11  ·  **👀 watch**
- **摘要**: We introduce Yielding Universal Bidigital Interface (YUBI), a finger-aligned gripper designed to enable intuitive, ergonomic, and scalable data collection for bimanual dexterous manipulation. While handheld data collection systems such as Universal Manipulation Interface (UMI) enable affordable data collection, their bulky pistol-grip designs can pose ergon…

## 🎓 模仿学习 / 强化学习 (15 篇)

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

### 4. A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity

- **arXiv**: [2607.02005v1](https://arxiv.org/abs/2607.02005v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.02005v1)
- **作者**: Sujan Kumar Dhali, Bhaskar Dasgupta
- **发表**: 2026-07-02  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping. To address this…

### 5. Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints

- **arXiv**: [2606.27509v1](https://arxiv.org/abs/2606.27509v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.27509v1)
- **作者**: Huaiyuan Weng, Huibin Li, Chul Min Yeum
- **发表**: 2026-06-25  ·  **类别**: cs.CV
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: In this study, we develop a Structured framework for Gaussian Splatting (3DGS) with LiDAR integration (Structured-Li-GS). It is a lightweight Gaussian Splatting pipeline that leverages LiDAR-inertial-visual SLAM. Structured-Li-GS achieves high-quality 3D reconstructions with fewer Gaussians by training on accurate, dense, colorized point clouds. Gaussian pr…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. A Synthetic-Driven Vision System for Assembly Step Recognition

- **arXiv**: [2607.00129v1](https://arxiv.org/abs/2607.00129v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00129v1)
- **作者**: Hui Zhang, Xuanang Lei, Rui Wang et al.
- **发表**: 2026-06-30  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Quality control in industrial assembly is essential, and real-time monitoring of the assembly process is crucial for preventing costly defects and ensuring production reliability. Vision-based automated inspection offers a powerful solution for such real-time monitoring. However, due to the specialized industrial components and processes, training these mod…

### 8. SENSE-VAD: Sentient and Semantic Video Anomaly Detection for Autonomous Driving

- **arXiv**: [2606.31875v1](https://arxiv.org/abs/2606.31875v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.31875v1)
- **作者**: Nghia T. Nguyen, Lokman Bekit, Yasin Yilmaz
- **发表**: 2026-06-30  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Autonomous vehicles (AVs) must navigate not only motion-based hazards but also socially complex situations whose danger is constituted by inter-agent relationships rather than movement statistics alone. A child running away from a guardian, a person being carried by another, or a pursuer chasing a pedestrian across a sidewalk are all anomalous in social con…

### 9. TACO: A Test and Check Framework for Robust Pose Graph Optimization

- **arXiv**: [2606.29851v2](https://arxiv.org/abs/2606.29851v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.29851v2)
- **作者**: Emilio Olivastri, Alberto Pretto, Tobias Fischer
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Pose Graph Optimization (PGO) is one of the most widely adopted approaches for solving Simultaneous Localization and Mapping (SLAM) problems. However, PGO approaches are particularly sensitive to outliers, which can substantially degrade the quality of the estimated trajectories. These outliers arise from incorrect place recognition associations caused by p…

### 10. VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM

- **arXiv**: [2606.29494v1](https://arxiv.org/abs/2606.29494v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.29494v1)
- **作者**: Raman Jha, Shuaihang Yuan, Yi Fang
- **发表**: 2026-06-28  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Visual SLAM performance often deteriorates in complex real-world applications. Semantic 3D Gaussian SLAM commonly fuses 2D semantic priors into a persistent 3D map using uniform optimization weights. However, such priors are not equally reliable in online mapping: occlusions, unsupported semantic boundaries, and ambiguous ray geometry can introduce persiste…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (3 篇)

### 1. FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2

- **arXiv**: [2605.25239v1](https://arxiv.org/abs/2605.25239v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2605.25239v1)
- **作者**: Manan Kharwar
- **发表**: 2026-05-24  ·  **类别**: cs.RO, eess.SP
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: We present FusionCore, an open-source ROS 2 sensor fusion package that fuses IMU, wheel encoder odometry, GPS, and Visual SLAM pose into a single 100 Hz odometry stream using a 23-state Unscented Kalman Filter (UKF). The 23rd state is an online estimate of the wheel encoder's systematic yaw rate bias, identified through GPS heading cross-covariance and subt…

### 2. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

### 3. HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction

- **arXiv**: [2411.17982v3](https://arxiv.org/abs/2411.17982v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2411.17982v3)
- **作者**: Wei Zhang, Qing Cheng, David Skuddis et al.
- **发表**: 2024-11-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often trade off between rendering quality and geometry accuracy, our research demonstrates that both can be achieved simultaneously with RGB input alone. The key idea…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. [Preprint] Dynamic Modeling, Gait Synthesis, and Control of a Novel Subsurface Bore Propagator

- **arXiv**: [2607.00569v1](https://arxiv.org/abs/2607.00569v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.00569v1)
- **作者**: Lina van Brügge, Shruti Kotpalliwar, Anton Koval et al.
- **发表**: 2026-07-01  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: In this article, we present dynamic modeling, gait synthesis, and feedback control design for a modular novel subsurface robot, designed for human-free subsurface exploration and excavation. The subsurface propagator design is based on two major aspects: 1) anchor and propel movement like an earthworm and 2) excavation similar to tunnel boring machines. Thi…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation](https://arxiv.org/abs/2606.31836v1) — score 22
2. [Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory](https://arxiv.org/abs/2606.31037v2) — score 19
3. [From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation](https://arxiv.org/abs/2606.30749v1) — score 19

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
