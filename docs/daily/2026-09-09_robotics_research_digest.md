# 机器人研究每日摘要 · 2026-09-09

> 自动生成,共 88 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (3 篇)

### 1. Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving

- **arXiv**: [2609.04070v1](https://arxiv.org/abs/2609.04070v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04070v1)
- **作者**: Ruoyu Yao, Yusen Xie, Qingzhao Liu et al.
- **发表**: 2026-09-03  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground semantic understanding in precise motion exec…

### 2. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 3. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. Towards Generalizable Visually Grounded Exploration of Household Devices

- **arXiv**: [2609.00845v1](https://arxiv.org/abs/2609.00845v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.00845v1)
- **作者**: Linhao Zheng, Zeming Liu, Wangke Chen et al.
- **发表**: 2026-09-01  ·  **类别**: cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent advancements in Vision-Language Models (VLMs) have demonstrated impressive capabilities in static visual recognition and high-level semantic reasoning. However, current embodied exploration paradigms still heavily rely on imitation learning from human-annotated trajectories, which severely limits agents' generalization ability. The key bottleneck of…

### 2. Linguistic Trajectory Encoding for Efficient Long-Horizon Spatial Memory in Embodied Agents

- **arXiv**: [2609.04802v1](https://arxiv.org/abs/2609.04802v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04802v1)
- **作者**: Tianyidan Xie, Shenyi Wang, Qiang Tang et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV, cs.AI
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Embodied agents performing long-horizon tasks require a memory representation in which the state transitions of dynamic objects remain queryable in natural language across hours-to-days observation horizons. Existing systems either drop fine-grained motion (clip-level video-language embeddings), keep it only as raw coordinates (geometric SLAM), or organise…

### 3. HitMem: Hierarchical Temporal 3D Memory with Multi-Modal Context-Aware Retrieval for Dynamic Environments

- **arXiv**: [2609.00950v1](https://arxiv.org/abs/2609.00950v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.00950v1)
- **作者**: Ruijie Tang, Chenye Zou, Guoquan Wu et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Executing long-term tasks in dynamic environments requires embodied agents to maintain robust and adaptive 3D scene representations. However, most existing 3D memory frameworks rely on static world assumptions. When objects are displaced by human activities or unobserved events, agents encounter memory-observation conflicts and often require costly geometri…

### 4. SmoothRL: Online Reinforcement Learning During Asynchronous Execution

- **arXiv**: [2608.29768v1](https://arxiv.org/abs/2608.29768v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29768v1)
- **作者**: Guang Gao, Yuxuan Nong, Baifu Huang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learn…

### 5. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 6. DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments

- **arXiv**: [2609.00619v1](https://arxiv.org/abs/2609.00619v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.00619v1)
- **作者**: Ming Liao, Chao Ye, Jianing Fei et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: In indoor environments, object positions frequently change due to human activities or embodied-agent interactions, causing previously constructed scene graphs to become inconsistent with the current scene. To address this issue, we propose DSG, a dynamic 3D scene graph construction framework that detects object changes and performs spatial relationship reas…

### 7. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 8. LookStep: Efficient Vision-Language Navigation with Linguistic Foresight and Event Driven Memory

- **arXiv**: [2609.02350v2](https://arxiv.org/abs/2609.02350v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02350v2)
- **作者**: Kun-Yang Yu, Yingzhe Li, Hongyu Xu et al.
- **发表**: 2026-09-02  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language Navigation (VLN) requires an embodied agent to follow natural-language instructions in unseen environments. Recent progress has been largely driven by Multimodal Large Language Models (MLLMs). Existing methods follow a next-step action prediction paradigm, supervising only the expert action, which requires a high quantity of data for trainin…

### 9. Monocular Depth Estimation from a Single Image: Progress and Opportunities

- **arXiv**: [2609.01172v1](https://arxiv.org/abs/2609.01172v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01172v1)
- **作者**: Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun et al.
- **发表**: 2026-09-01  ·  **类别**: cs.CV
- **相关性评分**: 3  ·  **📌 info**
- **摘要**: Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing t…

## 🦵 人形 / 足式机器人 (22 篇)

### 1. A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

- **arXiv**: [2609.01518v1](https://arxiv.org/abs/2609.01518v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01518v1)
- **作者**: Duncan Calvert, Luigi Penco, Dexton Anderson et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: There is tremendous value in humanoid robots taking on physically demanding, hazardous, and repetitive work in spaces built for humans. However, a useful robot for these spaces must coordinate locomotion, whole-body motion, perception, contact, and operator supervision. We present a robot-local, runtime-editable behavior authoring and runtime system that ad…

### 2. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 3. FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation

- **arXiv**: [2609.03889v2](https://arxiv.org/abs/2609.03889v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.03889v2)
- **作者**: Yutian Zhang, Siyuan Ma, Liwen Yang et al.
- **发表**: 2026-09-03  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabiliz…

### 4. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 5. Establishing a Dynamic Multimodal HRI Dataset for Engagement Analysis with a Humanoid Robot

- **arXiv**: [2609.03255v1](https://arxiv.org/abs/2609.03255v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.03255v1)
- **作者**: Buwan Kim, Wonse Jo
- **发表**: 2026-09-03  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: This paper presents an experimental design for constructing a multimodal dataset to analyze user engagement in human-robot interaction (HRI). Prior studies have mainly relied on observable behavioral cues, with limited frameworks integrating physiological signals. We therefore propose a structured data-collection protocol to build a multimodal dataset that…

### 6. LAC: Linear and Angular Compliance for Humanoid Whole-body Control

- **arXiv**: [2608.25405v1](https://arxiv.org/abs/2608.25405v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25405v1)
- **作者**: Yang Liu, Zhongkai Gu, Wei Zhu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches ap…

### 7. Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction

- **arXiv**: [2609.05361v1](https://arxiv.org/abs/2609.05361v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05361v1)
- **作者**: Thang Tran Viet, Thanh Nguyen Canh, Huy Uong Gia et al.
- **发表**: 2026-09-04  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechan…

### 8. Humanoid Safe Stop via Learned Stoppability Value

- **arXiv**: [2609.02358v1](https://arxiv.org/abs/2609.02358v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02358v1)
- **作者**: Junfeng Long, Pieter Abbeel, Koushil Sreenath et al.
- **发表**: 2026-09-02  ·  **类别**: cs.RO, cs.LG, eess.SY
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Humanoid robots responding to emergency stop commands typically execute a fixed maneuver, without reasoning about whether a safe stop is actually feasible from the current state. We cast emergency stopping as a reach-avoid problem and propose Safe-Stop, a task-agnostic framework that pairs a learned stop policy with learned stoppability estimators. The esti…

### 9. Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence

- **arXiv**: [2609.02134v1](https://arxiv.org/abs/2609.02134v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02134v1)
- **作者**: Hanyang Cao, Yuetong Fang, Taesoo Kwon et al.
- **发表**: 2026-09-02  ·  **类别**: cs.RO, cs.GR
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Humanoid learning increasingly relies on transforming vast and diverse human motion data into high-quality robot reference trajectories. However, retargeting human motion to humanoid robots is challenging due to substantial differences in morphology, degrees of freedom, joint ranges, and kinematic constraints between humans and robots. Existing retargeting…

### 10. KYON: Semi-Modular Wheel-Legged Quadruped With Agile Bimanual Capability

- **arXiv**: [2606.30243v2](https://arxiv.org/abs/2606.30243v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30243v2)
- **作者**: Luca Rossini, Arturo Laurenzi, Francesco Ruscelli et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents KYON, a hybrid wheel-legged quadruped robot equipped with a bimanual upper body for loco-manipulation tasks. The platform features a semi-modular design with a reconfigurable lower legs, enabling both wheeled and legged locomotion depending on the environment. A design approach that places actuators in the base and uses transmission mech…

## 🦾 操控 / 灵巧手 / 抓取 (33 篇)

### 1. Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds

- **arXiv**: [2609.01453v1](https://arxiv.org/abs/2609.01453v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01453v1)
- **作者**: Clinton Enwerem, John S. Baras, Calin Belta
- **发表**: 2026-09-01  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 20  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation policies learned by imitation are typically evaluated for robustness to variation in scenes, objects, or instructions, but their performance across task execution speeds is less often examined. This leaves open how much temporal robustness a learner retains relative to the expert it imitates. We compare an expert and learner under the…

### 2. RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?

- **arXiv**: [2609.05324v1](https://arxiv.org/abs/2609.05324v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05324v1)
- **作者**: Zhenxuan Fan, Bo Zhang, Yutong Lin et al.
- **发表**: 2026-09-04  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation. However, existing datasets and benchmarks mainly evaluate task completion under predefined settings, offering limited insight into model reasoning under increasing spatial and procedural complexity. We introduce \textbf{RoboSPA} (\textbf{Robo}t \t…

### 3. Motus2: A Self-Evolving General World Model for Dexterous Manipulation

- **arXiv**: [2608.30237v1](https://arxiv.org/abs/2608.30237v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30237v1)
- **作者**: Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-…

### 4. LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories

- **arXiv**: [2608.18618v1](https://arxiv.org/abs/2608.18618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18618v1)
- **作者**: Zhipeng Tang, Sihang Chen, Sha Zhang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: Autonomous laboratories hold great promise for accelerating scientific discovery. To achieve this vision, robots are supposed to dexterously manipulate diverse labware and instruments and execute long-horizon, state-dependent experimental procedures. Yet existing benchmarks do not jointly capture dexterous hand use, real-world laboratory interactions, and m…

### 5. ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation

- **arXiv**: [2609.02546v1](https://arxiv.org/abs/2609.02546v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.02546v1)
- **作者**: Mi Yan, Wenhao Zhang, Zhiqi Zhang et al.
- **发表**: 2026-09-02  ·  **类别**: cs.RO
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Zero-shot generalization to unseen embodiments is important for generalizable vision-language-action (VLA) models as robot hardware evolves and task-specific data collection remains costly. However, a systematic understanding of this problem remains limited, in part because the literature lacks a unified zero-shot transfer definition and controlled evaluati…

### 6. One Demonstration, Many Objects: Generalizing Manipulation via Local Contact Geometry

- **arXiv**: [2609.01938v2](https://arxiv.org/abs/2609.01938v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01938v2)
- **作者**: Satvik Sharma, Samrat Sahoo, Huang Huang et al.
- **发表**: 2026-09-01  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: Dexterous manipulation with multi-fingered robot hands promises human-level dexterity, but collecting large-scale dexterous robot hand data remains difficult. Learning from human demonstrations has emerged as a scalable alternative to robot teleoperation, providing strong priors on object interaction and contact strategies. Recent sim-to-real RL methods inc…

### 7. A Tendon-Driven Five-Fingered Hand with Distributed Tactile Perception for Dexterous Manipulation

- **arXiv**: [2608.25547v1](https://arxiv.org/abs/2608.25547v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25547v1)
- **作者**: Huayang Chen, Longhui Qin
- **发表**: 2026-08-26  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: To apply the techniques of embodied artificial intelligence to human-oid robots for complex manipulations, dexterous robotic hands are indispensable, which are restricted by the dexterity and tactile perception capability. In this work, we proposed a novel design of tendon-driven five-fingered hand with dis-tributed tactile perception. With a soft-rigid-hyb…

### 8. GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation

- **arXiv**: [2609.04193v1](https://arxiv.org/abs/2609.04193v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04193v1)
- **作者**: Yupeng Zheng, Xiang Li, Songen Gu et al.
- **发表**: 2026-09-03  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Vision-language pre-training and predictive world modeling provide robot policies with rich semantic and dynamic visual features, but their native action and visual-prediction objectives may omit critical physical and task structure while retaining control-irrelevant visual redundancy. We call this mismatch between visual richness and control utility the ac…

### 9. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 10. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

## 🎓 模仿学习 / 强化学习 (15 篇)

### 1. Sim2Signal: Sim-to-Real Benchmarks for Traffic Signal Control

- **arXiv**: [2609.01676v1](https://arxiv.org/abs/2609.01676v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01676v1)
- **作者**: Ferdous Al Rafi, Susrik Mukherjee, Latika Liladhar Dekate et al.
- **发表**: 2026-09-01  ·  **类别**: cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Reinforcement learning achieves strong traffic signal control performance in simulation, yet policies trained in simulators often fail once deployed in the real world, a failure known as the Sim-to-Real gap. When RL is applied to traffic signal control, this gap arises from several sources: sensing, action execution, traffic dynamics, and the control object…

### 2. Provably Safe Sim-to-Real Transfer

- **arXiv**: [2609.01418v1](https://arxiv.org/abs/2609.01418v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.01418v1)
- **作者**: Tingting Ni, Maryam Kamgarpour
- **发表**: 2026-09-01  ·  **类别**: cs.LG, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be…

### 3. A Low-Cost, Open Platform for End-to-End Autonomous Driving on a Miniature Ackermann Vehicle

- **arXiv**: [2609.04147v1](https://arxiv.org/abs/2609.04147v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04147v1)
- **作者**: Gustavo Claudio Karl Couto, Eric Aislan Antonelo, Gabriel George Zipperer
- **发表**: 2026-09-03  ·  **类别**: cs.LG, cs.AI, cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents a low-cost, open experimental platform for research in end-to-end autonomous driving with miniature Ackermann vehicles. The platform combines a physical vehicle, a printed urban track, data collection tools, trajectory registration, and a Webots digital twin, enabling controlled experiments that connect simulation-based autonomous-drivin…

### 4. Long-Horizon Consistent and Interaction-Aware World Models for Multi-Style End-to-End Driving

- **arXiv**: [2609.03225v1](https://arxiv.org/abs/2609.03225v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.03225v1)
- **作者**: Yuxuan Han, Kunyuan Wu, Liyunong Yang et al.
- **发表**: 2026-09-03  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: End-to-end autonomous driving has increasingly adopted world model-based reinforcement learning frameworks to improve learning efficiency through \textit{imagined rollouts}. However, existing world models suffer from three key limitations: temporal inconsistency in long-horizon imagined rollouts, inadequate modeling of ego-environment interactions, and limi…

### 5. Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies

- **arXiv**: [2603.02783v1](https://arxiv.org/abs/2603.02783v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.02783v1)
- **作者**: Mattes Kraus, Jonas Kuckling
- **发表**: 2026-03-03  ·  **类别**: cs.RO, cs.LG, cs.MA
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human de…

### 6. End-to-End Deep Imitation Learning: Robot Soccer Case Study

- **arXiv**: [1807.09205v1](https://arxiv.org/abs/1807.09205v1)  ·  **PDF**: [link](https://arxiv.org/pdf/1807.09205v1)
- **作者**: Okan Aşık, Binnur Görer, H. Levent Akın
- **发表**: 2018-06-28  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: In imitation learning, behavior learning is generally done using the features extracted from the demonstration data. Recent deep learning algorithms enable the development of machine learning methods that can get high dimensional data as an input. In this work, we use imitation learning to teach the robot to dribble the ball to the goal. We use B-Human robo…

### 7. Praxist: From Experimental Artifacts to Solution Lineages

- **arXiv**: [2608.25955v1](https://arxiv.org/abs/2608.25955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25955v1)
- **作者**: Jin Li, Ahmed Murtadha, Zhiyu Wang et al.
- **发表**: 2026-08-26  ·  **类别**: cs.MA, cs.SE
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-co…

### 8. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 9. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 10. Unblur-SLAM: Dense Neural SLAM for Blurry Inputs

- **arXiv**: [2603.26810v1](https://arxiv.org/abs/2603.26810v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2603.26810v1)
- **作者**: Qi Zhang, Denis Rozumny, Francesco Girlanda et al.
- **发表**: 2026-03-26  ·  **类别**: cs.CV, eess.IV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in…

## 🗺️ SLAM / 视觉里程计 / 3D 感知 (5 篇)

### 1. BLASt3R: Bundle Adjustment of Any Image Set with Multi-View Matching and Monocular Priors

- **arXiv**: [2609.05210v1](https://arxiv.org/abs/2609.05210v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.05210v1)
- **作者**: Vincent Leroy, Philippe Weinzaepfel, Lojze Zust et al.
- **发表**: 2026-09-04  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Recent hybrid Structure-from-Motion (SfM) systems combine the robustness of feed-forward 3D reconstruction with the accuracy of traditional bundle adjustment (BA) with pixel matching. They are usually the best performing methods however their scalability and usability remains limited since estimating dense correspondences between views is prohibitively cost…

### 2. Desc++: Efficient Descriptor Enhancement for Data Association in Existing Visual SLAM Systems

- **arXiv**: [2607.11099v1](https://arxiv.org/abs/2607.11099v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.11099v1)
- **作者**: Ting-Wei Ou, Huang-Ting Lin, Kuu-Young Young
- **发表**: 2026-07-13  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 3. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 4. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: With the growing demand for robotics, autonomous drones, and wearable extended reality systems, the deployment of Visual SLAM on embedded devices remains challenging. Tracking must sustain high frame rates while preserving compute resources for map extension and maintenance. This paper presents GLidE-SLAM, a monocular hybrid indirect-direct framework that a…

### 5. Geodesic Flow Matching for Denoising High-Dimensional Structured Representations

- **arXiv**: [2606.00248v1](https://arxiv.org/abs/2606.00248v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.00248v1)
- **作者**: Karim Habashy, Chris Eliasmith
- **发表**: 2026-05-29  ·  **类别**: cs.AI
- **相关性评分**: 2  ·  **📌 info**
- **摘要**: Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclide…

## 🧪 仿真 / Sim2Real (1 篇)

### 1. A Sim-to-Real Study of Surface-Code Decoder Benchmarking

- **arXiv**: [2609.04557v1](https://arxiv.org/abs/2609.04557v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2609.04557v1)
- **作者**: Shay J. Manor, Leila S. Erhili, Yassine Jebbouri
- **发表**: 2026-09-03  ·  **类别**: quant-ph, cs.LG
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Quantum error-correction decoders are typically benchmarked against synthetic circuit-level noise, under the assumption that a decoder's ranking under such noise transfers to hardware and improves as the noise model becomes more realistic. The Willow processor, the first to operate below the surface-code threshold, allows us to test this assumption. We rank…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](https://arxiv.org/abs/2609.01453v1) — score 20
2. [RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?](https://arxiv.org/abs/2609.05324v1) — score 19
3. [A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots](https://arxiv.org/abs/2609.01518v1) — score 18

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
