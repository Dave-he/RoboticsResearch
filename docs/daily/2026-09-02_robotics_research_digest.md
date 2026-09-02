# 机器人研究每日摘要 · 2026-09-02

> 自动生成,共 88 篇命中论文。

## 🧠 视觉-语言-动作模型 (VLA) (6 篇)

### 1. Training-Free Action Correction for VLA Model Failures via Language Feedback

- **arXiv**: [2608.29967v1](https://arxiv.org/abs/2608.29967v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29967v1)
- **作者**: Owen Kwon, Pablo Ortega-Kral, Arthur Bucker et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Vision-Language-Action (VLA) models demonstrate strong semantic understanding yet exhibit systematic failures during deployment. The conditions under which these failures occur, and whether they can be corrected without retraining, remain poorly understood. In this paper, we take steps toward addressing this gap. We present CorrectVLA, a framework that tran…

### 2. DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting

- **arXiv**: [2608.29749v1](https://arxiv.org/abs/2608.29749v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29749v1)
- **作者**: Yuxuan Gao, Shiqi Zhang, Yedong Shen et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: Conventional flow-based vision-language-action (VLA) models support expressive continuous action generation but rely on multi-step refinement to produce each action chunk, increasing latency in online robot control. To address this issue, we introduce DriftingVLA, a native one-step VLA that generates a complete action chunk with a single action-expert forwa…

### 3. The Embodiment Gap in Robot Foundation Models

- **arXiv**: [2608.18433v1](https://arxiv.org/abs/2608.18433v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18433v1)
- **作者**: Yukiyasu Domae, Keisuke Shirai, Hanbit Oh et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. In robotics, however, a model can generalize while work still remains before it can run on a robot with a particular body. The work required differs acros…

### 4. PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies

- **arXiv**: [2608.30378v1](https://arxiv.org/abs/2608.30378v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30378v1)
- **作者**: Botong Zhao, Fang Yu, Tim et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Direct vision-language-action policies generate continuous robot actions efficiently, but standard behavior cloning leaves two complementary gaps: their representations are not explicitly required to describe how the scene evolves over multiple time scales, and deployment trajectories of unequal quality are often reused without separating useful dynamics fr…

### 5. Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving

- **arXiv**: [2608.30144v1](https://arxiv.org/abs/2608.30144v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30144v1)
- **作者**: Tongfei Guo, Lili Su
- **发表**: 2026-08-31  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Vision-Language-Action (VLA) models are reshaping autonomous driving (AD) by unifying perception, reasoning, and control through language, enabling semantic grounding, interpretable decisions, and better long-tail generalization. But language is expensive onboard: latency and memory budgets are tight, and autoregressive decoding is inherently sequential. Th…

### 6. Action Chunk Scheduling for Batched Robot Policy Serving

- **arXiv**: [2608.00337v1](https://arxiv.org/abs/2608.00337v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.00337v1)
- **作者**: Rohan Bansal, David He, Nadun Ranawaka Arachchige et al.
- **发表**: 2026-07-31  ·  **类别**: cs.RO
- **相关性评分**: 4  ·  **📌 info**
- **摘要**: Deploying robot foundation models at scale is the next step towards realizing the potential of general-purpose robots. However, Vision-Language-Action (VLA) and other foundation models are computationally demanding, and on-device compute is constrained by power and space. In this paper, we introduce the problem of serving a robot policy to multiple robots f…

## 🌐 具身智能 / 机器人基础模型 (9 篇)

### 1. SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding

- **arXiv**: [2608.30451v1](https://arxiv.org/abs/2608.30451v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30451v1)
- **作者**: Yi Zhang, Yi Wang, Yueting Wu et al.
- **发表**: 2026-08-31  ·  **类别**: cs.CV
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Image-based 3D visual grounding is critical for embodied agents, yet existing benchmarks suffer from loose text-observation alignment and neglect temporal ordering. We introduce SeqAlign3DVG, a novel benchmark dedicated to temporally ordered and strictly observation-aligned image-based 3D visual grounding. Unlike prior works using order-agnostic views or gl…

### 2. SmoothRL: Online Reinforcement Learning During Asynchronous Execution

- **arXiv**: [2608.29768v1](https://arxiv.org/abs/2608.29768v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29768v1)
- **作者**: Guang Gao, Yuxuan Nong, Baifu Huang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Deploying robot policies in the physical world requires satisfying two fundamental desiderata: reliability and smooth real-time execution. However, deploying state-of-the-art generalist models presents challenges on both fronts. Achieving the precision and robustness required for real-world deployment necessitates sample-efficient online reinforcement learn…

### 3. PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents

- **arXiv**: [2608.30760v1](https://arxiv.org/abs/2608.30760v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30760v1)
- **作者**: Ziyi Bai, Siqi Li, Tinglei Huang et al.
- **发表**: 2026-08-31  ·  **类别**: cs.LG
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans. However, building agents that can continually improve through interaction and rapidly adapt to their environments remains challenging. Summing up experience from past interacti…

### 4. MCN-SLAM: Multi-Agent Collaborative Neural SLAM with Hybrid Implicit Neural Scene Representation

- **arXiv**: [2506.18678v2](https://arxiv.org/abs/2506.18678v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2506.18678v2)
- **作者**: Tianchen Deng, Guole Shen, Xun Chen et al.
- **发表**: 2025-06-23  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Neural implicit scene representations have recently shown promising results in dense visual SLAM. However, existing implicit SLAM algorithms are constrained to single-agent scenarios, and fall difficulties in large-scale scenes and long sequences. Existing NeRF-based multi-agent SLAM frameworks cannot meet the constraints of communication bandwidth. To this…

### 5. Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction

- **arXiv**: [2608.09146v1](https://arxiv.org/abs/2608.09146v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.09146v1)
- **作者**: Tianchen Deng, Chongdi Wang, Nailin Wang et al.
- **发表**: 2026-08-10  ·  **类别**: cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Neural Radiance Fields (NeRF)-based SLAM has demonstrated impressive results in small-scale scene reconstruction, yet scaling these methods to extensive, complex environments remains challenging due to catastrophic forgetting and accumulated trajectory drift. This paper presents a robust, large-scale neural SLAM system featuring a multi-submap architecture…

### 6. Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory

- **arXiv**: [2608.29910v1](https://arxiv.org/abs/2608.29910v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29910v1)
- **作者**: Runjia Qian, Zile Wang, Jihai Zhang et al.
- **发表**: 2026-08-30  ·  **类别**: cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consi…

### 7. CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action

- **arXiv**: [2608.27797v1](https://arxiv.org/abs/2608.27797v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27797v1)
- **作者**: Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi
- **发表**: 2026-08-28  ·  **类别**: cs.AI, cs.CL, cs.FL
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Natural-language tasking of embodied agents is rarely just goal specification: users also impose constraints that must persist while the world changes. Code-generating LLM agents can produce plausible behaviors for such instructions, but their free-form programs provide no stable object to verify, compose with new constraints, or repair from a failing trace…

### 8. Embodied Scene Rearrangement Planning

- **arXiv**: [2608.27371v1](https://arxiv.org/abs/2608.27371v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27371v1)
- **作者**: Canzhi Chen, Zan Wang, Siqi Zhu et al.
- **发表**: 2026-08-27  ·  **类别**: cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: This paper introduces Embodied Scene Rearrangement Planning (ESRP), a novel task requiring embodied agents to rearrange furniture in 3D scenes to match a target configuration using only egocentric observations and a top-down target layout. Unlike prior rearrangement tasks, ESRP precludes global state access and introduces mutual object occlusions, reflectin…

### 9. 4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation

- **arXiv**: [2608.26947v1](https://arxiv.org/abs/2608.26947v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.26947v1)
- **作者**: Zehao Qi, Haochen Luo, Jia-Wang Bian et al.
- **发表**: 2026-08-27  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Embodied agents need environments that are visually diverse, physically interactive, and changing over time. Procedural simulators can generate large interactive scene collections, and recent 4D generators produce compelling visual dynamics. Combining these properties in one environment, however, still demands extensive manual effort, and the result is rare…

## 🦵 人形 / 足式机器人 (25 篇)

### 1. Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters

- **arXiv**: [2608.28090v1](https://arxiv.org/abs/2608.28090v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.28090v1)
- **作者**: Kango Yanagida, Kazuki Miyazawa, Takato Horii
- **发表**: 2026-08-28  ·  **类别**: cs.RO
- **相关性评分**: 19  ·  **🔥 read_now**
- **摘要**: Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor…

### 2. Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds

- **arXiv**: [2607.18135v1](https://arxiv.org/abs/2607.18135v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.18135v1)
- **作者**: Jordan Dowdy, Jean Chagas Vaz
- **发表**: 2026-07-20  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 16  ·  **🔥 read_now**
- **摘要**: Learning-based approaches to locomotion have risen in popularity in recent years, showing the capability for complex legged locomotion and whole-body control. Reinforcement learning (RL), the primary learning-based approach for locomotion, often utilizes a high-performance simulation tool, providing a controlled and efficient training and development enviro…

### 3. LAC: Linear and Angular Compliance for Humanoid Whole-body Control

- **arXiv**: [2608.25405v1](https://arxiv.org/abs/2608.25405v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25405v1)
- **作者**: Yang Liu, Zhongkai Gu, Wei Zhu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Real-world humanoid tasks involve physical interaction with objects and humans, yet current controllers either reject external forces as disturbances or restrict compliance to limited body links while ignoring angular effects. We present LAC, a general whole-body controller that simultaneously realizes commanded Linear and Angular Compliance for wrenches ap…

### 4. The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments

- **arXiv**: [2606.30900v2](https://arxiv.org/abs/2606.30900v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30900v2)
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone an…

### 5. RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation

- **arXiv**: [2608.03387v2](https://arxiv.org/abs/2608.03387v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.03387v2)
- **作者**: Shuliang He, Shuai Wang, Bo Yue et al.
- **发表**: 2026-08-04  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual…

### 6. Blind Dexterity: Whole-Body Humanoid Manipulation via Pure Proprioception

- **arXiv**: [2608.29487v1](https://arxiv.org/abs/2608.29487v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29487v1)
- **作者**: Aditya Bhatt, Oleg Kaidanov, Puze Liu et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 10  ·  **👀 watch**
- **摘要**: We present blind, whole-body manipulation skills on a Unitree G1 humanoid using only onboard proprioception, without cameras, markers, force-torque, or tactile sensors. Despite this minimal sensing, the trained policies exhibit surprising capability across qualitatively different tasks: push-resilient bipedal walking without IMU feedback, active soccer ball…

### 7. Learning Agile Perceptive Traversal of Sparse 3D Structures for Humanoids

- **arXiv**: [2608.29769v1](https://arxiv.org/abs/2608.29769v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29769v1)
- **作者**: Efe Ongan, Chong Zhang, Boyang Sun et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Traversing sparse 3D structures requires humanoid robots to perceive thin, overhanging geometry while executing agile, accurate whole-body motions. We study this problem through monkey-bar traversal, where the robot must jump to the structure, traverse it through sparse bar interactions, and land safely. For this task, we present a reinforcement-learning-ba…

### 8. EgoNav: Bridging Learned Waypoints and Geometry-Aware Local Control for Robust Indoor Navigation

- **arXiv**: [2608.25642v1](https://arxiv.org/abs/2608.25642v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25642v1)
- **作者**: Jing Wang, Shiqi Zhao, Hairong Qu et al.
- **发表**: 2026-08-26  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Image-goal navigation using lightweight topological maps is a practical paradigm for indoor robot deployment: the map requires only geotagged images, and localization relies on visual matching rather than precise pose estimation. However, learned waypoint predictors can produce targets that violate geometric constraints or deviate from the global path. Exec…

### 9. KYON: Semi-Modular Wheel-Legged Quadruped With Agile Bimanual Capability

- **arXiv**: [2606.30243v2](https://arxiv.org/abs/2606.30243v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2606.30243v2)
- **作者**: Luca Rossini, Arturo Laurenzi, Francesco Ruscelli et al.
- **发表**: 2026-06-29  ·  **类别**: cs.RO
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: This paper presents KYON, a hybrid wheel-legged quadruped robot equipped with a bimanual upper body for loco-manipulation tasks. The platform features a semi-modular design with a reconfigurable lower legs, enabling both wheeled and legged locomotion depending on the environment. A design approach that places actuators in the base and uses transmission mech…

### 10. PAMoR: Parameterized Affective Motion Generation in Real Time for Humanoid Robots

- **arXiv**: [2608.28213v1](https://arxiv.org/abs/2608.28213v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.28213v1)
- **作者**: Yan Pan, Lingfan Bao, Tianhu Peng et al.
- **发表**: 2026-08-28  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: People read a humanoid robot's motion in social settings not only for the action performed but for the affect conveyed. Motion carrying that affect has so far been generated for human avatars, where style is taken from a reference clip or an emotion word, neither of which can be quantitatively parameterized. We present PAMoR, which turns affect into a measu…

## 🦾 操控 / 灵巧手 / 抓取 (28 篇)

### 1. Motus2: A Self-Evolving General World Model for Dexterous Manipulation

- **arXiv**: [2608.30237v1](https://arxiv.org/abs/2608.30237v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30237v1)
- **作者**: Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO, cs.AI, cs.CV
- **相关性评分**: 21  ·  **🔥 read_now**
- **摘要**: General embodied agents should perceive, predict, act, evaluate, and improve within a unified system. World models have shown great promise in building such agents, yet existing models typically append an action output head to a world simulator, without coupling them into a closed decision-and-learning loop for policy improvement. We present Motus2, a self-…

### 2. LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories

- **arXiv**: [2608.18618v1](https://arxiv.org/abs/2608.18618v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.18618v1)
- **作者**: Zhipeng Tang, Sihang Chen, Sha Zhang et al.
- **发表**: 2026-08-19  ·  **类别**: cs.RO
- **相关性评分**: 18  ·  **🔥 read_now**
- **摘要**: Autonomous laboratories hold great promise for accelerating scientific discovery. To achieve this vision, robots are supposed to dexterously manipulate diverse labware and instruments and execute long-horizon, state-dependent experimental procedures. Yet existing benchmarks do not jointly capture dexterous hand use, real-world laboratory interactions, and m…

### 3. A Tendon-Driven Five-Fingered Hand with Distributed Tactile Perception for Dexterous Manipulation

- **arXiv**: [2608.25547v1](https://arxiv.org/abs/2608.25547v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25547v1)
- **作者**: Huayang Chen, Longhui Qin
- **发表**: 2026-08-26  ·  **类别**: cs.RO, cs.AI
- **相关性评分**: 17  ·  **🔥 read_now**
- **摘要**: To apply the techniques of embodied artificial intelligence to human-oid robots for complex manipulations, dexterous robotic hands are indispensable, which are restricted by the dexterity and tactile perception capability. In this work, we proposed a novel design of tendon-driven five-fingered hand with dis-tributed tactile perception. With a soft-rigid-hyb…

### 4. Learning to infer and manipulate through distributed whole-arm interaction in a soft robot

- **arXiv**: [2608.30773v1](https://arxiv.org/abs/2608.30773v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30773v1)
- **作者**: Chuhan Zhang, Ebrahim Shahabi, Kseniia Khomenko et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO
- **相关性评分**: 15  ·  **🔥 read_now**
- **摘要**: In animals such as elephants and octopuses, acquiring non-visual information about an object and physically engaging with it are inseparable processes mediated by rich, large-area interactions between compliant appendages and the environment. Soft robots provide a natural platform for translating this principle into engineered systems. Yet current robotic i…

### 5. $τ_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation

- **arXiv**: [2608.16885v1](https://arxiv.org/abs/2608.16885v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.16885v1)
- **作者**: Xiaowei Cai, Yunuo Cai, Bingao Chen et al.
- **发表**: 2026-08-17  ·  **类别**: cs.RO
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices. We introduce $τ_…

### 6. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration

- **arXiv**: [2105.06411v2](https://arxiv.org/abs/2105.06411v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2105.06411v2)
- **作者**: Edward Johns
- **发表**: 2021-05-13  ·  **类别**: cs.RO, cs.LG
- **相关性评分**: 14  ·  **🔥 read_now**
- **摘要**: We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the p…

### 7. Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning

- **arXiv**: [2608.28578v1](https://arxiv.org/abs/2608.28578v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.28578v1)
- **作者**: Nan Wang, Mohit Yadav, Jonathan Wulff et al.
- **发表**: 2026-08-28  ·  **类别**: cs.RO, cs.AI, cs.LG
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through…

### 8. GhostTac: Manipulating Tactile Sensors without Physical Contact

- **arXiv**: [2608.20817v3](https://arxiv.org/abs/2608.20817v3)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.20817v3)
- **作者**: Kun Wang, Xuancun Lu, Ruochen Zhou et al.
- **发表**: 2026-08-21  ·  **类别**: cs.CR, cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: Tactile sensors are integral components of modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. Despite their importance, the physical-layer security of tactile sensors has received little attention in prior work. In this paper, we present GhostTac, to the best of our knowledge, the first c…

### 9. MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation

- **arXiv**: [2607.17970v1](https://arxiv.org/abs/2607.17970v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17970v1)
- **作者**: Kento Kawaharazuka, Yoshiki Obinata, Hirokazu Ishida et al.
- **发表**: 2026-07-20  ·  **类别**: cs.RO
- **相关性评分**: 13  ·  **🔥 read_now**
- **摘要**: The global competition for developing robotic foundation models is intensifying. Among the data collection systems used for dual-arm robots, ALOHA is representative of being low-cost and open-source, and is widely adopted by researchers as a de facto standard. However, due to its limited ability to generate high forces and speeds, it is difficult to handle…

### 10. Temporal Forcing: 4D Representation Alignment for Vision-Language-Action Models

- **arXiv**: [2608.30643v1](https://arxiv.org/abs/2608.30643v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30643v1)
- **作者**: Xingyu Ding, Yuzhong Zhao, Chunhai Zhao et al.
- **发表**: 2026-08-31  ·  **类别**: cs.RO
- **相关性评分**: 12  ·  **🔥 read_now**
- **摘要**: Recent vision-language-action (VLA) methods improve manipulation performance by aligning their representations with 3D scene geometry. However, these methods often struggle with long-horizon manipulation and observation aliasing between visually similar states due to a lack of temporal information: the 3D scene geometry captures only the current state, rath…

## 🎓 模仿学习 / 强化学习 (14 篇)

### 1. Praxist: From Experimental Artifacts to Solution Lineages

- **arXiv**: [2608.25955v1](https://arxiv.org/abs/2608.25955v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.25955v1)
- **作者**: Jin Li, Ahmed Murtadha, Zhiyu Wang et al.
- **发表**: 2026-08-26  ·  **类别**: cs.MA, cs.SE
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Autonomous R\&D agents now write, run, and improve executable artifacts under automated evaluation---but largely as laboratory instruments: shown on curated benchmarks, with gains that are hard to trace to a cause and costs well above what sustained engineering practice absorbs. The limitation is structural. Most systems treat each attempt as nearly self-co…

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

### 4. RIPE++: Reinforced Keypoint Learning from Positive Pairs Only

- **arXiv**: [2608.19693v1](https://arxiv.org/abs/2608.19693v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.19693v1)
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **发表**: 2026-08-20  ·  **类别**: cs.CV, cs.LG
- **相关性评分**: 7  ·  **👀 watch**
- **摘要**: Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. R…

### 5. GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM

- **arXiv**: [2607.07452v1](https://arxiv.org/abs/2607.07452v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.07452v1)
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang et al.
- **发表**: 2026-07-08  ·  **类别**: cs.RO
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoida…

### 6. Neural Multivariate Regression: Qualitative Insights from the Unconstrained Feature Model

- **arXiv**: [2505.09308v2](https://arxiv.org/abs/2505.09308v2)  ·  **PDF**: [link](https://arxiv.org/pdf/2505.09308v2)
- **作者**: George Andriopoulos, Soyuj Jung Basnet, Juan Guevara et al.
- **发表**: 2025-05-14  ·  **类别**: cs.LG
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: The Unconstrained Feature Model (UFM) is a mathematical framework that enables closed-form approximations for minimal training loss and related performance measures in deep neural networks (DNNs). This paper leverages the UFM to provide qualitative insights into neural multivariate regression, a critical task in imitation learning, robotics, and reinforceme…

### 7. Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

- **arXiv**: [2608.30690v1](https://arxiv.org/abs/2608.30690v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.30690v1)
- **作者**: Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- **发表**: 2026-08-31  ·  **类别**: cs.CV, cs.RO
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intend…

### 8. Should I Use This Synthetic Dataset for Training? How to Test with Minimal Real Data

- **arXiv**: [2608.27996v1](https://arxiv.org/abs/2608.27996v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27996v1)
- **作者**: Zhenyu Tao, Wei Xu, Xiaohu You et al.
- **发表**: 2026-08-28  ·  **类别**: cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Digital twins (DTs) and learned world models are increasingly used to generate synthetic data that augment the scarce real datasets available for training artificial intelligence (AI) models in engineering systems. Owing to the inevitable simulation-to-reality (sim-to-real) gap, however, augmentation may fail to improve the performance of the trained model…

### 9. Low-Altitude Fluid Antenna Network with Multi-Agent Reinforcement Learning

- **arXiv**: [2608.27909v1](https://arxiv.org/abs/2608.27909v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.27909v1)
- **作者**: Tong Zhang, Yanfei Su, Shuai Wang et al.
- **发表**: 2026-08-28  ·  **类别**: cs.IT, cs.AI
- **相关性评分**: 5  ·  **📌 info**
- **摘要**: Low-altitude wireless networks (LAWNs) integrate terrestrial and aerial platforms to provide ubiquitous communication, sensing, and localization services for unmanned aerial vehicles (UAVs) and electric vertical takeoff and landing (eVTOL) aircraft. However, dynamic air-ground and air-air channels, abrupt blockages, and heterogeneous interference hinder the…

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
- **相关性评分**: 9  ·  **👀 watch**
- **摘要**: Reliable visual data association is fundamental to visual SLAM (V-SLAM), as it directly determines the quality of the camera pose estimation and map consistency. However, the handcrafted descriptors used by most mature real-time systems degrade under illumination and viewpoint changes, while learning-based front-ends that address this weakness typically req…

### 2. DROID-ANCHOR: Odometry-Anchored Recurrent Metric Depth Estimation

- **arXiv**: [2607.17058v1](https://arxiv.org/abs/2607.17058v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.17058v1)
- **作者**: Yuxuan Chen, Brook Du
- **发表**: 2026-07-19  ·  **类别**: cs.RO, cs.CV
- **相关性评分**: 6  ·  **👀 watch**
- **摘要**: Precise metric depth estimation is fundamental for autonomous robot navigation, yet monocular systems inherently suffer from scale ambiguity and scale drift. While recent recurrent flow-based SLAM systems have demonstrated state-of-the-art robustness, they remain scale-ambiguous. In this paper, we propose Metric-DROID, an end-to-end recurrent architecture t…

### 3. GLidE-SLAM: GL-Accelerated Indirect-Direct Embedded SLAM

- **arXiv**: [2607.16897v1](https://arxiv.org/abs/2607.16897v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2607.16897v1)
- **作者**: Carlos A. Pinheiro de Sousa, Heiko Hamann, Oliver Deussen
- **发表**: 2026-07-18  ·  **类别**: cs.RO
- **相关性评分**: 2  ·  **📌 info**
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

## 🧪 仿真 / Sim2Real (1 篇)

### 1. Task-Relevant Feature-Dynamics Fidelity Enables Zero-Shot Sim-to-Real Transfer for Robotic Ultrasound Scanning

- **arXiv**: [2608.29516v1](https://arxiv.org/abs/2608.29516v1)  ·  **PDF**: [link](https://arxiv.org/pdf/2608.29516v1)
- **作者**: Yizhao Qian, Jiayuan Luo, Wanyi Zhu et al.
- **发表**: 2026-08-30  ·  **类别**: cs.RO
- **相关性评分**: 8  ·  **👀 watch**
- **摘要**: Robotic ultrasound policies operating directly on B-mode images require extensive interaction data, whereas real-robot data collection is costly and safety-constrained. Simulation provides a scalable alternative, but zero-shot transfer depends not only on single-frame realism but also on whether simulated observations reproduce task-relevant feature changes…

---

## 📋 本日操作建议

**建议今日深读 (Top 3):**
1. [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](https://arxiv.org/abs/2608.30237v1) — score 21
2. [Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters](https://arxiv.org/abs/2608.28090v1) — score 19
3. [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618v1) — score 18

- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告
- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接
- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库
